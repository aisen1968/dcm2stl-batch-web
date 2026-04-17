import subprocess
from pathlib import Path
from config import OPEN3SDCM_BIN

def convert_dcm_to_stl(dcm_path: Path, stl_path: Path):
    """
    Convierte un archivo DCM 3Shape a STL usando Open3SDCM
    """
    result = subprocess.run(
        [OPEN3SDCM_BIN, str(dcm_path), "-o", str(stl_path)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)
