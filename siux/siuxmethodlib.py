#!/usr/bin/python
# -*- coding: utf-8 -*-

# generate date: 2015-09-11 15:20:40


class SiUXmethod:


	# --- 
	# APIKEY 

	def apikeyAdd( self,  name='', readOnly=0 ):
		" Method apikeyAdd() "
		return self._call( 'apikey.add', self._auth, name, readOnly )

	def apikeyDelete( self,  apikeyId=0 ):
		" Method apikeyDelete() "
		return self._call( 'apikey.delete', self._auth, apikeyId )

	def apikeyList( self  ):
		" Method apikeyList() "
		return self._call( 'apikey.list', self._auth )


	# --- 
	# AVAILABILITY 

	def availabilityInfo( self,  dateTo=20150901 ):
		" Method availabilityInfo() "
		return self._call( 'availability.info', self._auth, dateTo )

	def availabilityList( self,  dateInput=20150901, history=30, sourceId=0 ):
		" Method availabilityList() "
		return self._call( 'availability.list', self._auth, dateInput, history, sourceId )


	# --- 
	# CHECKPOINT 

	def checkpointInfo( self,  checkpointId=0 ):
		" Method checkpointInfo() "
		return self._call( 'checkpoint.info', self._auth, checkpointId )

	def checkpointList( self,  active=-1 ):
		" Method checkpointList() "
		return self._call( 'checkpoint.list', self._auth, active )


	# --- 
	# DROPOUT 

	def dropoutInfo( self,  dateTo=20150901 ):
		" Method dropoutInfo() "
		return self._call( 'dropout.info', self._auth, dateTo )

	def dropoutList( self,  dateInput=2040101, history=7 ):
		" Method dropoutList() "
		return self._call( 'dropout.list', self._auth, dateInput, history )


	# --- 
	# FILTER 

	def filterAdd( self,  filterData={}, sourceIds=[] ):
		" Method filterAdd() "
		return self._call( 'filter.add', self._auth, filterData, sourceIds )

	def filterDelete( self,  filterId=0 ):
		" Method filterDelete() "
		return self._call( 'filter.delete', self._auth, filterId )

	def filterExist( self,  filterData={}, sourceIds=[] ):
		" Method filterExist() "
		return self._call( 'filter.exist', self._auth, filterData, sourceIds )

	def filterInfo( self,  filterId=0 ):
		" Method filterInfo() "
		return self._call( 'filter.info', self._auth, filterId )

	def filterList( self,  sourceId=0 ):
		" Method filterList() "
		return self._call( 'filter.list', self._auth, sourceId )

	def filterViewList( self  ):
		" Method filterViewList() "
		return self._call( 'filter.view.list', self._auth )


	# --- 
	# NOTIFY 

	def notifyAdd( self,  name='', value='', parameter={}, contactGroup=[] ):
		" Method notifyAdd() "
		return self._call( 'notify.add', self._auth, name, value, parameter, contactGroup )

	def notifyDeactive( self,  value='' ):
		" Method notifyDeactive() "
		return self._call( 'notify.deactive', self._auth, value )

	def notifyDelete( self,  contactId=0 ):
		" Method notifyDelete() "
		return self._call( 'notify.delete', self._auth, contactId )

	def notifyGroupAdd( self,  name='', parameter={} ):
		" Method notifyGroupAdd() "
		return self._call( 'notify.group.add', self._auth, name, parameter )

	def notifyGroupDelete( self,  contactGroupId=0 ):
		" Method notifyGroupDelete() "
		return self._call( 'notify.group.delete', self._auth, contactGroupId )

	def notifyGroupInfo( self,  contactGroupId=0 ):
		" Method notifyGroupInfo() "
		return self._call( 'notify.group.info', self._auth, contactGroupId )

	def notifyGroupList( self  ):
		" Method notifyGroupList() "
		return self._call( 'notify.group.list', self._auth )

	def notifyInfo( self,  contactId=0 ):
		" Method notifyInfo() "
		return self._call( 'notify.info', self._auth, contactId )

	def notifyList( self,  status='all' ):
		" Method notifyList() "
		return self._call( 'notify.list', self._auth, status )

	def notifySenderInfo( self,  dateTo=20150101 ):
		" Method notifySenderInfo() "
		return self._call( 'notify.sender.info', self._auth, dateTo )

	def notifyUpdate( self,  contactId=0, parameter={}, contactGroup=[] ):
		" Method notifyUpdate() "
		return self._call( 'notify.update', self._auth, contactId, parameter, contactGroup )


	# --- 
	# OPERATOR 

	def operatorInfo( self,  operatorId=0 ):
		" Method operatorInfo() "
		return self._call( 'operator.info', self._auth, operatorId )

	def operatorList( self  ):
		" Method operatorList() "
		return self._call( 'operator.list', self._auth )

	def operatorLogList( self,  operatorId=0 ):
		" Method operatorLogList() "
		return self._call( 'operator.log.list', self._auth, operatorId )


	# --- 
	# SELENIUM 

	def seleniumAdd( self,  name='', browser='chromelin', timeout=30, testType='content', testIds=[], paramJS=1, paramScreen='' ):
		" Method seleniumAdd() "
		return self._call( 'selenium.add', self._auth, name, browser, timeout, testType, testIds, paramJS, paramScreen )

	def seleniumAdvancedAdd( self,  name='', desc='', code='', nickname='', inputUrl='', targetUrl='' ):
		" Method seleniumAdvancedAdd() "
		return self._call( 'selenium.advanced.add', self._auth, name, desc, code, nickname, inputUrl, targetUrl )

	def seleniumAdvancedInfo( self,  advancedId=0 ):
		" Method seleniumAdvancedInfo() "
		return self._call( 'selenium.advanced.info', self._auth, advancedId )

	def seleniumAdvancedList( self  ):
		" Method seleniumAdvancedList() "
		return self._call( 'selenium.advanced.list', self._auth )

	def seleniumInfo( self,  seleniumId=0 ):
		" Method seleniumInfo() "
		return self._call( 'selenium.info', self._auth, seleniumId )

	def seleniumList( self  ):
		" Method seleniumList() "
		return self._call( 'selenium.list', self._auth )

	def seleniumOutputInfo( self,  seleniumId=0, date='2015-01-01' ):
		" Method seleniumOutputInfo() "
		return self._call( 'selenium.output.info', self._auth, seleniumId, date )

	def seleniumTestAdd( self,  urlInput='', searchType='css_selector', searchValue='', urlTarget='', advancedId=0 ):
		" Method seleniumTestAdd() "
		return self._call( 'selenium.test.add', self._auth, urlInput, searchType, searchValue, urlTarget, advancedId )

	def seleniumTestInfo( self,  seleniumTestId=0 ):
		" Method seleniumTestInfo() "
		return self._call( 'selenium.test.info', self._auth, seleniumTestId )

	def seleniumTestList( self  ):
		" Method seleniumTestList() "
		return self._call( 'selenium.test.list', self._auth )

	def seleniumUpdate( self,  seleniumId=0, name='', browser='chromelin', timeout=30, testType='content', testIds=[], status='active', paramJS=1, paramScreen='' ):
		" Method seleniumUpdate() "
		return self._call( 'selenium.update', self._auth, seleniumId, name, browser, timeout, testType, testIds, status, paramJS, paramScreen )


	# --- 
	# SOURCE 

	def sourceActive( self,  sourceId=0 ):
		" Method sourceActive() "
		return self._call( 'source.active', self._auth, sourceId )

	def sourceAdd( self,  sourceGroupId=0, name='', url='', parameter={} ):
		" Method sourceAdd() "
		return self._call( 'source.add', self._auth, sourceGroupId, name, url, parameter )

	def sourceDeactive( self,  sourceId=0 ):
		" Method sourceDeactive() "
		return self._call( 'source.deactive', self._auth, sourceId )

	def sourceDropoutInfo( self,  sourceId=0, date='2015-09-01' ):
		" Method sourceDropoutInfo() "
		return self._call( 'source.dropout.info', self._auth, sourceId, date )

	def sourceDropoutList( self,  sourceId=0, history=7 ):
		" Method sourceDropoutList() "
		return self._call( 'source.dropout.list', self._auth, sourceId, history )

	def sourceGroupAdd( self,  name='', parameter={} ):
		" Method sourceGroupAdd() "
		return self._call( 'source.group.add', self._auth, name, parameter )

	def sourceGroupDelete( self,  sourceGroupId=0 ):
		" Method sourceGroupDelete() "
		return self._call( 'source.group.delete', self._auth, sourceGroupId )

	def sourceGroupInfo( self,  sourceGroupId=0 ):
		" Method sourceGroupInfo() "
		return self._call( 'source.group.info', self._auth, sourceGroupId )

	def sourceGroupList( self  ):
		" Method sourceGroupList() "
		return self._call( 'source.group.list', self._auth )

	def sourceInfo( self,  sourceId=0 ):
		" Method sourceInfo() "
		return self._call( 'source.info', self._auth, sourceId )

	def sourceList( self,  sourceGroupId=0 ):
		" Method sourceList() "
		return self._call( 'source.list', self._auth, sourceGroupId )

	def sourceOutputGroup( self,  sourceId=0, tsGroup=0 ):
		" Method sourceOutputGroup() "
		return self._call( 'source.output.group', self._auth, sourceId, tsGroup )

	def sourceOutputInfo( self,  sourceId=0, date='2015-09-01', limit=2000, FromId=0, outputId=0, countrys=[], checkpointIds=[], dataView='all' ):
		" Method sourceOutputInfo() "
		return self._call( 'source.output.info', self._auth, sourceId, date, limit, FromId, outputId, countrys, checkpointIds, dataView )

	def sourceStatDailyList( self,  sourceId=0, date='2001-01' ):
		" Method sourceStatDailyList() "
		return self._call( 'source.stat.daily.list', self._auth, sourceId, date )

	def sourceStatList( self, hostname, history=7 ):
		" Method sourceStatList() "
		return self._call( 'source.stat.list', hostname, history )

	def sourceStatMonthlyList( self,  sourceId=0, history=12 ):
		" Method sourceStatMonthlyList() "
		return self._call( 'source.stat.monthly.list', self._auth, sourceId, history )

	def sourceUpdate( self,  sourceId=0, sourceDict={} ):
		" Method sourceUpdate() "
		return self._call( 'source.update', self._auth, sourceId, sourceDict )



