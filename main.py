from time import sleep
import requests

status = ""
progress = 0
order_number = ""
BOT_TOKEN = ""
ADMIN_CHAT_ID = ""
PERIOD = 3600


while True:
    data_from_embassy = requests.get(f"https://info.midpass.ru/api/request/{order_number}").json()
    name = data_from_embassy["internalStatus"]["name"]
    percents = data_from_embassy["internalStatus"]["percent"]

    if status != name or progress != percents:

        actual_message_for_telegram = f"""
Произошло изменение!
Новый статус: {name}
Прогресс: {percents}%
        """
        progress = percents
        status = name
    else:
        actual_message_for_telegram = "Пока ничего не изменилось"

    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/"
                  f"sendMessage?text={actual_message_for_telegram}&chat_id={ADMIN_CHAT_ID}")
    sleep(PERIOD)
