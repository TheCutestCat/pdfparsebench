from gptpdf import parse_pdf
import os

def extract_pdf_text_gptpdf(data_path, save_folder,api_key,base_url, gpt_worker = 10):
    if not os.path.isfile(data_path):
        raise ValueError(f"The data_path '{data_path}' must be a file.")
    content, image_paths = parse_pdf(data_path,output_dir=save_folder, api_key=api_key,base_url=base_url, gpt_worker= gpt_worker)

    print(f"Content saved to {os.path.join(save_folder, 'content.md')}")
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

    extract_pdf_text_gptpdf(pdf_example_path, save_path ,api_key,base_url, gpt_worker = 10)
