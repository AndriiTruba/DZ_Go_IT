from typing import Dict, Callable
from mongoengine_example.records import Record


def remove_contact():
    while True:
        name_input = input("\n>>> 0) to enter the main menu remove.\n<< Write contact name for a remove: ").strip()
        if name_input == "0":
            return '\n>>> You enter the main menu remove <<<'
        try:
            record = Record(name=name_input)
            if name_input == record.find_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_input}! <<<\n     >>>Choose another name <<<")
    record.remove_contact()
    return f"<<< Contact is remove >>>"


def remove_phone():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu remove.\n<< Write contact name for a remove phone: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu remove <<<'
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
    record = Record(name=name_cont, phone=old_phone)
    record.remove_phone()
    return f"<<< Phone is remove >>>"


def remove_email():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu remove\n<< Write contact name for a remove email: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu remove<<<'
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
    record = Record(name=name_cont, email=old_email)
    record.remove_email()
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


