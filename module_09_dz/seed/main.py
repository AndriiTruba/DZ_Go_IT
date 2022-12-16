from seed.add_handlers import main_add
from typing import Dict, Callable
from seed.change_handlers import main_change
from seed.show_handlers import main_show
from seed.remove_handlers import main_remove


def exit_handler():
    raise SystemExit('Good bye!')


FUNC: Dict[str, Callable] = {
    "1": main_add,
    '2': main_change,
    '3': main_show,
    '4': main_remove,
    '0': exit_handler
}

HELP_DICT = {
    '1': 'add menu',
    '2': 'change menu',
    '3': 'show menu',
    '4': 'remove menu',
}


def menu_help():
    help_text = "\nList of commands:\n"
    i = 1
    for help_com in HELP_DICT.values():
        help_text += "".join(f"> {i}) {help_com}" + "\n")
        i += 1
    return help_text + f"> 0) exit the console bot"


def main():
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
            print(e)
            break


if __name__ == '__main__':
    main()


