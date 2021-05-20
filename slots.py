import requests
import json
from fake_useragent import UserAgent
from datetime import datetime,timedelta
import time
import sys
import os

chat_id = "1850012850" # Your Chat ID
district_id = "150" #Your District ID
system_check_after = 360 # In Seconds (1 Hour)
age_limit = 18
dose_type = 1 # 1 or 2

def send_to_telegaram(message):
    requests.post("https://api.telegram.org/bot1801938689:AAENIGRQCBFrjlye-8qdJJMU9bkvmx5UFJE/sendMessage", json={"chat_id":chat_id,"text":message})

def get_vaccine_data(date):
    URL = "https://cdn-api.co-vin.in/api"

    temp_user_agent = UserAgent()
    headers = {'User-Agent': temp_user_agent.random, "Content-Type":"application/json", "Accept": "application/json"}

    get_7_session = f"/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date.strftime('%d-%m-%Y')}"
    sessions = json.loads(requests.get(f"{URL}{get_7_session}", headers=headers).text)

    centres = sessions["centers"]

    for centre in centres:
        for session in centre["sessions"]:
            if session['min_age_limit']<=age_limit and session[f'available_capacity_dose{dose_type}']>0:
                send_to_telegaram(f"NAME - {centre['name']}\nADDRESS - {centre['address']}\nDISTRICT - {centre['district_name']}\nFEE TYPE - {centre['fee_type']}\nDATE - {session['date']}\nDOSE {dose_type} - {session[f'available_capacity_dose{dose_type}']} LEFT\nAGE LIMIT - {session['min_age_limit']}")


count = 1
started = False
while True:
    try:
        today = datetime.now()
        if not started:
            send_to_telegaram(f"STARTED AT {today.strftime('%d-%m-%Y %H:%M')}")
            started = True
        get_vaccine_data(today)
        get_vaccine_data(today+timedelta(7))
        if count==system_check_after: # WILL SEND SYSTEM CHECK EVERY HOUR
            count=1
            send_to_telegaram(f"SYSTEM CHECK ON {today.strftime('%d-%m-%Y %H:%M')}")
        else:
            count+=1
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    time.sleep(10) # Checks API and Slots every 10 Seconds.