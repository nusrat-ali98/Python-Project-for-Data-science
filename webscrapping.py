from bs4 import BeautifulSoup
import requests
import pandas as pd


html = "<!DOCTYPE html><html><head><title>Web Scrapping</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html , "html.parser")

# method prettify() to display the HTML in the nested structure:
## print(soup.prettify())

tag_object = soup.h3
# print("tag object:",tag_object)

tag_child = tag_object.b

# HTML Attributes
# tag_child.attrs
# print(tag_child.attrs,tag_child['id'])

# Navigable String
tag_string = tag_child.text
# print(tag_string)
# print(type(tag_string))

unicode_string = str(tag_string)
# print(unicode_string)

table = "<table> <tr><td id='flight'>Flight No</td><td>Launch site</td><td>Payload mass</td> </tr> <tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>80 kg</td></tr></table>"

table_soup = BeautifulSoup(table ,"html.parser")

# find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
table_rows = table_soup.find_all('tr')
# print(table_rows)

first_row = table_rows[0]
# print(first_row)

# If we iterate through the list, each element corresponds to a row in the table:
# for i,rows in enumerate(table_rows):
#     print("row",i)
#     cells=rows.find_all('td')
#     for j,cell in enumerate(rows):
#         print("column:",j,"cell",cell)


list_input=table_soup.find_all(name=["tr","td"])
# print(list_input)


# print(table_soup.find_all(id='flight'))

# print(table_soup.find_all(string="Florida"))

# Code with two table
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

two_table_soup=BeautifulSoup(two_tables,"html.parser")
# print(two_table_soup.find("table"))
# print(two_table_soup.find("table",class_="pizza"))

# Downloading and Scraping the contents of a webpage

url = "http://www.ibm.com"
data = requests.get(url).text
ibm_soup=BeautifulSoup(data,"html.parser")

# for link in ibm_soup.find_all("a",href=True):
    # print(link.get('href'))

# Scrape  all images  Tags

# for link in ibm_soup.find_all('img'):
#     print(link)
#     print(link.get("src"))

#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
table_data=requests.get(url).text
table_data_soup=BeautifulSoup(table_data,"html.parser")
table=table_data_soup.find("table")

# for row in table.find_all("tr"):
#     cols=row.find_all('td')
#     color_name = cols[2].text
#     color_code = cols[3].text
#     print("{}--->{}".format(color_name,color_code))

url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
tables=soup.find_all("table")
print(len(tables))

for index , table in enumerate(tables):
    if("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
print(tables[table_index].prettify())
       
population_data = pd.DataFrame(columns=["Rank" , "Country","Population","Area","Density"])
for row in tables[table_index].tbody.find_all('tr'):
    col = row.find_all("td")
    if(col != []):
        rank=col[0].text
        country=col[1].text
        population = col[2].text.strip()
        area=col[3].text.strip()
        density =col[4].text.strip()
        new_data = pd.DataFrame({"Rank": [rank], "Country": [country], "Population": [population], "Area": [area], "Density": [density]})
        population_data = pd.concat([population_data, new_data], ignore_index=True)

print(population_data)

