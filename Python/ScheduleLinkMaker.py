#!/usr/bin/env python
import datetime				#import datetime 
import webbrowser			#import web browser 
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'     #OS location of Chrome

today = datetime.datetime.now()		#stores current date in today variable
year=str(today.year)				#puts current year in string format
month=str(today.month)				#puts current month in string format
day=str(today.day)					#puts current day in string format
	
if(month=="2"):						##checks if feb to adjust end date
	if(today.day+7<28):
		print(today.day+7)
		lastDay=str(today.day+7)
	else:
		lastDay="28"
elif(month=="4" or month=="6" or month=="9" or month=="11"):  ##checks if month has 30 days to adjust end date
	if(today.day+7<30):
		lastDay=str(today.day+7)
	else:
		lastDay="30"
else:									##checks if month has 31 days to adjust end date
	if(today.day+7<31):
		print(today.day+7)
		lastDay=str(today.day+7)
	else:
		lastDay="31"


################################################################################################################
###Schedule template
###Our schedule has our timezone, NY Clubhouse stylists, basic link for adjusting
#g=Group ID; the team that will be in the report
#t=timezone; used when showing schedule

DailySchedule="https://community.trunkclub.systems/CommunityWeb/UI/Schedule/PublishSchedule/Reports/AgentPublishedScheduleByUserGroup.aspx?g=67&t=35&e=&o=5&c=0&n=1&fd="+year+"%2f"+month+"%2f"+day+"&td="+year+"%2f"+month+"%2f"+lastDay+"&m=0&sn=15" 

###Use current date to create link from today to 7 days out or end of the month
################################################################################################################


print(DailySchedule)							##print link for schedule for today through 7 days out
webbrowser.get(chrome_path).open(DailySchedule)	##open chrome with schedule for the day
