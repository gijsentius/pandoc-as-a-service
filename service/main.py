import os
from typing import List, Optional

from fastapi import responses
from .internal.util import clean_workspace, create_folder, filename_output_with_path, filename_with_path, filename_without_extension, load_file, create_path
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import FileResponse
from .internal import pandoc


app = FastAPI()


@app.post("/convert")
async def convert_file(document: UploadFile = File(...),
                       bibliography: Optional[UploadFile] = None,
                       images: Optional[List[UploadFile]] = []):
    filename = filename_without_extension(document.filename)
    filename_output = filename + '.pdf'
    path_output = filename_output_with_path(filename_output)
    request_path = create_path(filename)
    request_filename_with_path = filename_with_path(document, request_path)
    bibliography_available = True if bibliography is not None else False

    # Create folder for request
    request_folder_available = create_folder(request_path)
    if not request_folder_available:
        pass  # return an server error
    image_folder_available = create_folder(request_path + "images")

    # Load all files on disk
    load_file(file=document, path=request_path)
    if bibliography_available:
        load_file(file=document, path=request_path)
    for image in images:
        load_file(file=image, path=request_path + "images")

    # Perform conversion
    pandoc.run_pandoc(request_filename_with_path, path_output)

    # After the conversion is finished succesfully clean the workspace
    clean_workspace([request_path, 'plantuml-images'])

    # return FileResponse(pdf_filepath)
    if os.path.exists(path_output):
        return FileResponse(path_output)
    else:
        return Response(status_code=500)
