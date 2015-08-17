#!/usr/bin/python
"""
	Script test one particular source and his uptime from last error.
	Main purpose of script is to create check that can be automatically added to your regular system checks.
	This example uses siux lib to connect to monitored server.
"""

import  sys, pprint,time, datetime
sys.path.append( '../src' )
import siuxlib

if len(sys.argv) > 1:
	print "Usage source_uptime.py www.yoursource.com"
	sys.exit(1)

# config
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth=auth )

# make request to server
retList = S.sourceList(auth)

#print return value in case of debugging
#pprint.pprint(retList)

# current time settings
currentTimestamp = time.time()

#check response code from server
if retList['statusCode'] == 'OK':

	for line in retList['data']:

		url = line['url'].replace("http://","").replace("https://","").replace("/","")

		if sys.argv[1] == url:

			errTime = line['lastErrChecktime']
			uptimeText = " "
			# if last return value is not 200 OK
			if errTime != 0:

					retList2 = retList = S.sourceInfo(auth,line['sourceId'])

					#pprint.pprint(retList2)

					errTime2 = retList2['data']['lastErrChecktime']

					uptimeSeconds=round(currentTimestamp-errTime2)

					timeText="%s s"%uptimeSeconds

					if uptimeSeconds > 60 and uptimeSeconds < 3600:
						timeText="%s m"%(round(uptimeSeconds/60))
					elif uptimeSeconds >= 3600 and uptimeSeconds < 86400:
						timeText="%s h"%(round(uptimeSeconds/3600))
					elif uptimeSeconds >= 84000 :
						timeText="%s d"%(round(uptimeSeconds/84000))

					uptimeText2 = "%s -  %s"%(timeText,datetime.datetime.fromtimestamp(errTime2).strftime('%Y-%m-%d %H:%M:%S'))
					print (line['url'],uptimeText2)
			else:
				print (line['url'],uptimeText)