import requests
import json
import base64
import os

def extract_pdf_text_jina_ai(data_path, save_path):
    """
    Extracts text from a PDF using Jina AI and saves it to a markdown file.
    
    :param data_path: Path to the PDF file to extract.
    :param save_path_template: Template for saving the extracted content. 
                               It should include placeholders for 'method' and 'pdfname'.
    """

    if not os.path.isfile(data_path): raise ValueError(f"The data_path '{data_path}' must be a file.")
    if os.path.basename(save_path) == "": raise ValueError(f"The save_path '{save_path}' must be a valid file name.")
    directory = os.path.dirname(save_path)
    if not os.path.exists(directory): os.makedirs(directory)

    url = 'https://r.jina.ai/'
    headers = {
        # 'Authorization': 'Bearer xxxxx', # this will let RPM larger
        'Content-Type': 'application/json'
    }
    with open(data_path, 'rb') as pdf_file: pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')

    data = {
        "url": "https://example.com",
        "pdf": pdf_base64
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    extracted_text = response.text

    with open(save_path, 'w') as f:
        f.write(extracted_text)
    print(f"Content extracted and saved to {save_path}")

if __name__ == "__main__":

    file_name = "jina_ai.md"
    from base import pdf_example_path, save_result_path_template
    pdfname = pdf_example_path.split('/')[-1].replace('.pdf', '')
    save_path = save_result_path_template.format(file_name=file_name, pdfname=pdfname)

    extract_pdf_text_jina_ai(pdf_example_path, save_path)
