import pymupdf

if __name__ == "__main__":
    from base import pdf_example_path, save_result_path_template
    pdfname = pdf_example_path.split('/')[-1].replace('.pdf', '')
    save_path = save_result_path_template.format(file_name=file_name, pdfname=pdfname)
    doc = pymupdf.open("example.pdf") # open a document
    for page in doc: # iterate the document pages
        text = page.get_text() # get plain text encoded as UTF-8