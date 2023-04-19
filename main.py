from pystyle import *
import requests
from mcquery import mcquery
import random
import string
import base64
import os
from cryptography.fernet import Fernet

print(f'''{Colors.light_red}
                        ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓     ██████  █    ██   ██████  ██░ ██  ██▓
                        ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒   ▒██    ▒  ██  ▓██▒▒██    ▒ ▓██░ ██▒▓██▒
                       ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░   ░ ▓██▄   ▓██  ▒██░░ ▓██▄   ▒██▀▀██░▒██▒
                       ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░      ▒   ██▒▓▓█  ░██░  ▒   ██▒░▓█ ░██ ░██░
                       ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░    ▒██████▒▒▒▒█████▓ ▒██████▒▒░▓█▒░██▓░██░
                        ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░      ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  
                         ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░       ░ ░▒  ░ ░░░▒░ ░ ░ ░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░
                       ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░         ░  ░  ░   ░░░ ░ ░ ░  ░  ░   ░  ░░ ░ ▒ ░
                             ░  ░  ░  ░    ░ ░        ░                    ░     ░           ░   ░  ░  ░ ░  
                                                   {Colors.white}discord.gg/easyteam
                                      {Colors.light_red} ╔══════════════╦══════════════╦══════════════╗
                                      {Colors.light_red} ║              ║              ║              ║
                                      {Colors.light_red} ║ [1]Message   ║  [2] QUERY   ║  [3] IP TOOL ║
                                     {Colors.light_red}  ║  channel     ║              ║              ║
                              {Colors.light_red}╔════════╩═════╦════════╩═══════╦══════╩════════╦═════╩════════╗    
                              {Colors.light_red}║              ║                ║               ║              ║
                              {Colors.light_red}║[4] GENERATOR ║  [5] ID TO     ║  [6] CYPTER   ║ [7] soon     ║
                              {Colors.light_red}║ MOTS DE PASSE║     TOKEN      ║   THE FOLDERS ║              ║
                              {Colors.light_red}╚══════════════╩════════════════╩═══════════════╩══════════════╝                   
''')
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    with open("Logs/generate_passwords.txt", "a+") as file:
      file.write(password + "\n")
      file.close()
    return password
def encrypt(key, filename):
  with open(filename, 'rb') as f:
    plaintext = f.read()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plaintext)

    with open(filename + '.enc', 'wb') as f:
        f.write(cipher_text)
def decrypt(key, filename):
    with open(filename, 'rb') as f:
        ciphertext = f.read()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(ciphertext)
    with open(filename[:-4], 'wb') as f:
        f.write(plain_text)        

  
def query(ip, port):
 with mcquery(ip, port=port, timeout=10) as data:
  print(f'''{Colors.light_red}
      ⚙️ | Statut:{Colors.white} Online (🟢)\n    
      ⚙️ | IP:{Colors.white} {data.host_ip}\n    
      ⚙️ | Port:{Colors.white} {data.host_port}\n         
      ⚙️ | Nombre de joueur en ligne:{Colors.white} {data.num_players} / {data.max_players}\n          
      ⚙️ | Version du serveur:{Colors.white} {data.version} \n
      ⚙️ | Plugins:{Colors.white} {data.plugins}\n  
      ⚙️ | MOTD:{Colors.white} {data.motd}
''') 

def IpOption(ip):
    api = f"http://ip-api.com/json/{ip}"
    data = requests.get(api).json()
    print (f"{Colors.light_red}[Victim]:", data['query'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red} [Fournisseur Internet]:{Colors.white}", data['isp'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red} [Organisation]:{Colors.white}", data['org'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red} [Ville]:{Colors.white}", data['city'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red} [Region]:{Colors.white}", data['region'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red}[Longitude]:{Colors.white}", data['lon'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red}[Latitude]:{Colors.white}", data['lat'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red}[Time zone]:{Colors.white}", data['timezone'])
    print(f"{Colors.red}<--------------->")
    print (f"{Colors.light_red}[Code Postale]:{Colors.white}", data['zip'])

def SendWeboohk(message, webhook):
  data = {
  "username": "EasyTeam | Tool",
  "embeds": [
    {
      "author": {
        "name": "- EasyTeam -"
      },
     "title": "EasyTeam | Annonce",
      "url": "https://discord.gg/easyteam",
     "description": f"{message}",
     "color": "15258703",
     "image": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5a/A_picture_from_China_every_day_108.jpg"
      },
      "footer": {
       "text": "EasyTeam・Tool officiel de la EasyTeam"
      }
    }
  ]
 }
  with open("Logs/message_channel.txt", "a+") as file:
   file.write(message + "\n")
   file.close()
  requests.post(webhook, json = data)
while True:  
 option = input(f"{Colors.green}[+] Options:{Colors.white} ")
   
 if option == "1":
   webhook = input(f"{Colors.green}[+] Webhhok:{Colors.white} ") 
   while True:
    message = input (f"\n\n{Colors.green}[+] Message:{Colors.white} ") 
    SendWeboohk(message, webhook)



 if option == "2":
   ip = input(f"{Colors.green}[+] Ip:{Colors.white} ")
   port = input (f"{Colors.green}[+] Port:{Colors.white} ")
   port = int(port)
   try:
    query(ip, port)
   except:
    print(f"Error :{Colors.white} (ip) / (port)") 



 if option == "3":
   ip = input(f"{Colors.green}[+] Ip:{Colors.white} ")
   try:
    IpOption(ip)
    with open("Logs/ip_tool.txt", "a+") as file:
      file.write(ip + "\n")
      file.close()
   except:
    print(f"Error :{Colors.white} IP INVALID") 



 if option == "4":
    caracteres = input(f"{Colors.green}[+] Caractères:{Colors.white} ") 
    caracteres = int(caracteres)
    password = generate_password(caracteres)
    print(password)


 if option == "5":
    id = input(f"{Colors.green}[+] Id:{Colors.white} ")
    encodedBytes = base64.b64encode(id.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(f'\n{Colors.light_red}══════════════════════════════════════════════════════════════════\n    {Colors.white}Token :{Colors.light_red} {encodedStr}    \n══════════════════════════════════════════════════════════════════')
    with open("Logs/id_to_token.txt", "a+") as file:
     file.write(encodedStr + "\n")
     file.close()  


 if option == "6":   
  filename = input(f"{Colors.green}[+] Nom du fichier à crypter/décrypter: {Colors.white}")
  key = input(f"{Colors.green}[+] Key: {Colors.white}")
  key = bytes(key, encoding='utf-8')


  if os.path.isfile(filename):
    encrypt(key, filename)
    print(f"Le fichier {filename} a bien été crypter")

    decrypt(key, filename + '.enc')
    print(f"Le fichier {filename} a bien été decrypter")
  else:
    print(f"Le fichier {filename} n'est pas trouver !")  
