import mailbox
import csv

fileCSV = csv.writer(open('cleanFile.csv', 'wb'))

for eachMail in mailbox.mbox('All mail Including Spam and Trash.mbox'):
	fileCSV.writerow([eachMail['subject'], eachMail['from'], eachMail['date']])

