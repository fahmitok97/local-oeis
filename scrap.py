import requests
from bs4 import BeautifulSoup
import time
import json

result = []

for i in range(1, 1001):
	idx = "A0" + str(i).zfill(5)
	url = "https://oeis.org/" + idx

	print "getting sequence with url {}".format(url)
	resp = requests.get(url)

	if(resp.status_code != 200):
		print "err on {}".format(i)

	soup = BeautifulSoup(resp.text, 'html.parser')
	sequence = soup.select("tt")[0].text
	name = soup.findAll("td", {"valign" : "top", "align" : "left"})[1].text.split('\n')[1].strip()
	result.append({"name" : name, "sequence" : sequence, "idx" : idx})

	f = open('result.json', 'w')
	f.write(json.dumps(result))
	f.close()
	time.sleep(10)