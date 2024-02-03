from PIL import Image
import os
import re
from PyPDF2 import PdfMerger

def natural_keys(text):
    return [int(c) if c.isdigit() else c for c in re.split('(\d+)', text)]

def images_to_pdf(image_folder, output_pdf):
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png') or f.endswith('.jpg')]
    image_files.sort(key=natural_keys)

    merger = PdfMerger()

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        pdf_path = os.path.splitext(image_path)[0] + '.pdf'
        image.save(pdf_path, "PDF", resolution=100.0)

        merger.append(pdf_path)

    merger.write(output_pdf)
    merger.close()
