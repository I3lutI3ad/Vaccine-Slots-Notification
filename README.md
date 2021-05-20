# Vaccine Slots Notofication

> Checks every 10 seconds for latest updates on available slots.

> Sends notification on telegram as soon as data is updated

## Install the requirements

`pip3 install -r requirements.txt`

## Telegram Setup

> Search IDBot (@myidbot) and Start a Chat

> Send `/getid` in chat to recieve your id

> Set this in `chat_id` in `slots.py` Line 9

> Search Vaccine Slots (@rvaccineslotsbot) and Start a Chat

> You're set up to recieve messages.

## Set District Id

> Search your state and district in `states.json`

> Set your district_id in `district_id` in `slots.py` Line 10

# Run

> Set `age_limit` and `dose_type` to required value

> run `python3 slots.py` and leave it running to receive notification when slot is available