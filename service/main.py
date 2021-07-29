import os
from typing import List, Optional
from .internal.util import clean_workspace, create_folder, filename_without_extension, load_file, create_path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from .internal import pandoc


app = FastAPI()


@app.post("/convert")
async def convert_file(document: UploadFile = File(...),
                       bibliography: Optional[UploadFile] = None,
                       images: Optional[List[UploadFile]] = []):
    filename = filename_without_extension(document.filename)
    request_path = create_path(filename)
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
    pandoc.run_pandoc(document.filename, filename + '.pdf')

    # Create respons from pdf
    

    # After the conversion is finished succesfully clean the workspace
    clean_workspace(request_path)

    # return FileResponse(pdf_filepath)
    return {"filename": document.filename,
            "images": [file.filename for file in images],
            "filename_without_extension": filename, "request_path": request_path}
