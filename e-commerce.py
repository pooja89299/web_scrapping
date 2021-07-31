from bs4 import BeautifulSoup
import requests
import json
import pprint
def e_commerce():
    url="https://webscraper.io/test-sites"
    res=requests.get(url)
    htmlcontent=res.content
    soup=BeautifulSoup(htmlcontent,"html.parser")
    name=soup.find_all("h2")
    # list=[]
    k=[]    # position=1
    number=0
    for i in name:
        number=number+1
        site=i.find("a").get_text()
        url1=i.find("a")["href"]
        # url2="https://webscraper.io/test-sites"+url1

        dict={"Position":number,"name":site ,"link":url1}
        k.append(dict)
        with open("eccom.json","w")as file:
            json.dump(k,file,indent=7)
    return  k 
e_commerce()
















































# from bs4 import BeautifulSoup
# import requests
# import json
# import pprint
# def e_commerce():
#     url="https://webscraper.io/test-sites"
#     site_page=requests.get(url)
#     htmlcontent= site_page.content
#     soup= BeautifulSoup(htmlcontent,"html.parser")
#     print(soup)
#     main_div=soup.find_all("h2",class_="col-md-7 pull-right")
#     # return(site_page)
#     d=[]
#     srno=1
#     for i in main_div:
#         name=i.find("h2",class_="site-heading").get_text()
#         url=i.find("h2",class_="site-heading").a["href"]
#         print(url)
#         print(name)
        
#         url_1="https://webscraper.io/test-sites"+url
#         position={"title":name,"data":url_1}
#         d.append(position)
#         with open("mymy.json","w") as f:
#             json.dump(d,f,indent=4)
# e_commerce()





















    
