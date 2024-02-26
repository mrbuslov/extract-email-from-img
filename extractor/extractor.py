import easyocr
import re
from .consts import SUPPORTED_LANGS, EMAIL_PATTERN
from .utils import find_all_emails_in_txt, binarize_image

# this needs to run only once to load the model into memory
reader = easyocr.Reader(SUPPORTED_LANGS)


def extract_text(file_path: str) -> str:
    '''Extracts text from image from provided image path'''
    processed_img_bytes = binarize_image(file_path)
    txt_result = reader.readtext(
        processed_img_bytes, 
        detail=0, 
        paragraph=True,
        # width_ths = 0.5,
        # mag_ratio=1,
        beamWidth=5,
        min_size = 20,
        adjust_contrast = 0.5,
        link_threshold = 0.4,
    )
    return ' '.join(txt_result) if txt_result else ''


def extract_emails(file_path: str) -> list[str]:
    txt_result = extract_text(file_path)
    print('Found text: ', txt_result)
    return find_all_emails_in_txt(txt_result)

