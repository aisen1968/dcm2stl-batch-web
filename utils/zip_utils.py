import zipfile
from pathlib import Path

def create_zip(zip_path: Path, files: list[Path]) -> None:
    """Crea archivo ZIP con los archivos STL"""
    with zipfile.ZipFile(zip_path, 'w') as zf:
        for file in files:
            zf.write(file, arcname=file.name)