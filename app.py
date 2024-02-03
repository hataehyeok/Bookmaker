import argparse
import src.make_pdf as make_pdf
import src.take_image as take_image

def main():
    parser = argparse.ArgumentParser(description='Capture Ebook\'s images and create a PDF.')
    
    parser.add_argument('folder_name', type=str, help='The name of the folder where images will be saved.')
    parser.add_argument('output_name', type=str, help='The name of the output PDF file.')
    parser.add_argument('page_count', type=int, help='The number of pages to capture.')
    
    args = parser.parse_args()
    args.output_name = args.output_name + '.pdf'

    take_image.capture_specific_area_with_screencapture(args.page_count, args.folder_name)
    make_pdf.images_to_pdf(args.folder_name, args.output_name)

if __name__ == '__main__':
    main()
