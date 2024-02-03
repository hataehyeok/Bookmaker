from PIL import Image
import os
from PyPDF2 import PdfMerger

def images_to_pdf(image_folder, output_pdf):
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png') or f.endswith('.jpg')]
    image_files.sort()

    merger = PdfMerger()

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        pdf_path = os.path.splitext(image_path)[0] + '.pdf'
        image.save(pdf_path, "PDF", resolution=100.0)

        merger.append(pdf_path)

    merger.write(output_pdf)
    merger.close()
