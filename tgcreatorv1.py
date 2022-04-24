countrys = {
    "Russia": "0",
    "Ukraine": "1",
    "Kazakhstan": "2",
    "China": "3",
    "Philippines": "4",
    "Myanmar": "5",
    "Indonesia": "6",
    "Malaysia": "7",
    "Vietnam": "10",
    "Kyrgyzstan": "11",
    "Usa": "12 ",
    "Israel": "13",
    "HongKong": "14",
    "Poland": "15",
    "England": "16",
    "DCongo": "18",
    "Nigeria": "19",
    "Macao": "20",
    "Egypt": "21",
    "India": "22",
    "Ireland": "23",
    "Cambodia": "24",
    "Laos": "25",
    "Haiti": "26",
    "Ivory": "27",
    "Gambia": "28",
    "Serbia": "29",
    "Yemen": "30",
    "Southafrica": "31",
    "Romania": "32",
    "Colombia": "33",
    "Estonia": "34",
    "Canada": "36",
    "Morocco": "37",
    "Ghana": "38",
    "Argentina": "39",
    "Uzbekistan": "40",
    "Cameroon": "41",
    "Chad": "42",
    "Germany": "43",
    "Lithuania": "44",
    "Croatia": "45",
    "Sweden": "46",
    "Iraq": "47",
    "Netherlands": "48",
    "Latvia": "49",
    "Austria": "50",
    "Belarus": "51",
    "Thailand": "52",
    "Saudiarabia": "53",
    "Mexico": "54",
    "Taiwan": "55",
    "Spain": "56",
    "Algeria": "58",
    "Slovenia": "59",
    "Bangladesh": "60",
    "Senegal": "61",
    "Turkey": "62",
    "Czech": "63",
    "Srilanka": "64",
    "Peru": "65",
    "Pakistan": "66",
    "Newzealand": "67",
    "Guinea": "68",
    "Mali": "69",
    "Venezuela": "70",
    "Ethiopia": "71",
    "Mongolia": "72",
    "Brazil": "73",
    "Afghanistan": "74",
    "Uganda": "75",
    "Angola": "76",
    "Cyprus": "77",
    "France": "78",
    "Papua": "79",
    "Mozambique": "80",
    "Nepal": "81",
    "Belgium": "82",
    "Bulgaria": "83",
    "Hungary": "84",
    "Moldova": "85",
    "Italy": "86",
    "Paraguay": "87",
    "Honduras": "88",
    "Tunisia": "89",
    "Nicaragua": "90",
    "Timorleste": "91",
    "Bolivia": "92",
    "Costarica": "93",
    "Guatemala": "94",
    "Uae": "95",
    "Zimbabwe": "96",
    "Puertorico": "97",
    "Togo": "99",
    "Kuwait": "100",
    "Salvador": "101",
    "Libyan": "102",
    "Jamaica": "103",
    "Trinidad": "104",
    "Ecuador": "105",
    "Swaziland": "106",
    "Oman": "107",
    "Bosnia": "108",
    "Dominican": "109",
    "Qatar": "111",
    "Panama": "112",
    "Mauritania": "114",
    "Sierraleone": "115",
    "Jordan": "116",
    "Portugal": "117",
    "Barbados": "118",
    "Burundi": "119",
    "Benin": "120",
    "Brunei": "121",
    "Bahamas": "122",
    "Botswana": "123",
    "Belize": "124",
    "Caf": "125",
    "Dominica": "126",
    "Grenada": "127",
    "Georgia": "128",
    "Greece": "129",
    "Guineabissau": "130",
    "Guyana": "131",
    "Iceland": "132",
    "Comoros": "133",
    "Saintkitts": "134",
    "Liberia": "135",
    "Lesotho": "136",
    "Malawi": "137",
    "Namibia": "138",
    "Niger": "139",
    "Rwanda": "140",
    "Slovakia": "141",
    "Suriname": "142",
    "Tajikistan": "143",
    "Monaco": "144",
    "Bahrain": "145",
    "Reunion": "146",
    "Zambia": "147",
    "Armenia": "148",
    "Somalia": "149",
    "Congo": "150",
    "Chile": "151",
    "Furkinafaso": "152",
    "Lebanon": "153",
    "Gabon": "154",
    "Albania": "155",
    "Uruguay": "156",
    "Mauritius": "157",
    "Bhutan": "158",
    "Maldives": "159",
    "Guadeloupe": "160",
    "Turkmenistan": "161",
    "Frenchguiana": "162",
    "Finland": "163",
    "Saintlucia": "164",
    "Luxembourg": "165",
    "Saintvincentgrenadines": "166",
    "Equatorialguinea": "167",
    "Djibouti": "168",
    "Antiguabarbuda": "169",
    "Caymanislands": "170",
    "Montenegro": "171",
    "Denmark": "172",
    "Switzerland": "173",
    "Norway": "174",
    "Australia": "175",
    "Eritrea": "176",
    "Southsudan": "177",
    "Saotomeandprincipe": "178",
    "Aruba": "179",
    "Montserrat": "180",
    "Anguilla": "181",
    "Japan": "182",
    "Northmacedonia": "183",
    "Seychelles": "184",
    "Newcaledonia": "185",
    "Capeverde": "186",
    "Southkorea": "190"
}
sms_services = {
    "simsms.org": "https://simsms.org/stubs/handler_api.php?",
    "sms-code.store": "http://sms-code.store/stubs/handler_api.php?",
    "getsmscode.com": "http://api.getsmscode.com/do.php?",
    "5sim.net": "https://5sim.net/v1/?",
    "smspva.com": "https://smspva.com/api/rent.php?",
    "sms-activate.org": "https://api.sms-activate.org/stubs/handler_api.php?"
}

