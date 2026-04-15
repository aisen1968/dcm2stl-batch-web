# dcm2stl-batch-web
Transforma ficheros DCM  a STL
# DCM to STL Batch Converter (3Shape)

Web application to convert multiple 3Shape DCM files into STL in batch mode.

## Features
- Upload multiple .DCM files
- Convert to STL server-side
- Download all STL files as a ZIP
- No client-side installation

## Tech stack
- Backend: Python (FastAPI)
- Frontend: HTML + JavaScript
- Converter: Open3SDCM
- Deployment: Docker / Server

## Compliance
- No external SaaS dependency
- No execution on client machine
- Temporary files are deleted after download
