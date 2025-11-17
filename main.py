from phonebook_class import PhoneBook

PB = PhoneBook()

while True:
    print("Enter input number for input:")
    
    print(f"1 : for add Contacts(only enter first Name)")
    print(f"2 : for Search Contact")
    print(f"3 : for Delete Contact")
    print(f"4 : To show all Contacts")
    print(f"5 : To exit()")
    x = int(input())
    if x == 1:
        inp = input().split()
        PB.add_contact(inp[0],int(inp[1]))
    elif x == 2:
        inp = input()
        PB.search_contact(inp)
    elif x == 3:
        inp = input()
        PB.delete_contact(inp)
    elif x == 4:
        PB.showall_contact()
    elif x == 5:
        break
    else:
        print("Please enter Correct input")
