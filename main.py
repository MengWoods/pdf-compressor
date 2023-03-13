#!/usr/bin/python3
import configargparse
from utils import pdfUtils

p = configargparse.ArgParser()
p.add('-b', '--base-path', default='./files', type=str, help='Base path to the PDF files for processing')
p.add('-i', '--input-files', required=True, nargs='+', help="Input PDF files name(s), add space between two files")
p.add('-f', '--font-size', default=10, help="Font size of the output PDF")
options = p.parse_args()

def main():
    pdf_compressor = pdfUtils.pdfCompressor(options.base_path, options.input_files, options.font_size)
    pdf_compressor.process()

if __name__ == "__main__":
    main()