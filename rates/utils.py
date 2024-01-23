import json


def write_rates_data(time_now, rub_rate):
    data = {"date": str(time_now)[:19], "rate": float(rub_rate)}
    with open('rates_data.json', 'a', encoding='utf-8') as data_file:
        json.dump([data], data_file)
        data_file.write('\n')


def get_rates_data():
    rates_data = []
    with open('rates_data.json', 'r', encoding='utf-8') as data_file:
        for line in data_file:
            rates_data.append(line)
    rates_data = [json.loads(line)[0] for line in rates_data]
    return rates_data
