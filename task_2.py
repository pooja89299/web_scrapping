from scap1 import scap_top_list
# from task_2 import  scap_top_list
import json

k=scap_top_list()
def group_by_decade(movies):
    years=[]
    for i in movies:
        if i["year"] not in years:
            years.append(i["year"])
    movie_dict={i:[]for i in years}
    for i in movies:
        year=i["year"]
        for (uppdate_year)in movie_dict:
            if (uppdate_year)==year:
                movie_dict[uppdate_year].append(i)
            with open("years_data_ task_2.json","w")as file1:
                json.dump(movie_dict,file1,indent=5)
    return movie_dict
group_by_decade(k)