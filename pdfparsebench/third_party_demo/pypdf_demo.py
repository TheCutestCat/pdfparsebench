from pypdf import PdfReader
import os

def extract_pdf_text_PdfReader(data_path, save_path):
    """
    Extracts text from a PDF and saves it to a markdown file.
    
    :param data_path: Path to the PDF file to extract.
    :param save_path_template: Template for saving the extracted content. 
                               It should include placeholders for 'method' and 'pdfname'.
    """
    if not os.path.isfile(data_path):
        raise ValueError(f"The data_path '{data_path}' must be a file.")
    
    if os.path.basename(save_path) == "":
        raise ValueError(f"The save_path '{save_path}' must be a valid file name.")
    directory = os.path.dirname(save_path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    reader = PdfReader(data_path)
    extracted_text = ""
    
    for i, page in enumerate(reader.pages):
        text = page.extract_text() if page.extract_text() else "[No extractable text]\n"
        extracted_text += f"## Page {i + 1}\n\n{text}\n\n"
        
    with open(save_path, 'w') as f:
        f.write(extracted_text)
    
    print(f"Content extracted and saved to {save_path}")

if __name__ == "__main__":
    file_name = "pypdf.md"
    from base import pdf_example_path, save_result_path_template
    pdfname = pdf_example_path.split('/')[-1].replace('.pdf', '')
    save_path = save_result_path_template.format(file_name=file_name, pdfname=pdfname)

    extract_pdf_text_PdfReader(pdf_example_path, save_path)