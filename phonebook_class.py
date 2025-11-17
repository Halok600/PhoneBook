
'''import json
file_path = 'Phonebook.json'
PB = {}
try:
    with open(file_path,"r") as file:
        PB = json.load(file)
except FileNotFoundError:
    PB = {}
def addContact(name,num):
    PB[name] = num
    with open(file_path,"w") as file:
        json.dump(PB,file,indent  = 4)
def search(name):
    if not PB:
        print("PhoneBook is Empty")
    else:
        if name in PB:
            print(f"The Contact for {name} is {PB[name]}")
        else:
            print(f"{name} not found!")
def delete_contact(name):
    if name in PB:
        del PB[name]
        with open(file_path,"w") as file:
            json.dump(PB,file,indent  = 4)
    else:
        print(f"{name} not found!!")

def showall():
    print(PB)



while True:
    print("Enter input number for input:")
    
    print(f"1 : for add Contacts(only enter first Name)")
    print(f"2 : for Search Contact")
    print(f"3 : for Delete Contact")
    print(f"4 : To show all Contacts")
    print(f"5 : To exit()")
    x = int(input())
    if x == 1:
        print("Enter name and number with space")
        lists = input().split()
        addContact(lists[0],int(lists[1]))
    elif x == 2:
        print("Enter name to search")
        name = input()
        search(name)
    elif x == 3:
        print("Enter name to delete")
        name = input()
        delete_contact(name)
    elif x == 4:
        showall()
    elif x == 5:
        break
    else:
        print("Wrong input, try again")
'''

import json

class PhoneBook:
    def __init__(self):
        self.file_path = "Phonebook.json"
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        try:
            with open(self.file_path,"r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    def save_contacts(self):
        with open(self.file_path,"w") as file:
            json.dump(self.contacts,file,indent = 4)
    
    def add_contact(self,name,num):
        
        self.contacts[name] = num
        self.save_contacts()
        print(f"Contact saved!")
    
    def search_contact(self,name):
        if name in self.contacts:
            print(f"{name} : {self.contacts[name]}")
        else:
            print(f"Contact not Found!!")
    def delete_contact(self,name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
        else:
            print(f"Contact {name} does not exist!!!")
    def showall_contact(self):
        if not self.contacts:
            print("PhoneBook is empty")
        else:
            print("Contacts")
            for name,num in self.contacts.items():
                print(f"{name} : {num}")