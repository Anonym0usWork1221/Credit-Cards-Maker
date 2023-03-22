"""
Git: https://github.com/Anonym0usWork1221/Credit-Cards-Maker

Warning: The Python tool for creating valid credit cards is intended for educational purposes only. Any use of
this tool for illegal or fraudulent activities is strictly prohibited and may result in severe legal consequences.
The tool generates credit card numbers that may be valid, but it is not intended to be used for making actual
purchases or transactions. The creator of this tool is not responsible for any illegal or unauthorized use of the
tool. Use at your own risk and discretion.
"""

from utils.card_generator import GetGenerate
from argparse import ArgumentParser


class CommandLine:
    _predefined_cards = ["AMEX", "Discover", "MasterCard", "Visa"]
    _predefined_line = '----------------------------------------------------------------------\n' * 2
    _predefined_file_start = '======================================================================\n' * 1
    _predefine_warning = 'Warning: The Python tool for creating valid credit cards is intended for educational\n' \
                         'purposes only. Any use of this tool for illegal or fraudulent activities is strictly\n' \
                         'prohibited and may result in severe legal consequences. The tool generates credit card\n' \
                         'numbers that may be valid, but it is not intended to be used for making actual purchases\n' \
                         'or transactions. The creator of this tool is not responsible for any illegal or\n' \
                         'unauthorized use of the tool. Use at your own risk and discretion\n\n'
    _predefined_details = '\nGit: https://github.com/Anonym0usWork1221/Credit-Cards-Maker\n'

    _args = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def arg_parser(self):
        parser = ArgumentParser(description='Command Line credit card generator by github.com/Anonym0usWork1221')
        parser.add_argument('-c', '--card_type', help=f'Select the card from available cards: '
                                                      f'{self._predefined_cards}', type=str)
        parser.add_argument('-l', '--limit_cards', help='Type number of card to generate e.g 5', type=int)
        parser.add_argument('-i', '--card_info', help='Fetch information of bank and related data',
                            default=False, action='store_true')
        parser.add_argument('-o', '--output_file', help='output file name to store card details', type=str,
                            default='./cards.txt')
        self._args = parser.parse_args()

    def check_args(self) -> tuple[str, int]:
        card_name = self._args.card_type
        limit_card = self._args.limit_cards
        if not card_name or not limit_card:
            print("[-] Type -h for help need card_name (-c) and limit_card (-l)")
            exit(0)

        is_valid_card = False
        for card in self._predefined_cards:
            if card_name.lower() == card.lower():
                card_name = card
                is_valid_card = True
                break

        if not is_valid_card:
            print("[-] Choose card from given cards (type -h for cards list)")
            exit(0)

        if int(limit_card) <= 0:
            print('[-] Card limit must be positive')
            exit(0)
        limit_card = int(limit_card)
        return card_name, limit_card

    def fetch_details(self):
        card_name, cards_limit = self.check_args()
        file_name = self._args.output_file
        card_info = self._args.card_info

        initialize_generator = GetGenerate(cards_limit, card_name)
        cards_data = initialize_generator.get_card(bank_info=card_info)

        unpacked_data = self._predefined_file_start + \
                        self._predefined_details + \
                        self._predefine_warning + \
                        self._predefined_file_start + "\n"

        if not cards_data:
            print('[-] Unable to generator cards')
            exit(0)

        if not card_info:
            for card_index in range(cards_limit):
                card_data = cards_data[card_index]
                for key, value in card_data.items():
                    unpacked_data += f'{key}: {value}\n'

                unpacked_data += "\n" + self._predefined_line + "\n"
        else:
            for card_index in range(cards_limit):
                card_data = cards_data[card_index]
                info = card_data["info"]
                value = card_data["value"]

                if value:
                    for key, v in value.items():
                        unpacked_data += f'{key}: {v}\n'
                else:
                    ...

                if info:
                    for key, v in info.items():
                        unpacked_data += f'{key}: {v}\n'
                else:
                    unpacked_data += 'info: unable to get info for this card\n'

                unpacked_data += "\n" + self._predefined_line + "\n"

        file_object = open(file=file_name, mode='w')
        file_object.write(unpacked_data)
        file_object.close()
        print(f'[+] File Created: {file_name}')


if __name__ == '__main__':
    App = CommandLine()
    App.arg_parser()
    App.fetch_details()

