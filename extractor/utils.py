import re
import cv2
from .consts import SUPPORTED_LANGS, EMAIL_PATTERN


def find_all_emails_in_txt(text: str) -> list[str]:
    return re.findall(EMAIL_PATTERN, text)


def binarize_image(image_path) -> bytes:
    '''Binarizes the image for better extraction'''
    
    # ----- V1 ------
    # NOTE: thresholding is not for all images, but this is the best option.
    # you can leave gray_image, but it's not the best.
    # pick the best here https://docs.opencv2.org/4.x/d7/d4d/tutorial_py_thresholding.html
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 170, 255, cv2.THRESH_BINARY)


    # # ----- V2 ------
    # image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # image = cv2.medianBlur(image,5)
    # binary_image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #             cv2.THRESH_BINARY,11,2)

    # cv2.imwrite('binary_image.jpg', binary_image)
    return binary_image
