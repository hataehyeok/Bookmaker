import argparse
import os
import src.make_pdf as make_pdf
import src.take_image as take_image

def main():
    parser = argparse.ArgumentParser(description='Capture Ebook\'s images and create a PDF.')
    
    parser.add_argument('folder_name', type=str, help='The name of the folder where images will be saved.')
    parser.add_argument('output_name', type=str, help='The name of the output PDF file.')
    parser.add_argument('page_count', type=int, help='The number of pages to capture.')
    
    args = parser.parse_args()

    # page_count should be a positive integer
    if args.page_count <= 0:
        parser.error('The page_count must be a positive integer.')

    # folder_name will be saved in the 'book_image' folder
    image_folder_path = os.path.join('book_image', args.folder_name)
    if not os.path.exists(image_folder_path):
        os.makedirs(image_folder_path)
        print(f"Note: The folder '{image_folder_path}' has been created.")

    # Ensure output_name has the '.pdf' extension
    if not args.output_name.lower().endswith('.pdf'):
        args.output_name += '.pdf'

    # Save the output PDF in the 'output_pdf' folder
    output_pdf_path = os.path.join('output_pdf', args.output_name)
    if not os.path.exists(os.path.dirname(output_pdf_path)):
        os.makedirs(os.path.dirname(output_pdf_path))
        print(f"Note: The folder '{os.path.dirname(output_pdf_path)}' has been created.")

    take_image.capture_specific_area_with_screencapture(args.page_count, image_folder_path)
    make_pdf.images_to_pdf(image_folder_path, output_pdf_path)

if __name__ == '__main__':
    main()
