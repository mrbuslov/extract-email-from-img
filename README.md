# Email Extractor from Image

This Python script extracts email addresses from an image. 
It receives the path to the input image and the path to the output text file as parameters.

## Installation
- `python3 -m venv venv` - create venv
- `. venv/bin/activate` - activate venv
- `pip install -r requirements.txt` - install required libs

## Usage
NOTE: you can use emages from ***extractor*** package. Path: `extractor/test-images`
 
``
python3 main.py --input <path_to_input_image> --output <path_to_output_text_file> 
example:
python3 main.py --input extractor/test-images/image-2.png --output output.txt
``

## Important Notes!
- In this project I didn't use `pytesseract` library, because I couldn't reach the precision as with `easyocr`.
- `easyocr` lib is multilingual. [Project repo](https://github.com/JaidedAI/EasyOCR)
- `easyocr` lib [Supoorted languages](https://github.com/JaidedAI/EasyOCR?tab=readme-ov-file)
- The image preprocesses before extracting via `opencv` lib - it thresholds (binarizes). This should be improved
- [finetune easyocr's readtext](https://github.com/JaidedAI/EasyOCR/issues/460#issuecomment-872079091)
- [finetune easyocr's model](https://github.com/JaidedAI/EasyOCR/blob/master/custom_model.md)

## To be done
- extract text/emails with LLM
