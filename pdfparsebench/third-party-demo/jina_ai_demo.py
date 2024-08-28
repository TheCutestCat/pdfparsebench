import requests
import json
import base64

def extract_pdf_text_jina_ai(data_path, save_path_template):
    """
    Extracts text from a PDF using Jina AI and saves it to a markdown file.
    
    :param data_path: Path to the PDF file to extract.
    :param save_path_template: Template for saving the extracted content. 
                               It should include placeholders for 'method' and 'pdfname'.
    """
    method = 'jina_ai'
    pdf_name = data_path.split('/')[-1].replace('.pdf', '')

    url = 'https://r.jina.ai/'
    headers = {
        # 'Authorization': 'Bearer xxxxx', # this will let RPM larger
        'Content-Type': 'application/json'
    }

    # Read the PDF file and convert its content to base64
    with open(data_path, 'rb') as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')

    data = {
        "url": "https://example.com",
        "pdf": pdf_base64
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    extracted_text = response.text

    # Save the extracted content into a markdown file
    save_path = save_path_template.format(method=method, pdfname=pdf_name)

    with open(save_path, 'w') as f:
        f.write(extracted_text)

    print(f"Content extracted and saved to {save_path}")

if __name__ == "__main__":
    from base import pdf_example_path, save_result_path_template
    extract_pdf_text_jina_ai(pdf_example_path, save_result_path_template)
