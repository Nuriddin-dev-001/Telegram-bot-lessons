import requests

token = "7926665974:AAGFadnhmF4QLRG2Y7xR85J07JLXYzdkIWw"
chat_id = 7192734058

response = requests.post(
    f'https://api.telegram.org/bot{token}/sendDocument',
    data={
        'chat_id': chat_id,
        'document': 'BQACAgIAAxkBAAMgaE1IqgABFi0Elzs_2Lu5an3Lj0OTAAJvZgACO43IS5nM3X163MNQNgQ'
    }
).json()

print(response)

