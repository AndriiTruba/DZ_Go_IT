from typing import Dict, Callable
from database.repository import Record, Name


def remove_contact():
    while True:
        name_input = input("\n>>> 0) to enter the main menu remove.\n<< Write contact name for a remove: ").strip()
        if name_input == "0":
            return '\n>>> You enter the main menu remove <<<'
        try:
            name = Name(name_input)
            record = Record(name=name)
            if name_input == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_input}! <<<\n     >>>Choose another name <<<")
    contact = record.get_contact_by_name()
    phones = record.get_phones(contact)
    for phone in phones:
        record.remove_phone(phone.id, contact)
    emails = record.get_emails(contact)
    for email in emails:
        record.remove_email(email.id, contact)
    record.remove_contact(contact.id)
    return f"<<< Contact is remove >>>"


def remove_phone():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu remove.\n<< Write contact name for a remove phone: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu remove <<<'
        try:
            name = Name(name_cont)
            record = Record(name=name)
            if name_cont == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")
    contact = record.get_contact_by_name()
    phones = record.get_phones(contact)
    print(f"Contact: {contact.name} have this phone:")
    for phone in phones:
        print(f"id: {phone.id} phone: {phone.phone}")

    while True:
        id_phone = input("\n>>> 0) to enter the main menu remove\n<< Enter the phone id you want to remove: ").strip()
        if id_phone == "0":
            return '\n>>> You enter the main menu <<<'
        if int(id_phone) in [phone.id for phone in phones]:
            break
        print(f">>> Contact: {contact.name} does not have a phone with id {id_phone} <<<")

    record.remove_phone(id_phone, contact)
    return f"<<< Phone is remove >>>"


def remove_email():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu remove\n<< Write contact name for a remove email: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu remove<<<'
        try:
            name_cont = Name(name_cont)
            record = Record(name=name_cont)
            if name_cont == record.get_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")
    contact = record.get_contact_by_name()
    emails = record.get_emails(contact)
    print(f"Contact: {contact.name} have this emails:")
    for email in emails:
        print(f"id: {email.id} email: {email.email}")

    while True:
        id_email = input("\n>>> 0) to enter the main menu remove\n<< Enter the email id you want to change: ").strip()
        if id_email == "0":
            return '\n>>> You enter the main menu remove <<<'
        if int(id_email) in [email.id for email in emails]:
            break
        print(f">>> Contact: {contact.name} does not have a phone with id {id_email}<<<")
    record.remove_email(id_email, contact)
    return f"<<< Email is remove >>>"


def exit_handler():
    raise SystemExit('\n>>> You enter the main menu remove <<<')


FUNC: Dict[str, Callable] = {
    '1': remove_phone,
    '2': remove_email,
    '3': remove_contact,
    '0': exit_handler
}

HELP_DICT = {
    '1': 'remove phone',
    '2': 'remove email',
    '3': 'remove contact'
}


def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n")
        i += 1
    return help_text + f"> 0) Exit to main menu"


def main_remove():
    while True:
        print(menu_help())
        user_input = input('\n<< Enter the command: ').strip()
        try:
            command_func = FUNC.get(user_input, None)
            command_func = command_func()
            if command_func:
                print(command_func)
            else:
                return '\n >>> Unknown command <<<'
        except TypeError:
            print('Unknown command or parametrs, please try again.')
        except SystemExit as e:
            return e


