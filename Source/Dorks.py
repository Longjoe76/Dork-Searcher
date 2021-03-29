#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#0737
#

try:
    import requests
    from bs4 import BeautifulSoup
    import os
    from os import system
    import random
    system("title " + "Soud Was Here - @8Y - Soud#0737")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()

good, bad, error, ban = 0, 0, 0, 0
logo = """
         _______   __
   ____ |  _  \ \ / /
  / __ \ \ V / \ V / 
 / / _` |/ _ \  \ /  
| | (_| | |_| | | |  
 \ \__,_\_____/ \_/  
  \____/             
"""
print(f"{Fore.CYAN}{logo}")
print("Dork Searcher V0.2 ")
print(f"{Fore.GREEN}\n\tInstagram: @8Y\n\tGithub: @Soud69\n\tDiscord: Soud#0737\n\tTelegram: @Soud69{Fore.RED}\n\t[Dont Try To Sell It]\n")
dork_name = input("Enter Your Dork File (dork.txt): ")
dork_file = open(dork_name, "r")
proxy_name = input("Enter Your Proxy File (proxy.txt): ")
proxy_file = open(proxy_name, "r")
while 1:
    proxy_dict = []
    for proxy in proxy_file:
        proxy_dict.append(proxy)
        rnd = str(random.choice(proxy_dict))
    try:
        proxyfinal = {
            "http": f"http://{rnd}",
            "https": f"https://{rnd}"
        }
        dork = dork_file.readline().split("\n")[0]
        if dork == "":
            print(f"Done Checking\nGood: {good} | Bad: {bad} | Error: {error} | Ban: {ban}")
            input()
            break
        google_req = requests.get(f"https://www.google.com/search?q={dork}&num=500", proxies=proxyfinal, timeout=5)
        if '<script src="https://www.google.com/recaptcha/api.js"' in google_req.text:
            ban += 1
        elif 'class="kCrYT"><a href="' in google_req.text:
            good += 1
            print(f"{Fore.GREEN}{dork}")
            google_soup = BeautifulSoup(google_req.text, "html.parser")
            google_dork = google_soup.select(".kCrYT a")
            for i in google_dork:
                google_dorks = i["href"]
                google_dorks_fixed = google_dorks.replace("/url?q=", "")
                with open("google-dorks.txt", "a") as save:
                    save.write(f"{google_dorks_fixed}\n")
                    save.close()
        elif 'class="kCrYT"><a href="' not in google_req.text:
            bad += 1
            print(f"{Fore.RED}{dork}")
        else:
            error += 1
            print(f"{Fore.YELLOW}{dork}")
    except:
        ban += 1

input("Click Enter To Exit")
