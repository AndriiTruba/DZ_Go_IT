import re
from typing import Dict, Callable
from database.repository import Record, CellPhone, EmailAddress, Name


def add_contact():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu add\n<< Write contact name: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu add<<<'
        try:
            name = Name(name_cont)
            record = Record(name=name)
            if name_cont == record.get_contact_by_name().name:
                print(f"\n>>> You have a contact {name_cont}! <<<\n     >>>Choose another name <<<")
        except AttributeError:
            break
    name = Name(name_cont)
    record = Record(name=name)
    record.save_contact()

    while True:
        phone_cont = input("\n>>> 0) to enter the main menu add\n<< Write phone: ").strip()
        if phone_cont in [phone.phone for phone in record.get_all_phones()]:
            print(f"\n<<< You have a phone {phone_cont} in other contact! >>>\n     >>>Choose another phone <<<")
            continue
        if phone_cont == "0":
            print(f">>>was added name: {name.value}, phone: {None}, email: {None}")
            return '\n>>> You enter the main menu add <<<'
        if len(phone_cont) == 10 and phone_cont.isnumeric():
            break
        print("<<< Phone must contains 10 symbols, only numbers>>>\n        <<<Write correct phone>>>")
    phone_cont = CellPhone(phone_cont)
    rec = Record(name=name, phones=phone_cont)
    rec.save_phone()

    while True:
        email_cont = input("\n>>> 0) to enter the main menu add\n<< Write email: ").strip()
        if email_cont in [email.email for email in record.get_all_emails()]:
            print(f"\n>>> You have a email {email_cont} in other contact! <<<\n     >>>Choose another email <<<")
            continue
        if email_cont == "0":
            print(f">>> was added (name: {name.value}, phone: {phone_cont.value}, email: {None}) <<<")
            return '>>> You enter the main menu add <<<'
        new_value = re.findall(r"[a-zA-z]{1}[\w+\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", email_cont)
        if len(new_value) >= 1:
            email_cont = str(new_value[0])
            break
        print(">>> You write invalid email <<<")
    email_cont = EmailAddress(email_cont)
    rec = Record(name=name, phones=phone_cont, emails=email_cont)
    rec.save_email()
    return f"was added({rec})"


def add_phone():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu add\n<< Write contact name for add phone: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu add<<<'
        try:
            name = Name(name_cont)
            record = Record(name=name)
            if name_cont == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")

    while True:
        phone_cont = input("\n>>> 0) to enter the main menu add\n<< Write phone: ").strip()
        if phone_cont in [phone.phone for phone in record.get_all_phones()]:
            print(f"\n<<< You have a phone {phone_cont} in other contact! >>>\n     >>>Choose another phone <<<")
            continue
        if phone_cont == "0":
            return '\n>>> You enter the main menu add <<<'
        if len(phone_cont) == 10 and phone_cont.isnumeric():
            break
        print("<<< Phone must contains 10 symbols and only numbers>>>\n        <<<Write correct phone>>>")
    phone_cont = CellPhone(phone_cont)
    record = Record(name=name, phones=phone_cont)
    record.save_phone()
    return f">>>was added name: {name.value}, phone: {phone_cont.value} <<<"


def add_email():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu add\n<< Write contact name for add email: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu add<<<'
        try:
            name = Name(name_cont)
            record = Record(name)
            if name_cont == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")

    while True:
        email_cont = input("\n>>> 0) to enter the main menu add\n<< Write email: ").strip()
        if email_cont in [email.email for email in record.get_all_emails()]:
            print(f"\n>>> You have a email {email_cont} in other contact! <<<\n     >>>Choose another email <<<")
            continue
        if email_cont == "0":
            return '>>> You enter the main menu add <<<'
        new_value = re.findall(r"[a-zA-z]{1}[\w+\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", email_cont)
        if len(new_value) >= 1:
            email_cont = str(new_value[0])
            break
        print(">>> You write invalid email <<<\n     >>>Choose another name <<<")
    email_cont = EmailAddress(email_cont)
    rec = Record(name=name, emails=email_cont)
    rec.save_email()
    return f"\n>>>was added name: {name.value}, email: {email_cont.value}"


def exit_handler():
    raise SystemExit('>>> You enter the main menu <<<')


FUNC: Dict[str, Callable] = {
    "1": add_contact,
    '2': add_phone,
    '3': add_email,
    '0': exit_handler
}

HELP_DICT = {
    '1': 'add contact',
    '2': 'add phone by contact',
    '3': 'add email by contact',
}


def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n")
        i += 1
    return help_text + f"> 0) Exit to main menu"


def main_add():
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


