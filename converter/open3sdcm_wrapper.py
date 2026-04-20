from pathlib import Path

def convert_dcm_to_stl(dcm_path: Path, stl_path: Path):
    """
    Convierte archivo DCM a STL usando Open3SDCM
    """
    # TODO: Implementar lógica de conversión real
    # Por ahora crea un archivo STL vacío para pruebas
    stl_path.write_text("# STL file placeholder")
