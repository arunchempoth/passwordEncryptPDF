from PyPDF2 import PdfFileReader, PdfFileWriter

INPUT_FILE=""
OUTPUT_FILE=""
PASSWORD=""

with open(INPUT_FILE, "rb") as in_file:
    input_pdf = PdfFileReader(in_file)

    output_pdf = PdfFileWriter()
    output_pdf.appendPagesFromReader(input_pdf)
    output_pdf.encrypt(PASSWORD)

    with open(OUTPUT_FILE, "wb") as out_file:
        output_pdf.write(out_file)