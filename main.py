from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def main():
    pdf_filepath = ""
    return FileResponse(pdf_filepath)