try:
    from random import choice
    import traceback
    from requests import get
    from time import sleep
    from json import load, loads, dump, decoder
    from os import system, remove, environ, path
    import os
    from sys import exit
    from telethon.sync import TelegramClient
    from telethon.errors import rpcerrorlist, SessionPasswordNeededError, PhoneNumberUnoccupiedError
    from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
    from telethon.tl.functions.photos import UploadProfilePhotoRequest
    from configparser import ConfigParser, NoSectionError, NoOptionError
    import subprocess,requests,time
    import multiprocessing as mp
    import random # New import
    import string, secrets, urllib.request
    from tkinter import *
    from tkinter import messagebox

except:
    traceback.print_exc()

users_input_global = ""
DIR = r'sessions'
start_accs = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

# CONFIG
try:
    config = ConfigParser()
    config.read('config_GUI.ini')

    # SIM API URL
    c_api_url = sms_services[config.get('sim_api_url', 'api_url')]

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

    # CONFIG

except NoSectionError as e:
    print(
        f'Error!!, config in the file \
            {str(e).strip("No section: ")} partition not found')
except NoOptionError as e:
    print(
        f'Error!!, config in the file \
             {str(e).strip("No section: ")} partition not found')

def update_config():
    global c_api_url, c_country, c_operator, c_product, c_token, c_api_id, c_ap_hash, c_thr_number, c_create_account_count, c_is_generator_photo
    config = ConfigParser()
    config.read('config_GUI.ini')

    # SIM API URL
    c_api_url = sms_services[config.get('sim_api_url', 'api_url')]

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

    # CONFIG




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class AccountMaker:
    def __init__(self, token, country, operator, product, api_id, api_hash):
        self.color = bcolors
        self.country = int(countrys[str(country).capitalize()])
        self.token = token
        self.operator = operator
        self.product = product
        self.api_id = api_id
        self.api_hash = api_hash
        self.buy_param = (('api_key', self.token), ('action', 'getNumber'), (
            'service', self.product), ('operator', self.operator), ('country', self.country))
        self.balance_param = (('api_key', self.token),
                              ('action', 'getBalance'))
        self.url = f"{c_api_url}"
        #self.url = 'https://api.sms-activate.org/stubs/handler_api.php?api_key={API_KEY}&action=setStatus&status=8&id={PHONE_KEY_ID'

    def create_account(self):
        global DIR
        need_accs = int(c_create_account_count)
        cur_accs = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        if need_accs <= (cur_accs - start_accs):
            return print(f"Limit accounts")

        balance = float(str(get(self.url,
                                params=self.balance_param).text).split(":")[-1])
        try:
            self.counter = 500
            print(self.color.OKGREEN +
                  f"\nBalance : {balance}\n"+self.color.ENDC)
            response = str(
                get(self.url, params=self.buy_param).text).split(":")
            try:
                phone = response[2]
                id = response[1]
            except:
                return print("No phone")
            print(self.color.OKCYAN +
                  f"Number: {phone}   |   Number ID: {id}\n" + self.color.ENDC)
            try:
                client = TelegramClient(
                    f"sessions/{phone}", self.api_id, self.api_hash)
                client.connect()
                send_code = client.send_code_request(phone=phone)
                self.code_sent(id)
                return self.get_code(client, id, phone, send_code)
            except rpcerrorlist.PhoneNumberBannedError:
                self.cancel_order(phone=phone, id=id, ban=True)
                return self.create_account()
            except rpcerrorlist.FloodWaitError:
                self.cancel_order(phone=phone, id=id, flood=True)
                return self.create_account()
            except rpcerrorlist.PhoneNumberInvalidError:
                self.cancel_order(phone=phone, id=id, flood=True)
                return self.create_account()
        except KeyboardInterrupt:
            print(self.color.FAIL+"\nexiting...\n"+self.color.ENDC)
            #return main()
        except IndexError:
            pass#return main()

    def code_sent(self, id):
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '1'), ('id', id))
        get(self.url, params=params)

    def get_code(self, client, id, phone, send_code):
        params = (('api_key', self.token),
                  ('action', 'getStatus'), ('id', id),)
        while True:
            if self.counter == 0:
                self.cancel_order(id, phone)
                return self.create_account()
            response = str(get(self.url, params=params).text)
            print(self.color.OKBLUE+"Code Waiting....."+self.color.ENDC)
            if response != "STATUS_WAIT_CODE":
                try:
                    code = response.split(":")[-1]
                    print(self.color.OKGREEN +
                          f"\nCode received: {code}\n"+self.color.ENDC)
                    client.sign_in(phone=phone, code=code)
                    #client.sign_up(code=code, first_name="Users", phone=phone)
                    print(client.is_user_authorized())
                    client.disconnect()
                    self.save_number(phone)
                    self.finish(id)
                    self.wait()
                    return self.create_account()
                except IndexError:
                    print(response)
                    #return main()
                except SessionPasswordNeededError:
                    print(
                        self.color.FAIL+"\nThis account was previously taken by someone else and the password was added, sorry you will not get your money back :(\n" + self.color.ENDC)
                    self.wait()
                    return self.create_account()
                except PhoneNumberUnoccupiedError:
                    name = random_line("data/names.txt").strip()  # New code
                    last_name = random_line("data/last_names.txt").strip()  # New code
                    about = random_line("data/about1.txt") # New code
                    client.sign_up(phone_code_hash=send_code.phone_code_hash,
                                   code=code, first_name=name, phone=phone)
                    print(
                        self.color.OKGREEN+f"\nAccount Created!!!\nAccount name: {client.get_me().first_name}\n"+self.color.ENDC)
                    self.save_number(phone)

                    try:
                        print("[!]Updating FirstName")
                        client(UpdateProfileRequest(
                            first_name=str(name),
                        ))

                        print("[!]Updating LastName")
                        client(UpdateProfileRequest(
                            last_name=str(last_name),
                        ))

                        print("[!]Updating About")
                        client(UpdateProfileRequest(
                            about=str(about)
                        ))

                        print("[!]Updating ProfilePic")
                        if c_is_generator_photo:
                            random_imagename = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                                                       for i in range(8))
                            image = urllib.request.urlretrieve("https://picsum.photos/200/300?random=1", f"./images/{random_imagename}.jpg")
                            client(UploadProfilePhotoRequest(client.upload_file(image)))
                        else:
                            client(UploadProfilePhotoRequest(
                                client.upload_file('images/' + str(random.randint(1, 4)) + '.jpg')))

                        client.loop.run_until_complete(del_limit(client)) # Try to unban for spam

                    except Exception as e:
                        continue

                    self.finish(id)
                    self.wait()
                    client.disconnect()
                    break

                except Exception as e:
                    print("To many requests to Telegram, waiting 100 seconds...")
                    sleep(100)
                    return self.create_account()
            else:
                sleep(3)
                self.counter -= 5
                continue

    def cancel_order(self, id, phone, ban=False, flood=False):
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '-1'), ('id', id))
        if ban:
            print(self.color.FAIL +
                  '\n[*] Number blocked by telegram, Number canceling..'+self.color.ENDC)
        elif flood:
            print(self.color.FAIL +
                  '\n[*] The number has a waiting period, the number is being cancelled...'+self.color.ENDC)
        else:
            print(self.color.FAIL +
                  "\n[*] Code not received within the specified time, Number canceling.."+self.color.ENDC)
        if get(self.url, params=params).text == "ACCESS_CANCEL":
            self.wait()
        try:
            remove(f"sessions/{phone}.session")
        except:
            pass
        return

    def save_number(self, number):
        with open("data/phones.json", "r") as f:
            data = load(f)
        data['phone_numbers'].append(number)
        with open("data/phones.json", "r+") as f:
            dump(data, f)

    def finish(self, id):
        params = (('api_key', self.token), ('action', 'setStatus'),
                  ('status', '6'), ('id', id))
        get(self.url, params=params)

    def wait(self):
        print(self.color.WARNING +
              "\n Waiting 5 seconds for new account..."+self.color.ENDC)
        sleep(5)


