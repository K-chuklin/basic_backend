from functions import get_data, get_filtered_data, get_sorted_data, get_formatted, hide_card_info


def main():
    data = get_data()
    data = get_filtered_data(data)
    data = get_sorted_data(data)
    for trans_inf in data:
        print(get_formatted(trans_inf['date']), end=' ')
        print(trans_inf['description'])
        if 'from' in trans_inf:
            print(hide_card_info(trans_inf['from']), '->', hide_card_info(trans_inf['to']))
        else:
            print(hide_card_info(trans_inf['to']))
        print(trans_inf['operationAmount']['amount'], trans_inf['operationAmount']['currency']['name'])


if __name__ == '__main__':
    main()

