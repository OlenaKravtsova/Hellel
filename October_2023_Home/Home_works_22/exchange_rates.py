coding: 'utf-8'
import requests
from datetime import datetime

def get_exchange_rates():
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"������� ��������� �����. ��� �����: {response.status_code}")

def write_to_file(data, filename="exchange_rates.txt"):
    with open(filename, "w") as file:
        file.write(f"[���� ��������� ������] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for item in data:
            file.write(f"{item['txt']} to UAH: {item['rate']}\n")

def run():
    try:
        exchange_rates = get_exchange_rates()
        write_to_file(exchange_rates)
        print("����� ����� ������ �������� � ����.")
    except Exception as e:
        print(f"�� ������� �������� ����� �����. �������: {e}")

# ��������� ������� �������������, ���� ������ ��������
run()