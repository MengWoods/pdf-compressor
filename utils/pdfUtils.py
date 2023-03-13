#!/usr/bin/python3
import os
from PyPDF2 import PdfReader
import textwrap
from fpdf import FPDF

class pdfCompressor:
    def __init__(self, base_path, pdf_file_list, font_size):
        self.file_name_list = pdf_file_list
        self.absolute_path = os.path.abspath(base_path)
        self.font_size = font_size

    def process(self):
        for i in range(len(self.file_name_list)):
            self.getFileInfo(self.file_name_list[i])
            self.ocrAndSaveTxt()
            self.txtTrim()
            self.txtToPdf()
            self.printSummary()

    def getFileInfo(self, file_name):
        self.file_name = file_name
        self.file_name_without_extenstion = os.path.splitext(self.file_name)[0]
        self.path_to_file = self.absolute_path + '/' + self.file_name
        self.path_to_result = self.absolute_path + '/' + self.file_name_without_extenstion + '_compressed' + '.pdf'
        self.path_to_txt = self.absolute_path + '/' + self.file_name_without_extenstion + '.txt'

    def ocrAndSaveTxt(self):
        with open(self.path_to_file, 'rb') as pdf:
            pdf_reader = PdfReader(pdf)
            with open(self.path_to_txt, 'w') as f:
                for j in range (len(pdf_reader.pages)):
                    page = pdf_reader.pages[j]
                    f.write(page.extract_text())
            pdf.close()

    def txtTrim(self):
        with open(self.path_to_txt, 'r') as f:
            text = f.read()
        text = text.replace('\n', '')
        with open(self.path_to_txt, 'w') as f:
            f.write(text)

    def txtToPdf(self):
        with open(self.path_to_txt, 'r', encoding='latin-1') as f:
            text = f.read()
        a4_width_mm = 210
        pt_to_mm = 0.35
        fontsize_pt = float(self.font_size)
        fontsize_mm = fontsize_pt * pt_to_mm
        margin_bottom_mm = 5
        character_width_mm = 7 * pt_to_mm
        width_text = a4_width_mm / character_width_mm * (10 / fontsize_pt)
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(True, margin=margin_bottom_mm)
        pdf.add_page()
        pdf.set_font(family='Courier', size=fontsize_pt)
        splitted = text.split('\n')
        for line in splitted:
            lines = textwrap.wrap(line, width_text)
            if len(lines) == 0:
                pdf.ln()
            for wrap in lines:
                pdf.cell(0, fontsize_mm, wrap, ln=1)
        pdf.output(self.path_to_result, 'F')

    def printSummary(self):
        with open(self.path_to_file, 'rb') as f:
            pdf = PdfReader(f)
            origin_num_pages = len(pdf.pages)
        with open(self.path_to_result, 'rb') as f:
            pdf = PdfReader(f)
            result_num_pages = len(pdf.pages)
        origin_file_size = os.path.getsize(self.path_to_file)
        result_file_size = os.path.getsize(self.path_to_result)
        print(f'File size (bytes):\t{origin_file_size}----> {result_file_size}')
        print(f'Page count: \t\t{origin_num_pages} --------> {result_num_pages}')
        print('=========================================')
        print('[INFO] Result is saved to:', self.path_to_result)
        print('[INFO] If need compress further, try lower the font size by tuning argument -f.')


