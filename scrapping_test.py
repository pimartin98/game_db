import os
import csv 
import requests
from bs4 import BeautifulSoup
import sqlite3



requete = requests.get("http://www.jeuxvideo.com/tous-les-jeux/")
page = requete.content
soup = BeautifulSoup(page, "html.parser")

#following code gets all the game title's from the tags <a class=".gameTitleLink__196nPy"> </a>
#see on the website


x = 1
while(x < 6): 
	url = "http://www.jeuxvideo.com/tous-les-jeux/?p="+str(x)
	requete = requests.get(url)
	page = requete.content
	soup = BeautifulSoup(page, "html.parser")
	print('Scraping page ' + str(x))

	game_list = []
	platform_list = []

	#for game_title in TABLE game 
	for game_title in soup.select(".gameTitleLink__196nPy"):
		game_list.append(game_title.text)
		print(game_title.text)


	#for platform's name (TABLE platform)
	for platform_name in soup.select(".platforms__2MTyZV.gamePlatforms__27bTXa"):
		platform_list.append(platform_name.text)
		print(platform_name.text)

	"""
	liste_game_platform = []
	for i in range(len(game_list)):
		liste_game_platform.append(game_list[i]+"$$"+platform_list[i]) 
		
	print(liste_game_platform)
	"""

	#for game's year_released (TABLE game) 
	for year_released in soup.select(".releaseDate__1RvUmc"):
		print(year_released.text)

	#don t know yet where to put the description into de DATABASES
	for description in soup.select(".description__1-Pqha"):
		print(description.text)

#get the href in tag class = "gameTitleLink..." to get jeux-nb and then the url 
#http://www.jeuxvideo.com/tous-les-jeux/jeux-nb/#details" will give the publisher of the game in	  class = ".xXx gameCharacteristicsDetailed__characValue "

#for genre's row of TABLE genre :
#same url of publisher but in class=".gameChracteristicsDetailed__characValue"

	x+=1



#----------------INSERT/SHOW DATA INTO THE DB -----------------------



#connection to the database
conn = sqlite3.connect('game_db.db')#path to the Data Base



curs = conn.cursor()


req = curs.execute('SELECT * from game')
print(req)

#print(curs.fetchall())
conn.commit()


conn.close()

