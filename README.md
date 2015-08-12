# siux-python

Python API library (src, example)

Simple example exporting siux sources list. Source is one monitored domain. In export you can find basic information about source , last ok and error statuses.

Run example:

`# cd example`

`# vim example_source.py`
... [change YOUR_API_KEY]

`# python example_source.py`

Return values

Return value you will receive is jason structure with standardised format
for all methods.

Basic structure is
```
{
 'status': 200,
 'statusCode': 'OK',
 'statusMessage': 'OK',
 'time': 0.005663,
 'found': 1,
 'data': {
  }
}
```

What is different for each method is data parameter, that holds method specific json structure

If method returns 200 OK status there will be data section with particular result for each method.


Scenario 1 - list all your sources

In this scenario you will list all your sources in siux system.

The simpliest code to get this info is (example/example/source_list_simple.py)
```
#!/usr/bin/python
import sys
sys.path.append( '../src' )
import siuxlib
auth = '<your_api_key>'
S = siuxlib.SiUXclient( auth=auth )
retList = S.sourceList(auth)
if retList['statusCode'] == 'OK':
	for line in retList['data']:
		print line
```

For little bit more explanatory way you can look to example/example_source_list.py


Scenario 2 - add source, check source

This scenario describes basic source workflow.

1. add desired source to system
2. check source if is added correctly
3. add regular source check
4. deactivate check


1. add desired source to system
For this action there is method addSource

struct sourceAdd( name, url )


name - name of source you want to display in siux system.
url - url to be monitored
parameters - optional aditonal parameters to setup check beahaviour

Python: example/example_source_add.py
```
S = siuxlib.SiUXclient( auth = auth )
name = " your website name "
url = "www.your-website-url.com";
retValue= S.sourceAdd( name , url)
# if status code is not ok  sourceId will not be present in result
sourceId=retList['data']['sourceId']
```

2. check source
This action allows you to review setup values. At this point check is executed on regular basis according
choosen (default) time schema (every 60 seconds) .

```
S = siuxlib.SiUXclient( auth = auth )
retList = S.sourceInfo(sourceId)
```

3. add regular source check
You ca use example/example_source_check.py to check your web sites regulary as a cron script




