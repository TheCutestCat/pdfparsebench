from third_party_demo.jina_ai_demo import extract_pdf_text_jina_ai
from third_party_demo.gptpdf_demo import extract_pdf_text_gptpdf
from third_party_demo.pypdf_demo import extract_pdf_text_PdfReader
import os
from argparse import ArgumentParser

if __name__ == "__main__":

    parser = ArgumentParser(description="Process PDF with different parsers.")
    parser.add_argument('--path', type=str, required=True, help="Path to the PDF file.")
    args = parser.parse_args()

    pdf_example_path = args.path
    
    pdfname = pdf_example_path.split('/')[-1].replace('.pdf', '')
    save_result_path_template = "./test_result/{pdfname}/{file_name}"

    save_path_pypdf = save_result_path_template.format(file_name='pypdf.md', pdfname=pdfname)
    save_path_jina_ai = save_result_path_template.format(file_name='jina_ai.md', pdfname=pdfname)
    save_path_gptpdf = save_result_path_template.format(file_name='gptpdf/', pdfname=pdfname)

    # openai api
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_BASE_URL')

    extract_pdf_text_PdfReader(pdf_example_path, save_path_pypdf)
    extract_pdf_text_jina_ai(pdf_example_path, save_path_jina_ai)
    extract_pdf_text_gptpdf(pdf_example_path, save_path_gptpdf ,api_key,base_url) 
