import re
from typing import Dict, Callable
from mongoengine_example.records import Record


def change_name():
    while True:
        old_name = input("\n>>> 0) to enter the main menu change\n<< Write contact name for a change: ").strip()
        if old_name == "0":
            return '\n>>> You enter the main menu change <<<'
        try:
            record = Record(name=old_name)
            if old_name == record.find_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {old_name}! <<<\n     >>>Choose another name <<<")
    while True:
        new_name = input("\n>>> 0) to enter the main menu add\n<< Write new contact name: ").strip()
        if new_name == "0":
            return '\n>>> You enter the main menu add<<<'
        try:
            record = Record(name=new_name)
            if new_name == record.find_contact_by_name().name:
                print(f"\n>>> You have a contact {new_name}! <<<\n     >>>Choose another name <<<")
        except AttributeError:
            break
    record.update_name(old_name)
    return f"Contact name: {old_name} new contact name: {new_name}"


def change_phone():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu change\n<< Write contact name for a change phone: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu change <<<'
        try:
            record = Record(name=name_cont)
            if name_cont == record.find_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")

    phones = record.find_phone()
    print(f"Contact: {name_cont} have this phone:")
    for phone in phones:
        print(phone.phone)

    while True:
        old_phone = input("\n>>> 0) to enter the main menu change\n<< Enter the phone to change: ").strip()
        if old_phone == "0":
            return '\n>>> You enter the main menu change <<<'
        if old_phone in [phone.phone for phone in phones]:
            break
        print(f">>> Contact: {name_cont} does not have a phone {old_phone} <<<")

    while True:
        new_phone = input("\n>>> 0) to enter the main menu change\n<< Write new phone: ").strip()
        if new_phone == "0":
            return '\n>>> You enter the main menu change <<<'
        if len(new_phone) == 10 and new_phone.isnumeric():
            break
        print("<<< Phone must contains 10 symbols and only numbers >>>\n        <<<Write correct new phone>>>")

    record = Record(phone=new_phone, name=name_cont)
    record.update_phone(old_phone)
    return f"Contact: {record.name} now has a new phone: {record.phone}"


def change_email():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu change\n<< Write contact name for a change email: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu change <<<'
        try:
            record = Record(name=name_cont)
            if name_cont == record.find_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")

    emails = record.find_email()
    print(f"Contact: {name_cont} have this emails:")
    for email in emails:
        print(email.email)

    while True:
        old_email = input("\n>>> 0) to enter the main menu change\n<< Enter the email you want to change: ").strip()
        if old_email == "0":
            return '\n>>> You enter the main menu change <<<'
        if old_email in [email.email for email in emails]:
            break
        print(f">>> Contact: {name_cont} does not have a phone with this id <<<")

    while True:
        new_email = input("\n>>> 0) to enter the main menu change\n<< Write new email: ").strip()
        if new_email == "0":
            return '\n>>> You enter the main menu change <<<'
        new_value = re.findall(r"[a-zA-z]{1}[\w+\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", new_email)
        if len(new_value) >= 1:
            email = str(new_value[0])
            break
        print(">>> You write invalid email <<<\n     >>>Choose another name <<<")
    record = Record(name=name_cont, email=email)
    record.update_email(old_email)
    return f"Contact: {record.name} now has a new email: {record.email}"


def exit_handler():
    raise SystemExit('>>> You enter the main menu <<<')


FUNC: Dict[str, Callable] = {
    "1": change_name,
    '2': change_phone,
    '3': change_email,
    '0': exit_handler
}

HELP_DICT = {
    '1': 'change name',
    '2': 'change phone',
    '3': 'change email',
}


def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n")
        i += 1
    return help_text + f"> 0) Exit to main menu"


def main_change():
    while True:
        print(menu_help())
        user_input = input('\n<< Enter the command: ').strip()
        try:
            command_func = FUNC.get(user_input, None)
            command_func = command_func()
            if command_func != None:
                print(command_func)
            else:
                return '\n >>> Unknown command <<<'
        except TypeError:
            print('Unknown command or parametrs, please try again.')
        except SystemExit as e:
            return e