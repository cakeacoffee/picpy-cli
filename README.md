# picpy-cli
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-blue?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Click__-white?style=for-the-badge&logo=python&logoColor=black)
![Black](https://img.shields.io/badge/Black-000000?style=for-the-badge&logo=python&logoColor=white)

A command-line tool for automating image processing tasks like resizing, format conversion, quality adjustment, and batch operations. Built with Python.

## Features/TODO:
- **Basic**
  - Resize Images, Crop,rotate
  - Convert Formats [JPEG, PNG, WebP, BMP, TIFF,PDF]
  - Adjust Quality [Control output image compression]
  - Apply Filters [Grayscale, blur, sharpen, contour, and edge enhance]
- **Batch Processing** [Process entire directories or wildcard patterns]
- **Auto-Rename** [Generate filenames with templates (e.g., date/time)]
- **Chart generator** [input data and produce a chart based on a style perameters (which can be set)]
- **AI Features**
  - upscale?
  - image gen?
  - image recognition

## Set Up
**1. Clone the Repository**
```
git clone https://github.com/cakeacoffee/picpy-cli.git
cd to_do_list
```
**2.  Environment Set up**

- Create Venv
```
python -m venv venv
```
- Activate environment

Mac/Linux
```
source venv/bin/activate
```
Windows
```
venv\Scripts\activate
```

**3. Install Dependencies**

```
pip install -r requirements.txt
```

## Dependencies and tools used
CLI tool: [Click](https://click.palletsprojects.com/en/stable/)

Code formatting: [Black](https://github.com/psf/black)
