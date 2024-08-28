from pypdf import PdfReader

def extract_pdf_text_to_markdown(data_path, save_path_template):
    """
    Extracts text from a PDF and saves it to a markdown file.
    
    :param data_path: Path to the PDF file to extract.
    :param save_path_template: Template for saving the extracted content. 
                               It should include placeholders for 'method' and 'pdfname'.
    """
    method = 'pypdf'
    pdf_name = data_path.split('/')[-1].replace('.pdf', '')
    
    reader = PdfReader(data_path)
    extracted_text = ""
    
    for i, page in enumerate(reader.pages):
        text = page.extract_text() if page.extract_text() else "[No extractable text]\n"
        extracted_text += f"## Page {i + 1}\n\n{text}\n\n"
    
    save_path = save_path_template.format(method=method, pdfname=pdf_name)
    
    with open(save_path, 'w') as f:
        f.write(extracted_text)
    
    print(f"Content extracted and saved to {save_path}")

if __name__ == "__main__":
    from base import pdf_example_path, save_result_path_template
    extract_pdf_text_to_markdown(pdf_example_path, save_result_path_template)