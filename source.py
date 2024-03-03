import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#WARNING DONT FORGET TO CREATE TXT LogandPass
def register():
    username = username_reg_entry.get()
    password = password_reg_entry.get()
    repeat_password = passwordrep_entry.get()
    if len(username) >= 8:
        if len(password) >= 8 and password == repeat_password:
            with open("LogandPass.txt", "a") as file:
                file.write(username + "\n")
                file.write(password + "\n")
            messagebox.showinfo("Регистрация", "Вы успешно зарегистрированы!")
            registration_button.config(state='disabled')
            password_reg_entry.delete(0, "end")
            username_reg_entry.delete(0, "end")
            passwordrep_entry.delete(0, "end")
        else:
            messagebox.showerror("Ошибка!", "Пароли не совпадают или содержат меньше 8 символов.")
    else:
        messagebox.showerror("Ошибка!", "Логин должен содержать как минимум 8 символов")

def login():
    username = username_login_entry.get()
    password = password_login_entry.get()

    with open("LogandPass.txt", "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), 2):
        if lines[i][:-1] == username and lines[i + 1][:-1] == password:
            messagebox.showinfo("Успешная авторизация", "Вы успешно вошли в систему!")
            login_button.config(state='disabled')
            return

    messagebox.showerror("Ошибка!", "Неправильный логин или пароль")

window = tk.Tk()
window.title('notebooks')
window.geometry("400x300")
notebook = ttk.Notebook(window, width=300, height=200)
tabel = ttk.Frame(notebook)
notebook.add(tabel, text='Регистрация')
notebook.place(x=5, y=5)

labreg = tk.Label(tabel, text='Имя пользователя').pack()
username_reg_entry = tk.Entry(tabel)
username_reg_entry.pack()

password_label = tk.Label(tabel, text="Пароль:").pack()
password_reg_entry = tk.Entry(tabel)
password_reg_entry.pack()
passwordrep_label = tk.Label(tabel, text="Повторите пароль:")
passwordrep_label.pack()
passwordrep_entry = tk.Entry(tabel)
passwordrep_entry.pack()
registration_button = tk.Button(tabel, text="Зарегистрироваться", command=register)
registration_button.pack()

tabel1 = ttk.Frame(notebook)
notebook.add(tabel1, text='Авторизация')
lab = tk.Label(tabel1, text="Авторизация")
lab.pack()
username_label = tk.Label(tabel1, text="Имя пользователя:")
username_label.pack()
username_login_entry = tk.Entry(tabel1)
username_login_entry.pack()

password_label = tk.Label(tabel1, text="Пароль:")
password_label.pack()
password_login_entry = tk.Entry(tabel1, show="*")
password_login_entry.pack()

login_button = tk.Button(tabel1, text="Войти", command=login)
login_button.pack()

window.mainloop()
