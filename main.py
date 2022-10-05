import requests as req
from pyrogram import *
from Config import *
import os

app=Client('exchange',
           api_id=API_ID,
           api_hash=API_HASH,
           bot_token=BOT_TOKEN)

url=base_url+base_currency



@app.on_message(filters.command('start'))
async def start_msg(client,message):
    await message.reply('Hey '+message.from_user.first_name+'🙋🏻‍♀️')
    await message.reply('I can fetch exchange rate of all countries')
    await message.reply('just enter a currency code\nExample:\n`inr`')
    await message.reply('Help menu : /help\nSource Code :/source')
@app.on_message(filters.command('help'))
async def start_msg(client,message):
    await message.reply('**Help Menu**\n\n - /status : for status of currency updation\n - /checkall : check all currency rate as bulk\n - /source : Get source code')
    
@app.on_message(filters.command('source'))
async def start_msg(client,message):
    await message.reply('Source Code : [Github Repo](https://github.com/riz4d)')

@app.on_message(filters.command('status'))
async def status_msg(client,message):
    url_req=req.get(url)
    exng_js=url_req.json()
    time_last_update_unix=str(exng_js['time_last_update_unix'])
    time_last_update_utc=str(exng_js['time_last_update_utc'])
    time_next_update_unix=str(exng_js['time_next_update_unix'])
    time_next_update_utc=str(exng_js['time_next_update_utc'])
    base_code=str(exng_js['base_code'])
    status='__LastUpdated UTC : '+time_last_update_utc+'\nLastUpdated Unix : '+time_last_update_unix+'\n\nNextUpdate UTC : '+time_next_update_utc+'\nNextUpdate Unix : '+time_next_update_unix+'\n\nBase Currency : '+base_code+'__'
    await message.reply(status)
    
    
@app.on_message(filters.command('checkall'))
async def check_all(client,message):
    url_req=req.get(url)
    exng_js=url_req.json()
    time_last_update_unix=str(exng_js['time_last_update_unix'])
    time_last_update_utc=str(exng_js['time_last_update_utc'])
    time_next_update_unix=str(exng_js['time_next_update_unix'])
    time_next_update_utc=str(exng_js['time_next_update_utc'])
    base_code=str(exng_js['base_code'])
    status='__LastUpdated UTC : '+time_last_update_utc+'\nLastUpdated Unix : '+time_last_update_unix+'\n\nNextUpdate UTC : '+time_next_update_utc+'\nNextUpdate Unix : '+time_next_update_unix+'\n\nBase Currency : '+base_code+'__'

    conversion_rates=str(exng_js['conversion_rates'])
    file = open('code.txt','w')
    file.write(conversion_rates)
    file.close()
    openfile=open('ne.txt', 'r')
    a=openfile.read()
    b=a.replace(',', '\n')
    c=b.replace('"', " ")
    d=c.replace('{', "Exchange Rates \n")
    e=d.replace('}', '')
    f=e.replace(':', ': ')
    await message.reply(status)
    await message.reply('**'+f+'**')
    os.remove('code.txt')
    
@app.on_message(filters.text)
async def exchange_msg(client,message):
   try: 
    url_req=req.get(url)
    exng_js=url_req.json()
    time_last_update_utc=str(exng_js['time_last_update_utc'])
    live_currency=str(message.text).upper()
    conversion_rate=str(exng_js['conversion_rates'][live_currency])
    exng_msg='__LastUpdated UTC : '+time_last_update_utc+'__\n\n**1 '+base_currency+'** = `'+conversion_rate+' '+live_currency+'`'
    await message.reply(exng_msg)
   except:
       await message.reply('invalid currency')
app.run()
