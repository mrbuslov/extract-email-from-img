import argparse, sys
from extractor.extractor import extract_emails


parser=argparse.ArgumentParser()
parser.add_argument("--input", help="path to input image")
parser.add_argument("--output", help="path to output text file")
args=parser.parse_args()


def main(path_to_input_image: str, path_to_output_text_file: str) -> str:
    emails_lst = extract_emails(path_to_input_image)

    res = (
        f'Found emails: {", ".join(emails_lst)}'
        if emails_lst
        else 'No emails found'
    )
    print('Result:', res)
    with open(path_to_output_text_file, 'w') as file:
        file.write(res)

if __name__ == "__main__":
    path_to_input_image = args.input
    path_to_output_text_file = args.output
    main(path_to_input_image, path_to_output_text_file)

