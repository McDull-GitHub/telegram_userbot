from telethon.sync import TelegramClient
from telethon import functions, types
import tkinter.messagebox
import tkinter as tk
import re

api_id = 1054981
api_hash = '341e29114e1bb38d1fda9f1a22b59b28'


class UI:
    def __init__(self):
        self.client = TelegramClient('token', api_id, api_hash)
        try:
            self.client.connect()
        except OSError:
            tk.messagebox.showerror('錯誤', '無法連線伺服器\n請檢查你的網路')

        if self.client.is_user_authorized():
            self.logged_in_windows = tk.Tk()
            self.logged_in_windows.title("快速刪除Telegram訊息")
            self.logged_in_windows.geometry('432x243')
            self.logged_in_windows.resizable(width=0, height=0)
            self.logged_in_windows.wm_attributes('-topmost', 1)
            """
            self.help_button = tk.Button(master=self.logged_in_windows, text='說明', width=40,
                                         height=30, command=self.help)
            self.help_button.place(x=94, y=200, height=26, width=60)
            self.login_button = tk.Button(master=self.logged_in_windows, text='登入', width=40,
                                          height=30, command=self.login)
            self.login_button.place(x=194, y=200, height=26, width=60)
            self.exit_button = tk.Button(master=self.logged_in_windows, text='退出', width=40,
                                         height=30, command=self.exit)
            self.exit_button.place(x=294, y=200, height=26, width=60)
            """
            self.logged_in_windows.mainloop()
        else:
            self.log_in_windows = tk.Tk()
            self.log_in_windows.title("快速刪除Telegram訊息")
            self.log_in_windows.geometry('432x243')
            self.log_in_windows.resizable(width=0, height=0)
            self.log_in_windows.wm_attributes('-topmost', 1)
            tk.Label(master=self.log_in_windows, text='電話號碼').place(
                x=50, y=50, height=26, width=70)
            tk.Label(master=self.log_in_windows, text='驗證碼').place(
                x=60, y=100, height=26, width=60)
            tk.Label(master=self.log_in_windows, text='密碼').place(
                x=66, y=150, height=26, width=60)
            self.phone_number = tk.Entry(master=self.log_in_windows)
            self.phone_number.place(x=144, y=50, height=26, width=220)
            self.code = tk.Entry(master=self.log_in_windows)
            self.code.place(x=144, y=100, height=26, width=100)
            self.password = tk.Entry(master=self.log_in_windows, show='*')
            self.password.place(x=144, y=150, height=26, width=220)
            self.get_code_button = tk.Button(master=self.log_in_windows, text='驗證碼', width=50,
                                             height=30, command=self.get_code)
            self.get_code_button.place(x=304, y=100, height=26, width=60)
            self.help_button = tk.Button(master=self.log_in_windows, text='說明', width=40,
                                         height=30, command=self.help)
            self.help_button.place(x=94, y=200, height=26, width=60)
            self.login_button = tk.Button(master=self.log_in_windows, text='登入', width=40,
                                          height=30, command=self.login)
            self.login_button.place(x=194, y=200, height=26, width=60)
            self.exit_button = tk.Button(master=self.log_in_windows, text='退出', width=40,
                                         height=30, command=lambda:self.close_window(self.log_in_windows))
            self.exit_button.place(x=294, y=200, height=26, width=60)
            self.log_in_windows.mainloop()
 
    def get_code(self):
        if len(self.phone_number.get()) <= 10:
            tk.messagebox.showerror(
                '錯誤', '請先輸入正確的電話號碼\n格式：國際電話區號＋電話號碼\n例如：+85223802850')
            return
        try:
            self.sent = self.client.send_code_request(self.phone_number.get())
            self.hash = self.sent.phone_code_hash
        except:
            tk.messagebox.showerror('未知錯誤', '無法取得驗證碼！')

    def help(self):
        pass

    def login(self):
        if len(self.code.get()) != 5:
            tk.messagebox.showerror('錯誤', '請先輸入正確的驗證碼')
            return
        self.client.sign_in(
            phone=self.phone_number.get(),
            code=self.code.get(),
            password=self.password.get(),
            phone_code_hash=self.hash)

    def close_window(self,window):
        window.quit()

if __name__ == "__main__":
    UI()
