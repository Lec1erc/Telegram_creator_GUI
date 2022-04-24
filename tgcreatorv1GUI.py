# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:59:36 2022

@author: ghulam muhammad
"""
import tgcreatorv1
import tkinter as tk
from tkinter import messagebox, Tk, Button, Frame
from PIL import ImageTk, Image
from configparser import ConfigParser
import sys
import webbrowser
import os
from tkinter.scrolledtext import ScrolledText
import socket


class PrintLogger(object):  # create file like object

    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.configure(state="normal")  # make field editable
        self.textbox.insert("end", text)  # write text to textbox
        self.textbox.see("end")  # scroll to end
        self.textbox.configure(state="disabled")  # make field readonly

    def flush(self):  # needed for file like object
        pass


try:
    config = ConfigParser()
    config.read('config_GUI.ini')

    # SIM API URL
    c_api_url = config.get('sim_api_url', 'api_url')

    # SIM API
    c_country = config.get('sim_api', 'country')
    c_operator = config.get('sim_api', 'operator')
    c_product = config.get('sim_api', 'product')
    c_token = config.get('sim_api', 'active_ru_key')

    # Telegram
    c_api_id = config.get('telegram', 'api_id')
    c_ap_hash = config.get('telegram', 'api_hash')

    # Multithreading
    c_thr_number = config.get('threads', 'thr_number')
    c_create_account_count = config.get('threads', 'create_account_count')

    # Photo generator
    c_is_generator_photo = config.get('photos', 'is_generator_photo')
except:
    None
if __name__ == "__main__":
    win = tk.Tk()

    win.title("TG ACCOUNT CREATOR V2--ANOOPKUMARPATEL.COM")
    win.geometry("1350x630+0+50")
    win.config(bg="#fff")
    win.resizable(False, False)

    api_key_var = tk.StringVar()
    api_id_var = tk.StringVar()
    api_hash_var = tk.StringVar()
    country_var = tk.StringVar()
    operator_var = tk.StringVar()
    thread_var = tk.StringVar()
    hangproof_var = tk.StringVar()
    random_avatar_var = tk.StringVar()
    total_acc_var = tk.StringVar()
    frame1_radio_var = tk.IntVar()
    frame1_2p_var = tk.IntVar()
    checkbutton_info = tk.IntVar()

    image = Image.open("Your_img.png")
    new_img = image.resize((880, 475))
    new_img.save("resized_img.png")

    img = ImageTk.PhotoImage(file="resized_img.png")
    lbl = tk.Label(win, image=img)
    lbl.place(x=0, y=100)

    title_label = tk.Label(win, text="TELEGRAM ACCOUNT CREATOR BULK", font=("Times new roman", 28), bg="lightgrey",
                           fg="black")
    title_label.place(x=0, y=0, relwidth=1)

    api_lable = tk.Label(win, text="API KEY", font=("Times new roman", 20), bg="white", fg="black")
    api_lable.place(x=50, y=100)
    api_entry_lable = tk.Entry(win, width=22, font=("Times new roman", 20), bg="#FFD94C", fg="black",
                               textvariable=api_key_var)
    api_entry_lable.place(x=200, y=100)
    api_entry_lable.insert(0, c_token)


    api_id_lable = tk.Label(win, text="API ID", font=("Times new roman", 20), bg="white", fg="black")
    api_id_lable.place(x=50, y=150)
    api_id_entry_lable = tk.Entry(win, width=15, font=("Times new roman", 20), bg="#FFD94C", textvariable=api_id_var)
    api_id_entry_lable.place(x=200, y=150)
    api_id_entry_lable.insert(0, c_api_id)

    api_hash_lable = tk.Label(win, text="API HASH", font=("Times new roman", 20), bg="white", fg="black")
    api_hash_lable.place(x=50, y=200)
    api_hash_entry_lable = tk.Entry(win, width=15, font=("Times new roman", 20), bg="#FFD94C", textvariable=api_hash_var)
    api_hash_entry_lable.place(x=200, y=200)
    api_hash_entry_lable.insert(0, c_ap_hash)

    country_lable = tk.Label(win, text="Country", font=("Times new roman", 20), bg="white", fg="black")
    country_lable.place(x=50, y=250)
    country_entry_lable = tk.Entry(win, width=15, font=("Times new roman", 20), bg="#FFD94C", textvariable=country_var)
    country_entry_lable.place(x=200, y=250)
    country_entry_lable.insert(0, c_country)

    operator_lable = tk.Label(win, text="Operator", font=("Times new roman", 20), bg="white", fg="black")
    operator_lable.place(x=50, y=300)
    operator_entry_lable = tk.Entry(win, width=15, font=("Times new roman", 20), bg="#FFD94C", textvariable=operator_var)
    operator_entry_lable.place(x=200, y=300)
    operator_entry_lable.insert(0, c_operator)

    frame1 = tk.Frame(win, bg="white", bd=5, relief="groove")
    frame1.place(x=50, y=350, height=130, width=500)
    frame2 = tk.Frame(win, bg="white", bd=5, relief="groove")
    frame2.place(x=50, y=485, height=70, width=500)

    website_checkbox = {"getsmscode.com": 1, "onlinesim.ru": 2, "simsims.org": 3, "sms-activate.org": 4, "smspva.com": 5,
                        "sms-reg.ru": 6}
    getsmscode = tk.Radiobutton(frame1, text="getsmscode.com", font=("Times new roman", 12), variable=frame1_radio_var,
                                value=1, bg="white", fg="black")
    getsmscode.place(x=10, y=10)
    onlinesim = tk.Radiobutton(frame1, text="onlinesim.ru", font=("Times new roman", 12), variable=frame1_radio_var,
                               value=2, bg="white", fg="black")
    onlinesim.place(x=10, y=50)
    simsims = tk.Radiobutton(frame1, text="simsims.org", font=("Times new roman", 12), variable=frame1_radio_var,
                             bg="white", value=3, fg="black")
    simsims.place(x=10, y=90)
    sms_activate = tk.Radiobutton(frame1, text="sms-activate.org", font=("Times new roman", 12), variable=frame1_radio_var,
                                  value=4, bg="white", fg="black")
    sms_activate.place(x=250, y=10)
    smspva = tk.Radiobutton(frame1, text="smspva.com", font=("Times new roman", 12), variable=frame1_radio_var, bg="white",
                            value=5, fg="black")
    smspva.place(x=250, y=50)
    sms_reg = tk.Radiobutton(frame1, text="sms-reg.ru", font=("Times new roman", 12), variable=frame1_radio_var, bg="white",
                             value=6, fg="black")
    sms_reg.place(x=250, y=90)
    frame1_radio_var.set(website_checkbox[c_api_url])

    checkbutton_lable = tk.Checkbutton(frame1, text="2p.", onvalue=1, offvalue=0, variable=checkbutton_info,
                                       font=("Times new roman", 12), fg="black", bg="white")
    checkbutton_lable.place(x=100, y=50)

    total_acc_lable = tk.Label(frame2, text="Total Accounts:", font=("Times new roman", 14), bg="white", fg="black")
    total_acc_lable.place(x=10, y=20)
    total_acc_entry_lable = tk.Entry(frame2, width=25, font=("Times new roman", 16), bg="#FFD94C",
                                     textvariable=total_acc_var)
    total_acc_entry_lable.place(x=150, y=20)
    total_acc_entry_lable.insert(0, c_create_account_count)

    thread_lable = tk.Label(win, text="Threads:", font=("Times new roman", 14, "bold"), bg="white", fg="black")
    thread_lable.place(x=600, y=170)
    thread_entry_lable = tk.Entry(win, width=5, font=("Times new roman", 16), bg="#FFD94C", textvariable=thread_var)
    thread_entry_lable.place(x=700, y=170, height=30)
    thread_entry_lable.insert(0, c_thr_number)

    frame3 = tk.Frame(win, bg="white", bd=5, relief="groove")
    frame3.place(x=600, y=220, height=50, width=250)

    users_ip = socket.gethostbyname(socket.gethostname())
    ip_lable = tk.Label(frame3, text="IP:", font=("Times new roman", 14, "bold"), bg="white", fg="black")
    ip_lable.place(x=10, y=5)
    ip_num_lable = tk.Label(frame3, text=users_ip, font=("Times new roman", 14), bg="white", fg="black")
    ip_num_lable.place(x=50, y=5)


    def load_config():
        update_config()
        with open("config_GUI.ini") as conf:
            print(conf.read())


    exe_button = tk.Button(win, text="LOAD CONFIG", font=("Times new roman", 16), fg="black", bg="white", cursor="hand2",
                           bd=5, relief="groove", command=load_config)
    exe_button.place(x=600, y=275, height=50, width=250)
    hang_lable = tk.Checkbutton(win, text="Hang Proof", onvalue=1, offvalue=0, font=("Times new roman", 12), fg="black",
                                bg="white", variable=hangproof_var)
    hang_lable.place(x=595, y=330)


    def avatar():
        path = os.getcwd()
        webbrowser.open(f"{path}/images")


    avatar_button = tk.Button(win, text="AVATARS", font=("Times new roman", 16), fg="black", bg="white", cursor="hand2",
                              bd=5, relief="groove", command=avatar)
    avatar_button.place(x=600, y=370, height=50, width=250)
    random_lable = tk.Checkbutton(win, text="Set Random Avatar(.jpg)", onvalue=True, offvalue=False,
                                  font=("Times new roman", 12), fg="black", bg="white", variable=random_avatar_var)
    random_lable.place(x=595, y=430)
    if c_is_generator_photo == "1":
        random_lable.select()
    else:
        random_lable.deselect()


    def accounts():
        path = os.getcwd()
        webbrowser.open(f"{path}/sessions")


    acc_button = tk.Button(win, text="ACCOUNTS", font=("Times new roman", 16), fg="black", bg="white", cursor="hand2", bd=5,
                           relief="groove", command=accounts)
    acc_button.place(x=600, y=470, height=50, width=250)

    last_lable = tk.Label(win, text="We recommend you to use IP changer during line grabbing!",
                          font=("Times new roman", 12), bg="white", fg="black")
    last_lable.place(x=50, y=560)

    call_log_lable = tk.Label(win, text="Call Logs:", font=("Times new roman", 14, "bold"), bg="white", fg="black")
    call_log_lable.place(x=885, y=90)
    T = ScrolledText(win, height=25, width=54, bd=5, relief="groove")
    T.place(x=885, y=120)
    logger = PrintLogger(T)
    sys.stdout = logger
    sys.stderr = logger


    def update_config():
        try:
            config = ConfigParser()
            config.read('config_GUI.ini')

            config.set('telegram', 'api_id', api_id_var.get())
            config.set('telegram', 'api_hash', api_hash_var.get())

            config.set('threads', 'thr_number', thread_var.get())
            config.set('threads', 'create_account_count', total_acc_var.get())

            config.set('sim_api', 'country', country_var.get())
            config.set('sim_api', 'operator', operator_var.get())
            config.set('sim_api', 'active_ru_key', api_key_var.get())
            config.set('photos', 'is_generator_photo', random_avatar_var.get())


        except Exception as e:
            print(e)

        with open('config_GUI.ini', 'w') as configfile:
            config.write(configfile)


    def create_acc():
        update_config()
        tgcreatorv1.main("1")


    create_acc_button = tk.Button(win, text="Create account", font=("Times new roman", 16), fg="black", bg="white",
                                  cursor="hand2", bd=5, relief="groove", command=create_acc)
    create_acc_button.place(x=560, y=530, height=50, width=150)


    def login_acc():
        update_config()
        tgcreatorv1.main("3")


    login_acc_button = tk.Button(win, text="login account", font=("Times new roman", 16), fg="black", bg="white",
                                 cursor="hand2", bd=5, relief="groove", command=login_acc)
    login_acc_button.place(x=715, y=530, height=50, width=150)


    def ban_control():
        update_config()
        tgcreatorv1.main("2")


    ban_control_button = tk.Button(win, text="Ban control", font=("Times new roman", 16), fg="black", bg="white",
                                   cursor="hand2", bd=5, relief="groove", command=ban_control)
    ban_control_button.place(x=870, y=530, height=50, width=150)


    def about():
        about_root = tk.Tk()
        about_root.title("about")
        about_root.geometry("600x150+380+240")
        about_root.config(bg="white")
        lable = tk.Label(about_root, text="Links & contact\n\nVisit our website:", font=("times new roman", 12), bg="white",
                         fg="black")
        lable.place(x=0, y=10)

        def callback1(url):
            webbrowser.open_new_tab(url)

        w_link = tk.Label(about_root, text="https://smmsoftsale.com/", font=("times new roman", 12), fg="blue", bg="white",
                          cursor="hand2")
        w_link.place(x=120, y=48)
        w_link.bind("<Button-1>", lambda e:
        callback1("https://smmsoftsale.com/"))

        lable2 = tk.Label(about_root, text="Visit our Youtube channel:", font=("times new roman", 12), bg="white",
                          fg="black")
        lable2.place(x=0, y=70)

        def callback2(url):
            webbrowser.open_new_tab(url)

        y_link = tk.Label(about_root, text="https://www.youtube.com/channel/UC3xbzSuNMj5TP-rNXHsV6BA",
                          font=("times new roman", 12), fg="blue", bg="white", cursor="hand2")
        y_link.place(x=170, y=70)
        y_link.bind("<Button-1>", lambda e:
        callback2("https://www.youtube.com/channel/UC3xbzSuNMj5TP-rNXHsV6BA"))

        lable3 = tk.Label(about_root, text="contact: +918368381698", font=("times new roman", 12), bg="white", fg="black")
        lable3.place(x=0, y=100)
        lable4 = tk.Label(about_root, text="Copyright ©telegrammemberadder.com", font=("times new roman", 12), bg="white",
                          fg="black")
        lable4.place(x=0, y=120)

        about_root.mainloop()


    about_button = tk.Button(win, text="About", font=("Times new roman", 16), fg="black", bg="white", cursor="hand2", bd=5,
                             relief="groove", command=about)
    about_button.place(x=1025, y=530, height=50, width=150)


    def setting():
        path = os.getcwd()
        webbrowser.open(path)


    setting_button = tk.Button(win, text="Settings", font=("Times new roman", 16), fg="black", bg="white", cursor="hand2",
                               bd=5, relief="groove", command=setting)
    setting_button.place(x=1180, y=530, height=50, width=150)



    win.mainloop()

# console_text = tk.Text()
# console_text.pack()
# pl = PrintLogger(console_text)
# sys.stdout = pl