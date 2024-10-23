d = {}
print('Console Application // Phone Book')
print('''Choose a function number:

 >>>> 1 > add contact
 >>>> 2 > delete contact
 >>>> 3 > open phone book
 >>>> 4 > change phone number
 >>>> 5 > exit''')

commands = ['1', '2', '3', '4', '5']

def validate_number(number):
    while not number.isdigit() or len(number) < 10:
        if not number.isdigit():
            number = input('Enter the phone number as digits: ')
        else:
            number = input('Enter the number correctly (as digits and 10 characters long (or a little longer)): ')
    return number




def add_name():
    name = input('Enter a name for the contact: ').title()
    if name in d:
        print('Contact is already in the phone book')
    else:
        number = validate_number(input('Enter contact number: '))
        d[name] = number
        print('Contact added!')

def delete_contact():
    delete = input('Enter contact name: ').title()
    while delete not in d:
        delete = input('''This contact is not in your book
                Enter an existing contact: ''').title()
    del d[delete]
    print('Contact deleted!')

def open_phone_book():
    if not d:
        print('Contact list is empty')
    else:
        print('Contact list')
        for key, value in sorted(d.items()):
            print(f'{key} -- {value}')

def change_phone_number():
    change = input('Enter the name of the contact whose number you want to change: ').title()
    if change not in d:
        print('Contact not found')
    else:
        number = validate_number(input('Enter contact number: '))
        d[change] = number
        print('Contact number changed!')

while True:
    task = input('Enter function number: ')

    while task not in commands:
        task = input('Enter a valid function: ')

    if task == commands[4]:
        print('Enter complete')
        exit()
    elif task == commands[0]:
        add_name()
    elif task == commands[1]:
        delete_contact()
    elif task == commands[2]:
        open_phone_book()
    elif task == commands[3]:
        change_phone_number()
