from Backend.src.parser_generic import MedicalDocParser
import re

class Prescriptionparser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self): #returns a json or dictionary
        return {
            'patient_name':self.get_name(),
            'patient_address': self.get_address(),
            'medicines':self.get_medicine(),
            'direction':self.get_directions(),
            'refill': self.get_refill()
        }

    def get_name(self):
        name_filter = 'Name:(.*)Date:'
        name = re.findall(name_filter,self.text)
        if len(name)>0:
            return name[0].strip()
    def get_address(self):
        address_filter = 'Address:(.*)\n'
        name = re.findall(address_filter,self.text)
        if len(name)>0:
            return name[0].strip()
    def get_medicine(self):
        medicine_filter = 'Address:[^\n]*(.*)Directions'
        medicines = re.findall(medicine_filter, self.text, flags=re.DOTALL)
        if len(medicines)>0:
            return medicines[0].strip()
    def get_directions(self):
        directions_filter = 'Directions:(.*)Refill'
        directions = re.findall(directions_filter, self.text, flags=re.DOTALL)
        if len(directions)>0:
            return directions[0].strip()
    def get_refill(self):
        refill_times = 'Refill:(.*)times'
        refill = re.findall(refill_times, self.text, flags=re.DOTALL)
        if len(refill)>0:
            return refill[0].strip()

if __name__=='__main__':

    document_text='''Name: Maria Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    pp=Prescriptionparser(document_text)
    print(pp.parse())


