import requests
import time
from telegram import Bot

# 텔레그램 봇 정보
TOKEN = '7415984689:AAFML5XfYwIAnqxp2isjiIhodTZh5xPrExg'
CHAT_ID = '7945409294'
bot = Bot(token=TOKEN)

def get_sol_price():
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT'
    response = requests.get(url)
    return float(response.json()['price'])

def wait_for_range(min_price=105.0, max_price=106.0):
    print(f"목표 범위: ${min_price} ~ ${max_price}")
    while True:
        try:
            price = get_sol_price()
            print(f"현재 SOL 가격: ${price}")
            if min_price <= price <= max_price:
                bot.send_message(chat_id=CHAT_ID, text=f"[SOL] 현재가 ${price:.2f}, 진입 구간 도달!")
                break
            time.sleep(5)
        except Exception as e:
            print(f"에러 발생: {e}")
            time.sleep(10)

wait_for_range()
