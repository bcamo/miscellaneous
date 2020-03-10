#!/bin/bash
import webbrowser #import web browser function

googleCalendar= "https://calendar.google.com"
googleMail= "https://mail.google.com"
helpdesk= "https://trunkclub.freshservice.com/helpdesk/tickets"
sysOpsPriorities= "https://paper.dropbox.com/doc/SysOps-Sprint-Priorities-ongoing--AgnO5Qd1hnGnjPABsnAWKIeDAg-da48cqHGDjs8BX6lf5cTM"
myJiraCards= "https://jira.trunkclub.com/issues/?filter=-1"


listOfSites=[googleMail, googleCalendar, myJiraCards, helpdesk, sysOpsPriorities, ]

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

for x in listOfSites:
	webbrowser.get(chrome_path).open(x)
	