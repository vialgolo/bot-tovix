import requests
from bs4 import BeautifulSoup
import urllib.request
import time
import json

n = 90349
for h in range(n):

	session = requests.Session()

	jar = requests.cookies.RequestsCookieJar()
	jar.set('xf_session', 'i71TBxHZSBmVGVjAEixmtvjjgub9YwAA')

	session.cookies = jar

	r = session.get("https://altenens.is/forums/accounts-and-database-dumps.45/")

	soup = BeautifulSoup(r.content, 'html.parser')

	links = []	
	for link in soup.find_all('a'):
	    links.append(link.get('href'))

	links2 = ("https://altenens.is"+links[122])

	r2 = session.get(links2)

	soup2 = BeautifulSoup(r2.content, 'html.parser')

	al = soup2.find_all('div', class_='bbWrapper')

	alten = list()

	count = 0
	for i in al:
		if count < 1:
			alten.append(i.text)
		else:
			break
		count += 1

	elim1 = "@_zxcvbnmasdfghjklñqwertyuiopZXCVBNMASDFGHJKLÑQWERTYUIOP://,'!. "
	text = alten
	text1=""
	for letra in text:
		if letra not in elim1:
			text1 = text1+letra

	elim2 = "@_zxcvbnmasdfghjklñqwertyuiopZXCVBNMASDFGHJKLÑQWERTYUIOP:,'!. "
	text3 = text1
	text4=""
	for letra2 in text3:
		if letra2 not in elim2:
			text4 = text4+letra2

	if (any(chr.isdigit() for chr in text4)) == True:
		url_req1 = "https://lookup.binlist.net/" + text4
		results1 = requests.get(url_req1)
		results2 = (results1.json())
		results3 = json.dumps(results2)
		results4 = json.loads(results3)
		results5 = ("Brand: " + results4['scheme'] + ", Type: " + results4['type'] + ", Level: " + results4['brand'] + ", Bank: " + results4['bank']['name'] + ", Bank: " + results4['country']['name'] )
		
		def send_msg(text):
				token = "1529602064:AAGqa3IhXBEjdD9MR7YZIG2FbSUSmfxG2p0"
				chat_id = "-1001246519565"

				url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
				results = requests.get(url_req)
				return (results.json())

		send_msg(text4 + results5)
		time.sleep(20)

	else:
		time.sleep(20)

