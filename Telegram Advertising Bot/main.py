import os
import time
from datetime import datetime, timezone, timedelta

try:
    import colorama, pystyle, bs4, tqdm, pandas, tabulate, requests
except ModuleNotFoundError:
    os.system("pip install telethon")
    os.system("pip install colorama")
    os.system("pip install pystyle")

os.system("title Telegram Controler 🤖 / Dev by rayan38000")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()
from telethon.sync import TelegramClient
from pystyle import Colors, Colorate, Write
from colorama import Fore, Style

title = """
                                                                          
 _____     _                          _____         _           _         
|_   _|___| |___ ___ ___ ___ _____   |     |___ ___| |_ ___ ___| |___ ___ 
  | | | -_| | -_| . |  _| .'|     |  |   --| . |   |  _|  _| . | | -_|  _|
  |_| |___|_|___|_  |_| |__,|_|_|_|  |_____|___|_|_|_| |_| |___|_|___|_|  
                |___| Advertising Bot                                                   
                
"""
styled_title = Colorate.Horizontal(Colors.blue_to_cyan, title)
print(styled_title)



api_id = input("Telegram account api id: ")
api_hash = input("Telegram account hash api: ")
phone_number = input("Telegram account phone number: ")
cooldown = int(input("Waiting time after next ad (in seconds): "))

with TelegramClient('session_name', api_id, api_hash) as client:
    client.connect()
    group_liste = []

    # Récupération de la liste des canaux
    with open("advertisingGroups.txt", 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()

    print("""
List of channels concerned by advertising :""")
    for ligne in lignes:
        print(f">>> {Fore.YELLOW+ligne.strip()+Style.RESET_ALL}")
        group_liste.append(ligne.strip().split("/")[-1])

    # Récupération du message de pub
    with open("advertisingMsg.txt", 'r', encoding='utf-8') as fichier:
        message = fichier.read()
    print(f"""
Message to publish :
{Fore.YELLOW+message+Style.RESET_ALL}""")

    # Liste des chemins vers les fichiers
    media_files = ["media/"+f for f in os.listdir("media") if os.path.isfile(os.path.join("media", f))]
    print("""
Media list attached :""")
    for file in media_files:
        print(f">>> {file}")
    print()



    # Vérifier si l'utilisateur est déjà connecté, sinon, envoyez le code de confirmation
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter the confirmation code : '))

    input(f">>> The bot is ready to start advertising! It will run on {str(len(group_liste))} group(s) every {str(cooldown)} seconds. Press [enter] to launch the bot.")
    while True:
        for group in group_liste:

            heure_et_date_locale = datetime.now(timezone.utc).astimezone()
            fuseau_horaire_francais = timedelta(hours=1) if heure_et_date_locale.dst() == timedelta(0) else timedelta(hours=2)
            heure_et_date_francaise = heure_et_date_locale + fuseau_horaire_francais
            date_francaise = heure_et_date_francaise.strftime("%Y-%m-%d")
            heure_francaise = heure_et_date_francaise.strftime("%H:%M:%S")

            try:
                group_entity = client.get_entity(group)
                media_ids = []
                if os.listdir("media"):
                    for file_path in media_files:
                        media = client.upload_file(file_path)
                        media_ids.append(media)
                        client.send_message(group_entity, message, file=media_ids)
                else:
                    client.send_message(group_entity, message)
                
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] [{date_francaise}] [{heure_francaise}] Message sent to  {Fore.YELLOW+group+Style.RESET_ALL}")
            except:
                print(f"[{Fore.RED}!{Style.RESET_ALL}] [{date_francaise}] [{heure_francaise}] An error happened while sending the message to {Fore.YELLOW+group+Style.RESET_ALL}")

        time.sleep(cooldown)