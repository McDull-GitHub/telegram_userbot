from telethon.sync import TelegramClient
from telethon import functions, types
import tkinter as tk
api_id = 1054981
api_hash = '341e29114e1bb38d1fda9f1a22b59b28'


class UI:
    def __init__(self):
        root = tk.Tk()
        root.title("快速刪除Telegram訊息")
        root.geometry('432x243')
        root.resizable(width=0, height=0)
        root.wm_attributes('-topmost', 1)
        tk.Label(master=root, text='電話號碼').place(
            x=50, y=50, height=26, width=70)
        tk.Label(master=root, text='驗證碼').place(
            x=60, y=100, height=26, width=60)
        tk.Label(master=root, text='密碼').place(
            x=66, y=150, height=26, width=60)
        self.phone_number = tk.Entry(master=root)
        self.phone_number.place(x=144, y=50, height=26, width=220)
        self.password = tk.Entry(master=root, show='*')
        self.password.place(x=144, y=150, height=26, width=220)
        self.password = tk.Entry(master=root)
        self.password.place(x=144, y=100, height=26, width=100)
        self.get_code_button = tk.Button(master=root, text='驗證碼', width=50,
                                         height=30, command=self.get_code)
        self.get_code_button.place(x=304, y=100, height=26, width=60)
        self.help_button = tk.Button(master=root, text='說明', width=40,
                                     height=30, command=self.help)
        self.help_button.place(x=94, y=200, height=26, width=60)
        self.login_button = tk.Button(master=root, text='登入', width=40,
                                      height=30, command=self.login)
        self.login_button.place(x=194, y=200, height=26, width=60)
        self.exit_button = tk.Button(master=root, text='退出', width=40,
                                     height=30, command=self.exit)
        self.exit_button.place(x=294, y=200, height=26, width=60)
        self.root = root
        root.mainloop()

    def get_code(self):
        client = TelegramClient('token', api_id, api_hash)
        client.connect()
        print(self.phone_number.get())
        client.send_code_request(self.phone_number.get())

    def help(self):
        pass

    def login(self):
        pass

    def exit(self):
        self.root.quit()


if __name__ == "__main__":
    UI()
