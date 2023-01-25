from bs4 import BeautifulSoup
import lxml #another type of parser if html.parser will not work . usage: soup = BeautifulSoup(contents, "lxml.parser")

with open("website.html", encoding="utf8") as file:  #without the encoding will not work 
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser") #soup is now beautifulsoup object that #contains the data of website.html
print(soup.title) # will print the title 
print(soup.a) # will print first a tag in the document (<a  >)
#print(soup.p)  #will print first paragaph of the document (<p    >)
all_ancors_tags = soup.find_all(name ="a") # will give as a list of all ancor tags in the document
print(all_ancors_tags)

for tag in all_ancors_tags:
    #print(tag.getText()) # method to get text from the tag, will give as text of all the ancor tags
    print(tag.get("href")) #get all the links in the documents 

    
heading = soup.find(name="h1", id="name")  # find something particular by tag name and  id 
print(heading) #will give as the heading content 
section_heading = soup.find(name="h3", class_="heading") #find something particular by tag name and class name , class_ =>because class is python keyword 
print(section_heading)

company_url = soup.select_one(selector = "p a") #will give as the first ancor which sits in paragraph, soup.select() allows as search by css selectors
print(company_url)

#soup.select() will give us a list instead of first maching item like select_one()


    


