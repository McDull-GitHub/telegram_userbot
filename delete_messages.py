from telethon import TelegramClient
import os


def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print('出現錯誤了！！！', e)


async def delete(chat):
    me = await client.get_me()
    async for message in client.iter_messages(chat):
        if message.from_id == me.id:
            print('刪除id為 {} 的訊息\n內容是 {}\n\n'.format(message.id, message.text))
            await client.delete_messages(chat, message.id)
    print('刪完了@{}的內容\n\n\n'.format(chat))

if __name__ == "__main__":
    try:
        from login import ID, HASH
        api_id = ID
        api_hash = HASH
    except ImportError as e:
        print('API ID 和 API HASH 要去 my.telegram.org 查看！！！\n電話號碼前面要輸入國碼：比如香港要加入+852')
        api_id = get_env('TG_API_ID', 'Please enter your API ID: ', int)
        api_hash = get_env('TG_API_HASH', 'Please enter your API hash: ')
        f = open('login.py', 'a')
        f.write("ID = {}\nHASH = '{}'".format(api_id, api_hash))
        f.close()
    client = TelegramClient('token', api_id, api_hash)
    while True:
        with client:
            chat = input('請輸入要刪除的群組，頻道，私訊的username：')
            client.loop.run_until_complete(delete(chat))
