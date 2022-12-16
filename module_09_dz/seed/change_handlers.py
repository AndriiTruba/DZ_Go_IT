import re
from typing import Dict, Callable
from database.repository import Record, CellPhone, EmailAddress, Name


def change_name():
    while True:
        old_name = input("\n>>> 0) to enter the main menu change\n<< Write contact name for a change: ").strip()
        if old_name == "0":
            return '\n>>> You enter the main menu change <<<'
        try:
            name_old = Name(old_name)
            record = Record(name=name_old)
            if old_name == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {old_name}! <<<\n     >>>Choose another name <<<")
    while True:
        new_name = input("\n>>> 0) to enter the main menu add\n<< Write new contact name: ").strip()
        if new_name == "0":
            return '\n>>> You enter the main menu add<<<'
        try:
            name = Name(new_name)
            record = Record(name=name)
            if new_name == record.get_contact_by_name().name:
                print(f"\n>>> You have a contact {new_name}! <<<\n     >>>Choose another name <<<")
        except AttributeError:
            break
    record.update_name(old_name)
    return f"Contact name: {name_old.value} new contact name: {new_name}"


def change_phone():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu change\n<< Write contact name for a change phone: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu change <<<'
        try:
            name_cont = Name(name_cont)
            record = Record(name=name_cont)
            if name_cont.value == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont.value}! <<<\n     >>>Choose another name <<<")
    contact = record.get_contact_by_name()
    phones = record.get_phones(contact)
    print(f"Contact: {contact.name} have this phone:")
    for phone in phones:
        print(f"id: {phone.id} phone: {phone.phone}")

    while True:
        id_phone = input("\n>>> 0) to enter the main menu change\n<< Enter the phone id you want to change: ").strip()
        if id_phone == "0":
            return '\n>>> You enter the main menu change <<<'
        if int(id_phone) in [phone.id for phone in phones]:
            break
        print(f">>> Contact: {contact.name} does not have a phone with id {id_phone} <<<")

    while True:
        new_phone = input("\n>>> 0) to enter the main menu change\n<< Write new phone: ").strip()
        if new_phone == "0":
            return '\n>>> You enter the main menu change <<<'
        if len(new_phone) == 10 and new_phone.isnumeric():
            break
        print("<<< Phone must contains 10 symbols and only numbers >>>\n        <<<Write correct new phone>>>")
    phone = CellPhone(new_phone)
    record = Record(phones=phone, name=name_cont)
    update = record.update_phone(id_phone)
    return f"Contact: {update.contact.name} now has a new phone: {update.phone}"


def change_email():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu change\n<< Write contact name for a change email: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu change <<<'
        try:
            name_cont = Name(name_cont)
            record = Record(name=name_cont)
            if name_cont.value == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont.value}! <<<\n     >>>Choose another name <<<")
    contact = record.get_contact_by_name()
    emails = record.get_emails(contact)
    print(f"Contact: {contact.name} have this emails:")
    for email in emails:
        print(f"id: {email.id} email: {email.email}")

    while True:
        id_email = input("\n>>> 0) to enter the main menu change\n<< Enter the email id you want to change: ").strip()
        if id_email == "0":
            return '\n>>> You enter the main menu change <<<'
        if int(id_email) in [email.id for email in emails]:
            break
        print(f">>> Contact: {contact.name} does not have a phone with this id <<<")

    while True:
        new_email = input("\n>>> 0) to enter the main menu change\n<< Write new email: ").strip()
        if new_email == "0":
            return '\n>>> You enter the main menu change <<<'
        new_value = re.findall(r"[a-zA-z]{1}[\w+\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", new_email)
        if len(new_value) >= 1:
            email = str(new_value[0])
            break
        print(">>> You write invalid email <<<\n     >>>Choose another name <<<")
    email = EmailAddress(email)
    record = Record(name=name_cont, emails=email)
    update = record.update_email(id_email)
    return f"Contact: {update.contact.name} now has a new email: {update.email}"


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