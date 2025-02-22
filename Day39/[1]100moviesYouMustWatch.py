import requests #type: ignore
from bs4 import BeautifulSoup #type:ignore

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_Webpage = response.text

soup = BeautifulSoup(movies_Webpage,"html.parser")

movie_titles = soup.find_all(name="h3", class_="title")

titles = [title.getText() for title in movie_titles]

titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.writelines(f"{title}\n")
