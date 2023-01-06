from typing import Dict, Callable
from mongoengine_example.records import Record


def show_phones_by_name():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu show\n<< Write contact name: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu show<<<'
        try:
            record = Record(name=name_cont)
            if name_cont == record.find_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")
    phones = record.find_phone()
    return f"Contact: {record.name} phones: {', '.join([phone.phone for phone in phones])}"


def show_emails_by_name():
    while True:
        name_cont = input("\n>>> 0) to enter the main menu show\n<< Write contact name: ").strip()
        if name_cont == "0":
            return '\n>>> You enter the main menu show <<<'
        try:
            record = Record(name=name_cont)
            if name_cont == record.find_contact_by_name().name:
                break
        except AttributeError:
            print(f"\n>>> You dont have a contact {name_cont}! <<<\n     >>>Choose another name <<<")
    emails = record.find_email()
    return f"Contact: {record.name} emails: {', '.join([email.email for email in emails])}"


def show_all_contact():
    record = Record()
    contacts = record.find_contact()
    for con in contacts:
        print(con)
    return f"\n<<< That's all >>>"


def exit_handler():
    raise SystemExit('>>> You enter the main menu <<<')


FUNC: Dict[str, Callable] = {
    '1': show_phones_by_name,
    '2': show_emails_by_name,
    '3': show_all_contact,
    '0': exit_handler
}

HELP_DICT = {
    '1': 'show phones by name',
    '2': 'show emails by name',
    '3': 'show all contact'
}


def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n")
        i += 1
    return help_text + f"> 0) Exit to main menu"


def main_show():
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
