import os
import subprocess
from subprocess import CompletedProcess
from typing import Dict, List, Final, Optional

PANDOC_CROSSREF_FLAG: Final[str] = "-F pandoc-crossref"
PANDOC_CITEPROC_FLAG: Final[str] = "-F pandoc-citeproc"
PANDOC_PLANTUML_FLAG: Final[str] = "-F " + \
    os.getcwd() + "/resources/plantuml/plantuml.py"

DEFAULT_TEMPLATE_FLAG: Final[str] = "--template eisvogel"
DEFAULT_CSL_FLAG: Final[str] = "--csl=ieee.csl"


def run_pandoc(input_file: str, output_file: str, flags: Optional[Dict[str, str]] = {}) -> CompletedProcess:
    """Method to start a pandoc process to convert a file from input to ouput.

    Adding extra flags is optional.
    CSL and template are set by default to ieee.csl and eisvogel for the template.
    """
    template = flags['template'] if 'template' in flags else DEFAULT_TEMPLATE_FLAG
    csl = flags['csl'] if 'csl' in flags else DEFAULT_CSL_FLAG
    base_command = ["pandoc", input_file,
                    "-o " + output_file,
                    PANDOC_CROSSREF_FLAG, PANDOC_CITEPROC_FLAG, PANDOC_PLANTUML_FLAG,
                    template, csl]
    print(base_command)
