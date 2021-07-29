import os
import subprocess
from subprocess import CompletedProcess
from typing import Dict, List, Final, Optional

PANDOC_CROSSREF_FLAG: Final[str] = ["-F", "pandoc-crossref"]
PANDOC_CITEPROC_FLAG: Final[str] = ["--citeproc"]
PANDOC_PLANTUML_FLAG: Final[str] = ["-F", "pandoc-plantuml"]

DEFAULT_TEMPLATE_FLAG: Final[List[str]] = ["--template", "eisvogel-default"]
DEFAULT_CSL_FLAG: Final[str] = ["--csl=styles/ieee.csl"]


def run_pandoc(input_file: str, output_file: str, flags: Optional[Dict[str, List[str]]] = {}) -> CompletedProcess:
    """Method to start a pandoc process to convert a file from input to ouput.

    Adding extra flags is optional.
    CSL and template are set by default to ieee.csl and eisvogel for the template.
    """
    template = flags['template'] if 'template' in flags else DEFAULT_TEMPLATE_FLAG
    csl = flags['csl'] if 'csl' in flags else DEFAULT_CSL_FLAG
    flags.pop('template', None)
    flags.pop('csl', None)
    base_command = ["pandoc", input_file, "-o", output_file]
    base_command.extend(PANDOC_CROSSREF_FLAG)
    base_command.extend(PANDOC_CITEPROC_FLAG)
    base_command.extend(PANDOC_PLANTUML_FLAG)
    base_command.extend(template)
    base_command.extend(csl)

    for flag in flags.values():
        base_command.extend(flag)
    process = subprocess.run(base_command)
    print(process)
    print(os.getcwd())
