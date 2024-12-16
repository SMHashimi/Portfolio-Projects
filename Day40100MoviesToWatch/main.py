from bs4 import BeautifulSoup
from requests import *

EMPIRE_ONLINE_WEBSITE = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = get(url = EMPIRE_ONLINE_WEBSITE)
movies_100 = response.text


soup = BeautifulSoup(movies_100, "html.parser")
all_100_movies = soup.find_all(name = "h3")

movies_list_from_100_to_1 = []
for movie in all_100_movies:
    from_1_100_movies = movie.text
    movies_list_from_100_to_1.append(from_1_100_movies)
movie_list = movies_list_from_100_to_1[::-1]
print(movie_list)

with open("movies.txt", mode = "w", encoding = "utf-8") as movie_file:
    for movie in movie_list:
        movie_file.write(f"{movie}\n")


