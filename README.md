# pdf-compressor
Compress PDF file's pages and size. It helps you try the free-version [ChatPDF](https://www.chatpdf.com/) with large-size file.

## Introduction

A light-weight tool to compress PDF file's pages and size. The processing loses origin file's format, only the text information is saved in the compressed result.

With default font size 10, the compressing result looks like:
```bash
$ python main.py -i input.pdf
File size (bytes):      15114015----> 45828
Page count:             23 --------> 15
```
By setting the font size smaller to 5:
```bash
$ python main.py -i symmetry.pdf -f 5
File size (bytes):      15114015----> 31638
Page count:             23 --------> 4
```

## Requirements

In Python 3.X envrionment, install reqirements by `pip install -r requirements.txt`

## Usage
1. Clone the repository, put PDF file(s) to `./files` folder.
`python main.py -h` to check arguments' meanings. 
2. One typical usage command is:
    ```
    python main.py -i input.pdf
    ```