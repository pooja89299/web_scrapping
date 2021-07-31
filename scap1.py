from bs4 import BeautifulSoup
import requests 
import json
def scap_top_list():
    url = "https://www.imdb.com/india/top-rated-indian-movies/?sort=rk,asc&mode=simple&page=1"
    page = requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    movie=soup.find("tbody",class_="lister-list")
    movies=movie.find_all("tr")
    # print(movies)
    k=[]
    possition=0
    for i in movies:
        possition+=1
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        movie=movie_name


        movie_year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        years=int(movie_year)


        movie_rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        rationg=float(movie_rating)

        movie_link=i.find("td",class_="titleColumn").a["href"]
        link="https://www.imdb.com/"+movie_year


        dict={"Position":possition,"movie name":movie,"year":years,"Rating":rationg,"movei_link":link}
        k.append(dict)
        with open("movie_data_.json","w")as file:
            json.dump(k,file,indent=7)
    return  k
scap_top_list()







        


















