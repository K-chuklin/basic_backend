import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        return data


def get_filtered_data(data):
    new_data = []
    for transaction in data:
        if 'state' in transaction and transaction['state'] == 'EXECUTED':
            new_data.append(transaction)
    return data


def get_sorted_data(data):
    if 'date' in data:
        data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def get_formatted(data):
    date_transaction = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    date_transaction = date_transaction.strftime("%d.%m.%Y")
    return date_transaction


def hide_card_info(card_data):
    card_num = card_data.split()[-1]
    card_name = ' '.join(card_data.split()[:-1])
    if len(card_data) != 0:
        if len(card_num) == 16 and card_num.isdigit():
            card_num = card_num[:4] + ' ' + card_num[4:6] + '** **** ' + card_num[-4:]
        elif len(card_num) == 20 and card_num.isdigit():
            card_num = '**' + card_num[-4:]
        else:
            return 'data error'

    return f'{card_name} {card_num}'


def hide_card_check(card_data: str):
    if card_data.startswith('Счет'):
        return 'Счет ****' + card_data[-4:0]

