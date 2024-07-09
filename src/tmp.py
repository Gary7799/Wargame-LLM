import PyPDF2

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()

        for page_num in range(start_page - 1, end_page):
            page = reader.getPage(page_num)
            writer.addPage(page)

        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

input_pdf = '978-3-319-66299-2.pdf'  # 输入PDF文件名
output_pdf = 'output.pdf'  # 输出PDF文件名
start_page = 106  # 起始页码
end_page = 121  # 结束页码

extract_pages(input_pdf, output_pdf, start_page, end_page)
