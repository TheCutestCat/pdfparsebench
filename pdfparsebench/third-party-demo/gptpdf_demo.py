from gptpdf import parse_pdf
import os

def extract_pdf_text_gptpdf(data_path, save_folder,api_key,base_url):
    if not os.path.isdir(save_folder):
        raise ValueError(f"The save_folder '{save_folder}' must be a directory.")
    if not os.path.isfile(data_path):
        raise ValueError(f"The data_path '{data_path}' must be a file.")
    content, image_paths = parse_pdf(data_path,output_dir=save_path, api_key=api_key,base_url=base_url)

    # Ensure that the directory exists before writing
    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the content to a text file
    with open(os.path.join(save_path, 'output.txt'), 'w') as f:
        f.write(content)

    print(f"Content saved to {os.path.join(save_path, 'content.txt')}")
    return None

if __name__ == "__main__":
    file_name = "/gptpdf/"

    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_BASE_URL')

    from base import pdf_example_path, save_result_path_template

    pdfname = pdf_example_path.split('/')[-1].replace('.pdf', '')
    save_path = save_result_path_template.format(file_name=file_name, pdfname=pdfname)

    extract_pdf_text_gptpdf(pdf_example_path, save_path ,api_key,base_url)
