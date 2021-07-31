from scap1 import scap_top_list
from task_2 import group_by_decade
import json

scrapped_data=scap_top_list()
movie_by_year=group_by_decade(scrapped_data)
def group_by_decades_1(movies):
    moviedec={}
    list1=[]
    for year in movies:
        mod=year%10
        decade=year-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()

    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
        with open("my_file3.json","w")as file:
            json.dump(moviedec,file,indent=4)
    return moviedec
group_by_decades_1(movie_by_year)

