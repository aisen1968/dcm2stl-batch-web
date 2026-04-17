from zipfile import ZipFile
from pathlib import Path

def create_zip(zip_path: Path, files: list[Path]):
    with ZipFile(zip_path, "w") as zipf:
        for file in files:
            zipf.write(file, arcname=file.name)
