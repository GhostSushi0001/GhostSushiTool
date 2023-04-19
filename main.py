from pystyle import *
import requests, json
from mcquery import mcquery

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
                                      {Colors.light_red} ║ {Colors.green}[1]{Colors.white}Message{Colors.light_red}   ║  {Colors.green}[2]{Colors.white} QUERY {Colors.light_red}  ║  {Colors.green}[3] {Colors.white}IP TOOL{Colors.light_red} ║
                                     {Colors.light_red}  ║  {Colors.white}channel{Colors.light_red}     ║ {Colors.light_red}             ║              ║
                                    {Colors.light_red}   ╚══════════════╬══════════════╬══════════════╝                                
''')

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
   except:
    print(f"Error :{Colors.white} IP INVALID") 
  
