import os
from typing import List, Optional

from fastapi import responses
from fastapi.middleware.cors import CORSMiddleware
from .internal.util import clean_workspace, create_folder, filename_output_with_path, filename_with_path, filename_without_extension, load_file, create_path
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import FileResponse
from .internal import pandoc


app = FastAPI(root_path="/api/v1")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

# origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/convert")
async def convert_file(document: UploadFile = File(...),
                       other: Optional[List[UploadFile]] = []):
    filename = filename_without_extension(document.filename)
    filename_output = filename + '.pdf'
    path_output = filename_output_with_path(filename_output)
    request_path = create_path(filename)
    request_filename_with_path = filename_with_path(document, request_path)

    # Create folder for request
    request_folder_available = create_folder(request_path)
    if not request_folder_available:
        pass  # return an server error
    other_folder_available = create_folder(request_path + "other")

    # Load all files on disk
    load_file(file=document, path=request_path)
    for other_file in other:
        load_file(file=other_file, path=request_path + "other")

    # Perform conversion
    pandoc.run_pandoc(request_filename_with_path, path_output)

    # After the conversion is finished succesfully clean the workspace
    clean_workspace([request_path, 'plantuml-images'])

    # return FileResponse(pdf_filepath)
    if os.path.exists(path_output):
        print(path_output)
        return FileResponse(path_output, filename=filename_output, media_type="application/pdf")
    else:
        return Response(status_code=500)