methodArgs =  {'seleniumList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.list'}, 'notifyGroupList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.list'}, 'notifyGroupDelete': {'paramArr': ['client', 'contactGroupId'], 'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.delete'}, 'notifyAdd': {'paramArr': ['client', 'name', 'value', 'parameter', 'contactGroup'], 'params': {'contactGroup': [], 'client': '', 'parameter': {}, 'name': '', 'value': ''}, 'parent': 'notify', 'rpcMethod': 'notify.add'}, 'sourceStatMonthlyList': {'paramArr': ['client', 'sourceId', 'history'], 'params': {'sourceId': 0, 'client': '', 'history': 12}, 'parent': 'source', 'rpcMethod': 'source.stat.monthly.list'}, 'notifyGroupInfo': {'paramArr': ['client', 'contactGroupId'], 'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.info'}, 'seleniumInfo': {'paramArr': ['client', 'seleniumId'], 'params': {'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.info'}, 'availabilityInfo': {'paramArr': ['client', 'dateTo'], 'params': {'dateTo': 20150901, 'client': ''}, 'parent': 'availability', 'rpcMethod': 'availability.info'}, 'sourceDropoutList': {'paramArr': ['client', 'sourceId', 'history'], 'params': {'sourceId': 0, 'client': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.dropout.list'}, 'operatorInfo': {'paramArr': ['client', 'operatorId'], 'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.info'}, 'sourceActive': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.active'}, 'sourceStatDailyList': {'paramArr': ['client', 'sourceId', 'date'], 'params': {'sourceId': 0, 'date': '2001-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.stat.daily.list'}, 'sourceGroupDelete': {'paramArr': ['client', 'sourceGroupId'], 'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.delete'}, 'sourceUpdate': {'paramArr': ['client', 'sourceId', 'sourceDict'], 'params': {'sourceId': 0, 'sourceDict': {}, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.update'}, 'sourceDeactive': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.deactive'}, 'filterInfo': {'paramArr': ['client', 'filterId'], 'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.info'}, 'seleniumTestAdd': {'paramArr': ['client', 'urlInput', 'searchType', 'searchValue', 'urlTarget', 'advancedId'], 'params': {'searchType': 'css_selector', 'searchValue': '', 'advancedId': 0, 'client': '', 'urlInput': '', 'urlTarget': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.add'}, 'apikeyList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'apikey', 'rpcMethod': 'apikey.list'}, 'sourceOutputGroup': {'paramArr': ['client', 'sourceId', 'tsGroup'], 'params': {'sourceId': 0, 'tsGroup': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.output.group'}, 'sourceStatList': {'paramArr': ['hostname', 'history'], 'params': {'hostname': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.stat.list'}, 'seleniumTestInfo': {'paramArr': ['client', 'seleniumTestId'], 'params': {'seleniumTestId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.info'}, 'sourceList': {'paramArr': ['client', 'sourceGroupId'], 'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.list'}, 'filterViewList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.view.list'}, 'filterList': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.list'}, 'notifyInfo': {'paramArr': ['client', 'contactId'], 'params': {'contactId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.info'}, 'sourceGroupList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.group.list'}, 'operatorLogList': {'paramArr': ['client', 'operatorId'], 'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.log.list'}, 'seleniumAdvancedInfo': {'paramArr': ['client', 'advancedId'], 'params': {'client': '', 'advancedId': 0}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.info'}, 'sourceOutputInfo': {'paramArr': ['client', 'sourceId', 'date', 'limit', 'FromId', 'outputId', 'countrys', 'checkpointIds', 'dataView'], 'params': {'sourceId': 0, 'dataView': 'all', 'checkpointIds': [], 'outputId': 0, 'countrys': [], 'client': '', 'limit': 2000, 'date': '2015-09-01', 'FromId': 0}, 'parent': 'source', 'rpcMethod': 'source.output.info'}, 'seleniumTestList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.list'}, 'seleniumUpdate': {'paramArr': ['client', 'seleniumId', 'name', 'browser', 'timeout', 'testType', 'testIds', 'status', 'paramJS', 'paramScreen'], 'params': {'status': 'active', 'seleniumId': 0, 'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.update'}, 'checkpointInfo': {'paramArr': ['client', 'checkpointId'], 'params': {'client': '', 'checkpointId': 0}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.info'}, 'seleniumAdd': {'paramArr': ['client', 'name', 'browser', 'timeout', 'testType', 'testIds', 'paramJS', 'paramScreen'], 'params': {'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.add'}, 'availabilityList': {'paramArr': ['client', 'dateInput', 'history', 'sourceId'], 'params': {'sourceId': 0, 'dateInput': 20150901, 'client': '', 'history': 30}, 'parent': 'availability', 'rpcMethod': 'availability.list'}, 'filterAdd': {'paramArr': ['client', 'filterData', 'sourceIds'], 'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.add'}, 'notifyList': {'paramArr': ['client', 'status'], 'params': {'status': 'all', 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.list'}, 'sourceGroupAdd': {'paramArr': ['client', 'name', 'parameter'], 'params': {'client': '', 'parameter': {}, 'name': ''}, 'parent': 'source', 'rpcMethod': 'source.group.add'}, 'operatorList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.list'}, 'sourceDropoutInfo': {'paramArr': ['client', 'sourceId', 'date'], 'params': {'sourceId': 0, 'date': '2015-09-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.dropout.info'}, 'seleniumAdvancedAdd': {'paramArr': ['client', 'name', 'desc', 'code', 'nickname', 'inputUrl', 'targetUrl'], 'params': {'code': '', 'name': '', 'targetUrl': '', 'client': '', 'inputUrl': '', 'nickname': '', 'desc': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.add'}, 'dropoutList': {'paramArr': ['client', 'dateInput', 'history'], 'params': {'dateInput': 2040101, 'client': '', 'history': 7}, 'parent': 'dropout', 'rpcMethod': 'dropout.list'}, 'notifyGroupAdd': {'paramArr': ['client', 'name', 'parameter'], 'params': {'client': '', 'parameter': {}, 'name': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.add'}, 'checkpointList': {'paramArr': ['client', 'active'], 'params': {'active': -1, 'client': ''}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.list'}, 'seleniumOutputInfo': {'paramArr': ['client', 'seleniumId', 'date'], 'params': {'date': '2015-01-01', 'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.output.info'}, 'seleniumAdvancedList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.list'}, 'filterDelete': {'paramArr': ['client', 'filterId'], 'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.delete'}, 'notifyUpdate': {'paramArr': ['client', 'contactId', 'parameter', 'contactGroup'], 'params': {'contactGroup': [], 'contactId': 0, 'client': '', 'parameter': {}}, 'parent': 'notify', 'rpcMethod': 'notify.update'}, 'apikeyAdd': {'paramArr': ['client', 'name', 'readOnly'], 'params': {'readOnly': 0, 'client': '', 'name': ''}, 'parent': 'apikey', 'rpcMethod': 'apikey.add'}, 'sourceInfo': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.info'}, 'filterExist': {'paramArr': ['client', 'filterData', 'sourceIds'], 'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.exist'}, 'sourceAdd': {'paramArr': ['client', 'sourceGroupId', 'name', 'url', 'parameter'], 'params': {'url': '', 'client': '', 'parameter': {}, 'name': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.add'}, 'notifyDelete': {'paramArr': ['client', 'contactId'], 'params': {'contactId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.delete'}, 'apikeyDelete': {'paramArr': ['client', 'apikeyId'], 'params': {'client': '', 'apikeyId': 0}, 'parent': 'apikey', 'rpcMethod': 'apikey.delete'}, 'dropoutInfo': {'paramArr': ['client', 'dateTo'], 'params': {'dateTo': 20150901, 'client': ''}, 'parent': 'dropout', 'rpcMethod': 'dropout.info'}, 'notifySenderInfo': {'paramArr': ['client', 'dateTo'], 'params': {'dateTo': 20150101, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.sender.info'}, 'notifyDeactive': {'paramArr': ['client', 'value'], 'params': {'client': '', 'value': ''}, 'parent': 'notify', 'rpcMethod': 'notify.deactive'}, 'sourceGroupInfo': {'paramArr': ['client', 'sourceGroupId'], 'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.info'}}
