## now we are going to scrap a real live site 
#our site are going to be https://news.ycombinator.com/

import requests 
from bs4 import BeautifulSoup 

response = requests.get("https://news.ycombinator.com/news") #same as we did with open.. to read html file
#print(response.text) # we will get the html file of the site 
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(largest_number)
print(largest_index)







