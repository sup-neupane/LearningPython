#Some websites dosent let us interact with them through API
#In web scraping we look through underlying HTML code of website to create soup
#Beautiful Soup is HTML Parser which allows us to do so

#Create Soup As:
# soup = BeautifulSoup( insert_content, parser)

#You can now access the entire content using soup
#Parser is necessary to define what kind of file is it parsing
#e.g. you can het hold of title by soup.title
#you can get gold of its contents by soup.title.string

#Find first paragraph by soup.p
#Find all paragraph as soup.find_all(name = "p")
#You can use get() to search by attributes

#In any website add /robots.txt to seee for what can be legally scraped

#Scraping a live website:
import requests #type: ignore
from bs4 import BeautifulSoup #type:ignore

response = requests.get("https://news.ycombinator.com/news") 
#Use requests module to get hold of data

# print(response.text)   #This gives the entire HTML file
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.prettify())    #Make the response easier to visualise

article_text = soup.select(".titleline")  #Select all tags with class selector .titleline
print(article_text[0].text)


#Getting Upvote of first article:
upvote = soup.select_one('.score')  #Selects first tag with class .score
print(upvote.text)







