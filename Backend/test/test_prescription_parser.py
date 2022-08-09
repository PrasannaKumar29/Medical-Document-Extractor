from Backend.src.parser_prescription import Prescriptionparser
import pytest

@pytest.fixture()
def doc_1_maria(): #though this is looking like a function, by putting the word '@pytest.fixture',doc_1_maria can be used as a return value of that function
    document_text = '''Name: Maria Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    '''
    return Prescriptionparser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text= ''' Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times'''
    return Prescriptionparser(document_text)

@pytest.fixture()
def doc_3_empty():
    return Prescriptionparser('')

def test_get_name(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_name()=='Maria Sharapova'
    assert doc_2_virat.get_name()=='Virat Kohli'
    assert doc_3_empty.get_name()==None

def test_get_address(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_address() == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_address()== '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_address() == None

def test_get_medicine(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_medicine() == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert doc_2_virat.get_medicine()== '| Omeprazole 40 mg'
    assert doc_3_empty.get_medicine() == None

def test_get_directions(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_directions() == 'Prednisone, Taper 5 mg every 3 days,\n    Finish in 2.5 weeks a\n    Lialda - take 2 pill everyday for 1 month'
    #assert doc_2_virat.get_directions() == 'Use two tablets daily for three months'
    assert doc_3_empty.get_directions() == None

def test_get_refill(doc_1_maria,doc_2_virat,doc_3_empty):
    assert doc_1_maria.get_refill() == '2'
    assert doc_2_virat.get_refill()== '3'
    assert doc_3_empty.get_refill() == None