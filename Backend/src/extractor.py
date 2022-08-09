from pdf2image import convert_from_path
import pytesseract
import util
from parser_prescription import Prescriptionparser
from parser_patientDetails import PatientDetailsParser
pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH=r'C:\poppler-22.04.0\Library\bin'

def extract(file_path,file_format):

        pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
        document_text=""
        processed_image=util.preprocess_image(pages[0])
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text='\n'+text

        if file_format=='prescription':
            extracted_data=Prescriptionparser(document_text).parse()
        elif file_format=='patient_details':
            extracted_data = PatientDetailsParser(document_text).parse()
        else:
            raise Exception(f"Invalid document format: {file_format}")
        return extracted_data

if __name__=='__main__':
    data=extract('../resources/prescription/pre_1.pdf','prescription')
    print(data)