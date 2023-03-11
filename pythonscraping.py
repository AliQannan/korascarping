from bs4 import BeautifulSoup
import csv
import requests
from itertools import zip_longest

#pip install requests 
#pip install beautifulsoup4
#pip install lxml
page=requests.get("https://www.yallakora.com/Match-Center")
src=page.content ### html code and css and java
cham=[]
teama=[]
allteams=[]
allteamsB=[]
score=[]
#parsing
soup=BeautifulSoup(src,"lxml")
Match_delails=[]
championship=soup.find_all("div",{"class":"matchCard"})
print(championship)
allteamsA=[]
for i in range(len(championship)):
    cham.append(championship[i].find("div",{"class":"teams teamA"}).text.split())
print(cham)
print(len(cham))
allteamsa=soup.find_all("div",{"class":"teams teamA"})
for i in range(len(allteamsa)):
    allteamsA.append(allteamsa[i].text.strip())
# for al in range(len(allteamsa)):
#     if allteamsa[-1]==None:
#         allteamsa.pop(-1)
print(allteamsA)

allteamsb=soup.find_all("div",{"class":"teams teamB"})
for i in range(len(allteamsb)):
    allteamsB.append(allteamsb[i].text.strip())
print(type(allteamsB))
for nb in range(len(allteamsB)):
    with open("teamB.txt","w") as w:
        w.write("\n"+allteamsB[nb])
print(len(allteamsA))
for n in range(len(allteamsA)):
    with open("teamA.txt","w") as w:
        w.write("\n"+allteamsA[n])
print(len(allteamsA))
alllist=[allteamsA,allteamsB]
file=zip_longest(*alllist)
print(file)

newlist=[]

time=soup.find_all("div",{"class":"MResult"})
for sc in range(len(time)):
    score.append(time[sc].text.replace("\n-\n","-").strip())
for x in range(len(score)):
    str1=r"\n-\n"
  
    s="".join(score[x])
    new2=s.replace(r"\n-\n"," ")
    newlist.append(new2)
print(newlist)

# with open("reslut.csv","a") as mylist:
#     wr=csv.writer(mylist)
#     wr.writerow(refolder)

# print(score)
# for ss in range(len(score)):
#     if score[-1] == "-" :
#         score.pop(-1)


# print(score)

# print(time)



# for i in range(len(cham)):
#     teama.append(cham[i].find("li").find("div",{"class":"teams teamA"}).text)
# print(teama)

# for i in range(len(championship)):
#     cham.append(championship[i])
# print(cham)
#print(title_championship)

# print(championship)

# for x in range(len(championship)):
#     teama.append(championship[x].find("section",{"class":"mtchCntrContainer maxWidth"}).find("div",{"class":"2781 matchCard matchesList"}).find('ul').find("div",{"class":"teams teamA"}).text)

# print(teama)
# with open("teamdata.csv","w") as myfile:
#     wr=csv.writer(myfile)
#     wr.writerows(file)