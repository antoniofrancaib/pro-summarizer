import PyPDF2

pdf_file = 'assets/pdf/barbero22a.pdf'  
output_file = 'assets/output/extracted_text.txt'  

pdf_reader = PyPDF2.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

print(f"The PDF has {num_pages} pages.")

start_page = 0
end_page = 8

if start_page < 0 or end_page >= num_pages or start_page > end_page:
    print("Invalid page range. Please check your input and try again.")
else:
    extracted_text = ''
    for page_num in range(start_page, end_page + 1):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        if text:
            extracted_text += text + '\n'
        else:
            print(f"Warning: No text found on page {page_num + 1}.")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(extracted_text)

    print(f"Text extracted from pages {start_page + 1} to {end_page + 1} and saved to '{output_file}'.")
