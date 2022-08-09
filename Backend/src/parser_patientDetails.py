from Backend.src.parser_generic import MedicalDocParser
import re

class PatientDetailsParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'phone_number': self.get_patient_phone_number(),
            'medical_problems': self.get_medical_problems(),
            'hepatitis_b_vaccination': self.get_hepatitis_b_vaccination()
        }

    def get_patient_name(self):
        def remove_noise_for_name(noisy_name):
            noisy_name= noisy_name.replace("Birth Date", "").strip()
            pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
            date_matches = re.findall(pattern, noisy_name)
            date=date_matches[0][0]
            noisy_name=noisy_name.replace(date,"").strip()
            return noisy_name

        name_filter = 'Patient Information(.*?)\(\d{3}\)'
        phrase = re.findall(name_filter, self.text, flags=re.DOTALL)  # flags = re.DOTALL is put to consider dot as new line
        final_name=''
        final_name=remove_noise_for_name(phrase[0])
        return final_name
    def get_patient_phone_number(self):
        phone_filter = 'Patient Information(.*?)(\(\d{3}\).\d{3}-\d{4})'
        phone_no = re.findall(phone_filter, self.text, flags=re.DOTALL)
        return phone_no[0][1].strip()
    def get_medical_problems(self):
        medprob_filter = 'List any Medical Problems \(asthma, seizures, headaches(\}|\)):(.*)'
        medprob = re.findall(medprob_filter, self.text, flags=re.DOTALL)
        return medprob[0][1].strip()
    def get_hepatitis_b_vaccination(self):
        vaccination_filter = 'Have you had the Hepatitis B vaccination\?.*(Yes|No|yes|no)'
        vaccination = re.findall(vaccination_filter, self.text, flags=re.DOTALL)
        return vaccination[0]

if __name__=='__main__':
    document_text='''17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine'''
    pp = PatientDetailsParser(document_text)
    print(pp.parse())

