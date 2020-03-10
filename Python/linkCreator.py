import webbrowser
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'     #OS location of Chrome

links=[]									#list for playerLinks
firstName=[]								#list for player First Names
lastName=[]									#list for player Last Names

################################################################################################

roster=["Lebron James","Kyrie Irving","Kevin Love","Stephen Curry"]		#demo roster
currentName=""															#blank currentName

for x in roster:
	check=True					#checks if first or last name
	for y in x:					#goes through each letter
		if(y==" "):
			firstName.append(currentName) 				#append currentName to firstName list
			currentName=""								#wipes currentName
			check=False									#switches check to False
		else:
			currentName=currentName+y					#if not space; add letter to current name 
	lastName.append(currentName)						#append last name 
	currentName=""										#wipes currentName

################################################################################################
	
url = 'https://www.basketball-reference.com/players'	#link to open
spot=0													#increment linkCreator loop

for x in roster:
	currentFirst=firstName[spot]						#assigns first name to current first
	currentLast=lastName[spot]							#assigns last name to current last
	spot=spot+1											#increment position in roster

	player='/'+currentLast[0]+'/'+currentLast[:5]+currentFirst[:2]+'01.html'	#takes part of first and last name
	currentLink=url+player 					#combines url piece w/ player link
	links.append(currentLink.lower())		#appends current link to list of links
	
for x in links:
	webbrowser.get(chrome_path).open(x)	
	

