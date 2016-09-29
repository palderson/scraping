import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.narpm.org/find/property-managers?submitted=true&toresults=1&resultsperpage=2000&a=managers&orderby=&fname=&lname=&company=&chapter=&city=&state=&xRadius=&cert=&page=0")
r = requests.get("http://www.narpm.org/find/property-managers?submitted=true&toresults=1&resultsperpage=2000&a=managers&orderby=&fname=&lname=&company=&chapter=&city=&state=&xRadius=&cert=&page=1")
r = requests.get("http://www.narpm.org/find/property-managers?submitted=true&toresults=1&resultsperpage=2000&a=managers&orderby=&fname=&lname=&company=&chapter=&city=&state=&xRadius=&cert=&page=2")

soup = BeautifulSoup(r.content)

manager = soup.find_all("div", {"class": "member-accordion-list-wrapper"})

for item in manager:
	try:
		print "<tr><td>'%s'</td>" %(item.contents[0].find_all("div", {"class": "member-name"})[0].text)
	except:
		pass
	try:
		print "<td>'%s'</td>" %(item.contents[0].find_all("span", {"class": "member-company"})[0].text)
	except:
		pass
	try:		
		print "<td>'%s'</td>" %(item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text)
	except:
		pass
	try:			
		print "<td>'%s'</td></tr>" %(item.contents[1].find_all("div", {"class": "phone"})[0].text)
	except:
		pass
