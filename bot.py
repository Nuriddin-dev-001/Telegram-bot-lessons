import requests

token = "********************************************"
chat_id = **********

response = requests.post(
    f'https://api.telegram.org/bot{token}/sendDocument',
    data={
        'chat_id': chat_id,
        'document': 'BQACAgIAAxkBAAMgaE1IqgABFi0Elzs_2Lu5an3Lj0OTAAJvZgACO43IS5nM3X163MNQNgQ'
    }
).json()

print(response)

