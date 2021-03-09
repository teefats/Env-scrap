import requests

from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
first_h1 =html_soup.find('h1')
print(first_h1.name)
print(first_h1.contents)
daisy = first_h1.contents
# print(type(daisy))
# print(daisy[1])
print(str(first_h1))
print(str(first_h1.text))
print(first_h1.get_text())
print(first_h1.attrs)
print(first_h1.attrs['id'])
# print(html_soup.find('', {'id':'p-logo'}))
# print(html_soup.find('span', {'class':'mw-editsection-bracket'}))
# for found in html_soup.find_all(['h1', 'h2']):
#     print(found)
cites = html_soup.find_all('cite', class_="citation", limit=5)
for citation in cites:
    print(citation.get_text())
    link = citation.find('a')
    print(link.get('href'))
    print()


# Fecth table data
episodes =[]
ep_tables =
