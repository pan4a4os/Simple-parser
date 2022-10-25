from bs4 import BeautifulSoup
import urllib.request


url = "https://disfold.com/world/companies/?page=20"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)

soup = BeautifulSoup(response, 'html.parser')

f = open('text.txt', 'w', encoding='utf-8')

list_data = []
for i in soup.select('a[href^="/company/"]'):
    list_data.append(i.text)


new_list = []
for el in list_data:
    if not '$' in el:
        new_list.append(el)
    else:
        pass

f.write("\n".join(new_list))
print("\n".join(new_list))
f.close()