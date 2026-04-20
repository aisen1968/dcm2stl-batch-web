from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
import uuid

from config import INPUT_DIR, OUTPUT_DIR
from converter.open3sdcm_wrapper import convert_dcm_to_stl
from utils.zip_utils import create_zip

app = FastAPI(title="DCM to STL Batch Converter")

@app.post("/convert")
async def convert(files: list[UploadFile] = File(...)):
    job_id = str(uuid.uuid4())
    job_input = INPUT_DIR / job_id
    job_output = OUTPUT_DIR / job_id

    job_input.mkdir(parents=True)
    job_output.mkdir(parents=True)

    stl_files = []

    for uploaded in files:
        dcm_path = job_input / uploaded.filename
        with dcm_path.open("wb") as buffer:
            shutil.copyfileobj(uploaded.file, buffer)

        stl_name = dcm_path.stem + ".stl"
        stl_path = job_output / stl_name

        convert_dcm_to_stl(dcm_path, stl_path)
        stl_files.append(stl_path)

    zip_path = job_output / "result.stl.zip"
    create_zip(zip_path, stl_files)

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="DCM_to_STL_result.zip"
    )
