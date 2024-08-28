## pdfparsebench
this is a benchmark of current pdf parse open-source method.


## Usage

To run the pdfparsebench benchmark using the example PDF file `pdfphrase_example.pdf`.

Use the following command:

fill the ```OPENAI_API_KEY``` and ```OPENAI_BASE_URL``` in ```.env.example``` and change the name to ```.env```

```python pdfparsebench/main.py --path ./test_data/example/pdfphrase_example.pdf```

the result is in the folder ```test_result```, currently we have : ``` jina.ai ``` ``` pypdf ``` ``` gptpdf ```

## todo
use [modal](https://modal.com/) to run the method that need GPU

## method list
- [x] **Jina ai** [Link](https://r.jina.ai/)
- [x] **PyPDF** [Link](https://github.com/py-pdf/pypdf)
- [x] **GPTPDF** [Link](https://github.com/CosmosShadow/gptpdf)
- [ ] **Marker** [Link](https://github.com/VikParuchuri/marker) # need GPU skip~
- [ ] **llm-graph-builder** [Link](https://github.com/neo4j-labs/llm-graph-builder) # too complex
- [ ] **Ragflow** [Link](https://github.com/infiniflow/ragflow) # need GPU
- [ ] **Kit** [Link](https://github.com/opendatalab/PDF-Extract-Kit) # need GPU
- [ ] **ZeroX** [Link](https://github.com/getomni-ai/zerox) # same method with GPTPDF
- [ ] **Omniparse** [Link](https://github.com/adithya-s-k/omniparse) # need GPU
- [x] **MinerU** [Link](https://github.com/opendatalab/MinerU) # need GPU [online demo](https://opendatalab.com/OpenSourceTools/Extractor/PDF)    [example reuslt](https://opendatalab.com/OpenSourceTools/Extractor/PDF/4a1ded1b-8dd7-4344-a34f-c919ffa333bb)
- [ ] **PyMuPDF** [Link](https://github.com/pymupdf/PyMuPDF)
- [ ] **PDFPlumber** [Link](https://github.com/jsvine/pdfplumber)
- [ ] **Camelot** [Link](https://github.com/camelot-dev/camelot)

