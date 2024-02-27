from bs4 import BeautifulSoup
import requests


# url ="https://webscraper.io/test-sites/tables"
# response = requests.get(url)


# for ok respose
# print(response)


# all htmp element of perticular page not in proper format
# print(response.content)


# for get clear response we use beautiful soup here html parser is use to clean up the code beutifully
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)


# heading tag
# soup = BeautifulSoup(response.content, 'html.parser')
# headings1 = soup.find_all('h1')
# print(headings1)
# heading2 = soup.find_all('h2')
# print(heading2)
# images = soup.find_all('img') # it give full imag
# print(images)
# but we want only src
# images = soup.find_all('img')
# print(images[0]['src'])
# if you want alt
# print(images[0]['alt'])


# we will learn how to get table

# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')
# print(table)


# here we print second table
# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')[1]
# print(table)


# find the row of table
# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')[1]
# rows = table.find_all('tr')
# print(rows)


# removing first row
# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')[1]
# rows = table.find_all('tr')[1:]
# print(rows)



# find last_name
# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')[1]
# rows = table.find_all('tr')[1:]
#
# last_names = []
# for row in rows:
#     print(row.find_all('td'))


# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')[1]
# rows = table.find_all('tr')[1:]
#
# last_names = []
# for row in rows:
#     print(row.find_all('td')[2])



#  remove td
# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')[1]
# rows = table.find_all('tr')[1:]
#
# last_names = []
# for row in rows:
#     print(row.find_all('td')[2].get_text())





# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find_all('table')[1]
# rows = table.find_all('tr')[1:]
#
# last_names = []
# for row in rows:
#     last_names.append(row.find_all('td')[2].get_text())
#
# print(last_names)




# wekipedia python


url ="https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# print all content all page
# print(soup)


# datatype_table = soup.find_all(class_="wikitable")
# print(datatype_table)


datatype_table = soup.find(class_="wikitable")
body = datatype_table.find('tbody')
rows = body.find_all('tr')[1:]

mutable_type = []
immutable_type = []

for row in rows:
    data = row.find_all('td')
    if data[1].get_text()=='mutable\n':
        mutable_type.append(data[0].get_text().strip())
    else:
        immutable_type.append(data[0].get_text().strip())

print(mutable_type)
print(immutable_type)