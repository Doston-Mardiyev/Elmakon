import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import get_data
import os
import asyncio

bot = Bot(token='5092894332:AAHtLELna7n71rt13xLM8Zqcy4Z_DeTmo3g', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Phone', 'Laptop', 'Devices']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer('Choose products', reply_markup=keyboard)
    

@dp.message_handler(Text(equals='Phone'))
async def get_discount_knives(message: types.Message):
    await message.answer('Please waiting...')
    
    # get_data(file_path)
    
    with open('result.json') as file:
        data = json.load(file)
        
    for index, item in enumerate(data):

        if index%20 == 0:
            asyncio.sleep(3)

        # card = f'{hbold(item.get("article_title"))}\n' \
        #        f'{hbold("INFO: ")}{item.get("article_selling_info")}%\n' \
        #        f'{hbold("Confugration: ")}${item.get("prodact_info")}🔥'
            #    f'{hbold("Photo: ")}${item.get("prodact_image")}'
        # bot.send_photo(chat_id, photo=f'{item.get("prodact_image")}')
        await message.answer_photo(photo=f'{item.get("prodact_image")}', caption=f'{item.get("article_title")} \n {item.get("prodact_info")}')

    
    
       
            
        # await message.answer(card)
        
        
@dp.message_handler(Text(equals='🔫 Снайперские винтовки'))
async def get_discount_guns(message: types.Message):
    await message.answer('Please waiting...')
    
    # collect_data(cat_type=4)
    
    with open('result.json') as file:
        data = json.load(file)
        
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}🔥'
    
    
        if index%20 == 0:
            asyncio.sleep(3)
            
        await message.answer(card)

    
def main():
    executor.start_polling(dp)
    
    
if __name__ == '__main__':
    main()
    