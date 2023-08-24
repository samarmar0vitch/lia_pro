import requests
import json
chat_id = "-1001737322376"
api_key = "6545350878:AAEGRCv1uiDmh6dFO1oi21fipqH0Gy7TPw8"

def send_telegram_message(message: str,
                          chat_id: str,
                          api_key: str,
                          proxy_username: str = None,
                          proxy_password: str = None,
		  proxy_url: str = None):
    responses = {}
    print(proxy_url)

    proxies = None
    if proxy_url is  None:

        headers = {'Content-Type': 'application/json',
                   'Proxy-Authorization': 'Basic base64'}
        data_dict = {'chat_id': chat_id,
                     'text': message,
                     'parse_mode': 'HTML',
                     'disable_notification': True}
        data = json.dumps(data_dict)
        url = f'https://api.telegram.org/bot{api_key}/sendMessage'
        print(url)
        response = requests.post(url,
                                 data=data,
                                 headers=headers,
                                 #proxies=proxies,
                                 verify=False)
        print(response)
        return response

print(send_telegram_message("Hello world!!! i am LIVE now On Tiktok : https://www.tiktok.com/@liaeljoni1/live", chat_id, api_key,None,None,None))
