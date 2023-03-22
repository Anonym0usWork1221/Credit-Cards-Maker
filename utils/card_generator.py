"""
Git: https://github.com/Anonym0usWork1221/Credit-Cards-Maker

Warning: The Python tool for creating valid credit cards is intended for educational purposes only. Any use of
this tool for illegal or fraudulent activities is strictly prohibited and may result in severe legal consequences.
The tool generates credit card numbers that may be valid, but it is not intended to be used for making actual
purchases or transactions. The creator of this tool is not responsible for any illegal or unauthorized use of the
tool. Use at your own risk and discretion.
"""


from random import randint, choice
from datetime import datetime
from requests import get


class CardValidator:
    def __init__(self, card_number):
        self.card_number = str(card_number)
        self.len_card = len(str(card_number))
        self.luhn_valid = None
        self.card_info = {}
        self.jdata = {'AMEX': ['34', '37'], 'Discover': ['65', '6011'],
                      'MasterCard': ['51', '52', '53', '54', '55'], 'Visa': ['4']}
        self.type_card = 'Unknown'

    def luhn_validator(self):
        double = 0
        total = 0

        digits = str(self.card_number)

        for i in range(len(digits) - 1, -1, -1):
            for c in str((double + 1) * int(digits[i])):
                total += int(c)
            double = (double + 1) % 2

        self.luhn_valid = (total % 10) == 0
        return self.luhn_valid

    def card_type(self):
        # AMEX
        if self.len_card == 15 and self.card_number[:2] in self.jdata['AMEX']:
            self.type_card = 'AMEX'

        # MasterCard, Visa, and Discover
        elif self.len_card == 16:
            # MasterCard
            if self.card_number[:2] in self.jdata['MasterCard']:
                self.type_card = 'MasterCard'

            # Discover
            elif self.card_number[:2] in self.jdata['Discover'] or self.card_number[:4] in self.jdata['Discover']:
                self.type_card = 'Discover'

            # Visa
            elif self.card_number[:1] in self.jdata['Visa']:
                self.type_card = 'Visa'

        # VISA
        elif self.len_card == 13 and self.card_number[:1] in self.jdata['Visa']:
            self.type_card = 'Visa'

        return self.type_card

    def card_info_lookup(self):
        req = get(f"https://lookup.binlist.net/{self.card_number.replace(' ', '')[:6]}")
        if req.status_code == 200:
            j_req = req.json()
            try:
                self.card_info.update({"type": j_req['type']})
            except Exception as e:
                # print("[-] Error in info lookup: ", e)
                pass
            country = ''
            currency = ''
            short = ''
            try:
                country = j_req['country']['name']
            except:
                ...
            try:
                currency = j_req['country']['currency']
            except:
                ...
            try:
                short = j_req['country']['alpha2']
            except:
                ...

            self.card_info.update({
                "country": country,
                "currency": currency,
                "short": short,
            })
            if j_req['bank']:
                for ids in ['name', 'phone', 'url']:
                    try:
                        self.card_info.update({
                            f"bank_{ids}": j_req['bank'][ids],
                        })
                    except Exception as e:
                        # print("[-] Error in json data unpacking: ", e)
                        pass
        else:
            return None

        return self.card_info


class GetGenerate:
    def __init__(self, count=1, credit_type="Visa"):
        self.count = count
        self.credit_type = credit_type
        self.jdata = {"amex": ['34', '37'], "discover": ['65', '6011'],
                      "mastercard": ['51', '52', '53', '54', '55'], "visa": ['4']}
        self.info_card = {}
        self.ready_card = {}
        self.beautiful_card = None

    def card_info(self, card_list):
        for card_number in card_list:
            self.info_card.update({card_number: CardValidator(card_number).card_info_lookup()})

        return self.info_card

    def beautiful_card_gen(self, card_list):
        if type([]) == type(card_list):
            self.beautiful_card = []
            for card_ids in card_list:
                out = []
                template_base = ""
                card_ids = str(card_ids)
                while card_ids:
                    out.append(card_ids[-4:])
                    card_ids = card_ids[:-4]
                    template_base = ' '.join(out[::-1])
                self.beautiful_card.append(template_base)
        elif type({}) == type(card_list):
            self.beautiful_card = {}
            for idList in card_list:
                card_ids = card_list[idList]['card']
                out = []
                template_base = ""
                while card_ids:
                    out.append(card_ids[-4:])
                    card_ids = card_ids[:-4]
                    template_base = ' '.join(out[::-1])
                j_value = {idList: {"card": template_base,
                                    "date": card_list[idList]['date'],
                                    "csv": card_list[idList]['csv']}}
                self.beautiful_card.update(j_value)
        return self.beautiful_card

    def get_card(self, beautiful_card=None, bank_info=None):
        if self.credit_type.lower() == "visa":
            for x in range(self.count):
                card_id = choice(self.jdata['visa'])
                if randint(0, 1):
                    while 1:
                        card_number = f"{card_id}{randint(111111111111, 999999999999)}"
                        if CardValidator(card_number).luhn_validator():
                            data_value = int(datetime.now().strftime("%y")) + randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"0{randint(1, 10)}/{data_value}",
                                              "csv": randint(111, 999)}}
                            self.ready_card.update(json_value)
                            break
                else:
                    while 1:
                        card_number = f"{card_id}{randint(111111111111111, 999999999999999)}"
                        if CardValidator(card_number).luhn_validator():
                            data_value = int(datetime.now().strftime("%y")) + randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"0{randint(1, 10)}/{data_value}",
                                              "csv": randint(111, 999)}}
                            self.ready_card.update(json_value)
                            break

        else:
            for x in range(self.count):
                card_id = choice(self.jdata[self.credit_type.lower()])
                if self.credit_type.lower() == "amex":
                    card_id = choice(self.jdata['amex'])
                    while 1:
                        card_number = f"{card_id}{randint(1111111111111, 9999999999999)}"
                        if CardValidator(card_number).luhn_validator():
                            data_value = int(datetime.now().strftime("%y")) + randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"0{randint(1, 10)}/{data_value}",
                                              "csv": randint(111, 9999)}}
                            self.ready_card.update(json_value)
                            break
                else:
                    while 1:
                        card_number = f"{card_id}{randint(11111111111111, 99999999999999)}"
                        if CardValidator(card_number).luhn_validator():
                            data_value = int(datetime.now().strftime("%y")) + randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"0{randint(1, 10)}/{data_value}",
                                              "csv": randint(111, 999)}}
                            self.ready_card.update(json_value)
                            break

        if beautiful_card:
            self.ready_card = GetGenerate().beautiful_card(self.ready_card)
        if bank_info:
            json_info_bank = {}
            for card_id in self.ready_card:
                ready_info = CardValidator(self.ready_card[card_id]['card']).card_info_lookup()
                json_info_bank.update({card_id: {"value": self.ready_card[card_id], "info": ready_info}})
            self.ready_card = json_info_bank
        return self.ready_card
