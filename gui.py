from telethon.sync import TelegramClient
from telethon import functions, types
import tkinter.messagebox
import tkinter as tk

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
            self.logged_in_windows.title(
                "快速刪除Telegram訊息({}已登入)".format(self.client.get_me().first_name))
            self.logged_in_windows.geometry('432x243')
            self.logged_in_windows.resizable(width=0, height=0)
            self.logged_in_windows.wm_attributes('-topmost', 1)
            self.chat_room = tk.Entry(self.logged_in_windows)
            self.chat_room.pack()
            tk.Label(self.logged_in_windows, text='\n使用說明\n\n在上方輸入頻道、群組的share link或者私訊對方的username\n格式可以是 https://t.me/TGQNA @TGQNA 或者 TGQNA\n\n在下方選譯是僅刪除自己傳送的訊息還是刪除所有的訊息\n注意：刪除所有訊息時請確保你有對應的權限\n').pack()
            self.del_button = tk.Button(
                self.logged_in_windows, text='刪除自己的訊息', command=self.del_msg)
            self.del_button.pack()
            self.del_all_button = tk.Button(
                self.logged_in_windows, text='刪除全部的訊息', command=self.delall_msg)
            self.del_all_button.pack()
            self.logged_in_windows.mainloop()
        else:
            self.log_in_windows = tk.Tk()
            self.log_in_windows.title("快速刪除Telegram訊息（未登入）")
            self.log_in_windows.geometry('432x243')
            self.log_in_windows.resizable(width=0, height=0)
            self.log_in_windows.wm_attributes('-topmost', 1)
            tk.Label(master=self.log_in_windows, text='國碼＋電話號碼').place(
                x=20, y=50, height=26, width=100)
            tk.Label(master=self.log_in_windows, text='驗證碼').place(
                x=66, y=100, height=26, width=60)
            tk.Label(master=self.log_in_windows, text='密碼').place(
                x=72, y=150, height=26, width=60)
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
                                         height=30, command=self.exit)
            self.exit_button.place(x=294, y=200, height=26, width=60)
            self.log_in_windows.mainloop()

    def exit(self):
        self.log_in_windows.quit()

    def get_code(self):
        if len(self.phone_number.get()) <= 8:
            tk.messagebox.showerror(
                '錯誤', '請先輸入正確的電話號碼\n格式：國際電話區號＋電話號碼\n例如：+85223802850')
            return
        try:
            self.sent = self.client.send_code_request(self.phone_number.get())
            self.hash = self.sent.phone_code_hash
        except:
            tk.messagebox.showerror('未知錯誤', '無法取得驗證碼，請兩分鐘後再試！')

    def help(self):
        tk.messagebox.showinfo(
            '使用說明', '電話號碼格式國際電話區號＋電話號碼\n例如：+85223802850\n\n驗證碼是5位數字的\n密碼是雙步驟驗證（2FA）密碼，沒有就留空')

    def del_msg(self):
        self.me = self.client.get_me()
        for self.message in self.client.iter_messages(self.chat_room.get()):
            if self.message.from_id == self.me.id:
                self.client.delete_messages(
                    self.chat_room.get(), self.message.id)
                print(self.message.id)
        tk.messagebox.showinfo(
            '成功', '成功刪除 {} 裡自己傳送的訊息'.format(self.chat_room.get()))

    def delall_msg(self):
        for self.message in self.client.iter_messages(self.chat_room.get()):
            self.client.delete_messages(self.chat_room.get(), self.message.id)
            print(self.message.id)
        tk.messagebox.showinfo(
            '成功', '成功刪除 {} 裡所有的訊息'.format(self.chat_room.get()))

    def login(self):
        if len(self.code.get()) != 5:
            tk.messagebox.showerror('錯誤', '請先輸入正確的驗證碼')
            return
        try:
            self.client.sign_in(
                phone=self.phone_number.get(),
                code=self.code.get(),
                password=self.password.get(),
                phone_code_hash=self.hash)
        except:
            tk.messagebox.showerror('未知錯誤', '無法登入!')
            return
        tk.messagebox.showinfo('登入成功', '請重新啟動這個應用程式！')
        self.log_in_windows.quit()


if __name__ == "__main__":
    UI()
