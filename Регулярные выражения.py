import re
import csv
from pprint import pprint

def normalize_phone_number(phone):
    pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(\s*доб\.\s*(\d+))?')
    normalized_phone = pattern.sub(r'+7(\2)\3-\4-\5\6', phone)
    return normalized_phone

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        contacts = [row for row in reader]
    return contacts


def split_fullname(contact):
    full_name = ' '.join(contact[:3]).split()
    lastname, firstname, surname = (full_name + [''] * 3)[:3]
    return [lastname, firstname, surname] + contact[3:]

def merge_contacts(contacts):
    contacts_dict = {}
    for contact in contacts:
        key = (contact[0], contact[1])  
        if key not in contacts_dict:
            contacts_dict[key] = contact
        else:
            for i in range(len(contact)):
                if contact[i]:
                    contacts_dict[key][i] = contact[i]
    return list(contacts_dict.values())

def clean_contacts(contacts):
    cleaned_contacts = []
    for contact in contacts:
        contact = split_fullname(contact)
        contact[5] = normalize_phone_number(contact[5])
        cleaned_contacts.append(contact)
    return merge_contacts(cleaned_contacts)

def write_csv(file_path, contacts):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


file_path = '/Users/mustafodavlatov/Desktop/Тс2101/phonebook_raw.csv'
contacts = read_csv(file_path)
cleaned_contacts = clean_contacts(contacts)

output_file_path = '/Users/mustafodavlatov/Desktop/Тс2101/phonebook new.csv'
write_csv(output_file_path, cleaned_contacts)


for contact in cleaned_contacts:
    pprint(contact)
    
    