def login_accounts():
    with open("data/phones.json", "r") as f:
        data = load(f)
    phone_data = data["phone_numbers"]
    for id, number in enumerate(phone_data):
        print(f"[{id}] {number}")
    #id = input("Please enter the number of the account you want to login :> ")
    id = input_window()

    if not id:
        print("You have not made a selection, you are being redirected to the menu!!")
        return None
    print (id)
    selected_number = phone_data[int(id)]
    print(f"The number you chose: [{selected_number}]\n")
    print(f"Trying to login please wait..")
    client = TelegramClient("sessions/"+selected_number, c_api_id, c_ap_hash)
    client.connect()
    if client.is_user_authorized():
        print("Account created please ask for Code to login and press enter (only when you request Code)")
        print("Code Waiting...")
        while True:
            try:
                message = client.get_messages(777000, limit=1)
                code = message[0].message.split(":")[1].split(".")[0]
                print("Code received!!!!")
                print(f"Code:{code}")
                client.disconnect()
                break
            except IndexError:
                continue



def check_ban():
    list = []
    with open("data/phones.json", "r") as f:
        d = load(f)
    for i in d['phone_numbers']:
        client = TelegramClient(f"sessions/{i}.session", c_api_id, c_ap_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(i)
            except rpcerrorlist.PhoneNumberBannedError:
                print(bcolors.FAIL+f"{i}: Banned"+bcolors.ENDC)
                #print(f"{i}: Banned")

                client.disconnect()
                remove(f"sessions/{i}.session")
        else:
            print(bcolors.OKGREEN+f"{i}: Active"+bcolors.ENDC)
            #print( f"{i}: Active" )
            list.append(i)
            client.disconnect()
    d['phone_numbers'] = list
    with open("data/phones.json", "w") as l:
        dump(d, l)
    print(f"\nNumber List updated, banned numbers and session files deleted\n")
    #input(bcolors.OKCYAN+"\nNumber List updated, banned numbers and session files deleted\n"+bcolors.ENDC)
    #return main()


def input_window():
    # Create a Toplevel window
    top = Toplevel()
    top.geometry("250x50")
    users_input = StringVar()
    # Create an Entry Widget in the Toplevel window
    entry = Entry(top, width=25, textvariable=users_input)
    entry.pack()

    var = IntVar()
    # Create a Button Widget in the Toplevel Window

    button = Button(top, text="Ok", command=lambda: var.set(1))
    button.pack(pady=5, side=TOP)
    button.wait_variable(var)
    return users_input.get()







def banner():
    print()


def menu():
    print(bcolors.OKCYAN+"""\n
*************************** Menu ******************************
*                                                             *
* [1] Account Builder          [2] Ban Control                *
* [q] Exit                     [3] Login to accounts          *
*                                                             *
***************************************************************
"""+bcolors.ENDC)


def main(action=False):
    try:
        banner()
       # menu()
        if not action:
            op = input(bcolors.OKGREEN+"\nMenu :> "+bcolors.ENDC)
        else:
            update_config()
            op = action
            sleep(0.1)
        if str(op) == "1":
            print ("test1")
            maker = AccountMaker(token=c_token, country=c_country, operator=c_operator,
                                 product=c_product, api_id=c_api_id, api_hash=c_ap_hash)
            print("test2")
            multi_threading(func_name=maker.create_account)
        elif str(op) =="2":
            check_ban()
        elif str(op) =="3":
            login_accounts()
        elif str(op).lower() == "q":
            exit()
        else:
            input("Incorrect operation")
            #return main()
    except KeyboardInterrupt:
        print("\nexiting...")
        exit()

def multi_threading(func_name):
    'Initiate threads from config'
    DIR = r'sessions'
    need_accs = int(c_create_account_count)
    cur_accs = 0
    start_accs = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    with open(r"proxy.json") as proxies: # Open file with proxy
        proxies = loads(proxies.read())
    thr_list = []

    while need_accs > (cur_accs-start_accs):
        try:
            for el in range(int(c_thr_number)):
                sleep(2)
                try:
                    environ['http_proxy'] = proxies[str(el)]
                except IndexError:
                    print("Wrong proxy index working on local IP")
                ctx = mp.get_context('spawn')
                thread = ctx.Process(target=func_name)
                thr_list.append(thread)
                thread.start()
                cur_accs = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
                if need_accs <= (cur_accs - start_accs):
                    thread.terminate()
                    time.sleep(0.1)
                    return print(f"Complite")
            for thr in thr_list:
                thr.join()
        except:
            continue

async def del_limit(client):
    try:
        print("Trying to remove limit")
        await client.send_message("@spambot", "/start")
        time.sleep(1)
        await client.send_message("@spambot", "But I can’t message non-contacts!")
        time.sleep(1)
        await client.send_message('@spambot', "No, I’ll never do any of this!")
        time.sleep(1)
        radnom_message = ["hello idk bro", "i dont know", "pls remove my limit", "delete limits please",
                          "why its limited i made this account freshly", "telegram del my limit"
            , "delete limit urgent", "🥺🥺🥺", "🧐"]
        await client.send_message("@spambot", random.choice(radnom_message))
        print("sent request to spambot")

    except Exception as e:
        print(e)
        print("Error : failed limit del request.")

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


if __name__ == "__main__":
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\nexiting...")
        exit()
