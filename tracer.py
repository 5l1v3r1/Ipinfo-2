import requests

import bs4



header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
def tr_ip(ip_adress):
    req = requests.get("https://www.ip-tracker.org/locator/ip-lookup.php?ip={}".format(ip_adress) , headers = header)
    req1 = requests.get("https://www.ip-tracker.org/blacklist-check.php?ip={}".format(ip_adress) , headers = header)
    main_link = bs4.BeautifulSoup(req.text , "html.parser")
    follow_up_link = bs4.BeautifulSoup(req1.text , "html.parser")
    backlist_check  = follow_up_link.find("td" , {"class":"trackingrond"})
    continent = main_link.findAll("td", {"class":"tracking"})
    print(ip_adress)
    print(backlist_check.text)
    print("host name: "+continent[1].text)
    print("continet:" + continent[2].text)
    print("state:" +continent[4].text)
    print("postal: " + continent[5].text)
    print("ISP: " + continent[6].text)
    print("Organization: "+ continent[7].text)
