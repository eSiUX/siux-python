#!/usr/bin/python
# -*- coding: utf-8 -*-

# generate date: 2015-08-24 14:45:29


class SiUXmethod:


	# --- 
	# APIKEY 

	def apikeyAdd( self,  name='', readOnly=0 ):
		" Method apikeyAdd() "
		return self._call( 'apikey.add', self._auth, name, readOnly )

	def apikeyDelete( self,  apiId=0 ):
		" Method apikeyDelete() "
		return self._call( 'apikey.delete', self._auth, apiId )

	def apikeyList( self  ):
		" Method apikeyList() "
		return self._call( 'apikey.list', self._auth )


	# --- 
	# AVAILABILITY 

	def availabilityInfo( self,  dateTo=20140101 ):
		" Method availabilityInfo() "
		return self._call( 'availability.info', self._auth, dateTo )

	def availabilityList( self,  dateInput=20140101, history=30, sourceId=0 ):
		" Method availabilityList() "
		return self._call( 'availability.list', self._auth, dateInput, history, sourceId )


	# --- 
	# BROWSER 

	def browserList( self  ):
		" Method browserList() "
		return self._call( 'browser.list', self._auth )


	# --- 
	# CHECKPOINT 

	def checkpointInfo( self,  checkpointId=0 ):
		" Method checkpointInfo() "
		return self._call( 'checkpoint.info', self._auth, checkpointId )

	def checkpointList( self,  active=-1 ):
		" Method checkpointList() "
		return self._call( 'checkpoint.list', self._auth, active )


	# --- 
	# CONTACT 

	def contactAdd( self,  name='', value='', parametr={}, contactGroup=[] ):
		" Method contactAdd() "
		return self._call( 'contact.add', self._auth, name, value, parametr, contactGroup )

	def contactDeactive( self,  value='' ):
		" Method contactDeactive() "
		return self._call( 'contact.deactive', self._auth, value )

	def contactDelete( self,  contactId=0 ):
		" Method contactDelete() "
		return self._call( 'contact.delete', self._auth, contactId )

	def contactGroupAdd( self,  name='', parametr={} ):
		" Method contactGroupAdd() "
		return self._call( 'contact.group.add', self._auth, name, parametr )

	def contactGroupDelete( self,  contactGroupId=0 ):
		" Method contactGroupDelete() "
		return self._call( 'contact.group.delete', self._auth, contactGroupId )

	def contactGroupInfo( self,  contactGroupId=0 ):
		" Method contactGroupInfo() "
		return self._call( 'contact.group.info', self._auth, contactGroupId )

	def contactGroupList( self  ):
		" Method contactGroupList() "
		return self._call( 'contact.group.list', self._auth )

	def contactInfo( self,  contactId=0 ):
		" Method contactInfo() "
		return self._call( 'contact.info', self._auth, contactId )

	def contactList( self,  status='all' ):
		" Method contactList() "
		return self._call( 'contact.list', self._auth, status )

	def contactUpdate( self,  contactId=0, parametr={}, contactGroup=[] ):
		" Method contactUpdate() "
		return self._call( 'contact.update', self._auth, contactId, parametr, contactGroup )


	# --- 
	# COUNTRY 

	def countryList( self  ):
		" Method countryList() "
		return self._call( 'country.list', self._auth )


	# --- 
	# DOMAIN 

	def domainList( self  ):
		" Method domainList() "
		return self._call( 'domain.list', self._auth )


	# --- 
	# DROPOUT 

	def dropoutInfo( self,  dateTo=20140101 ):
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
	# LANG 

	def langList( self  ):
		" Method langList() "
		return self._call( 'lang.list', self._auth )


	# --- 
	# OPERATOR 

	def operatorAdd( self,  email='', name='', surname='', passwd='', parametr={} ):
		" Method operatorAdd() "
		return self._call( 'operator.add', self._auth, email, name, surname, passwd, parametr )

	def operatorDelete( self,  operatorId=0 ):
		" Method operatorDelete() "
		return self._call( 'operator.delete', self._auth, operatorId )

	def operatorInfo( self,  operatorId=0 ):
		" Method operatorInfo() "
		return self._call( 'operator.info', self._auth, operatorId )

	def operatorList( self  ):
		" Method operatorList() "
		return self._call( 'operator.list', self._auth )

	def operatorLogList( self,  operatorId=0 ):
		" Method operatorLogList() "
		return self._call( 'operator.log.list', self._auth, operatorId )

	def operatorUpdate( self,  operatorId=0, operatorDict={} ):
		" Method operatorUpdate() "
		return self._call( 'operator.update', self._auth, operatorId, operatorDict )


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
	# SENDER 

	def senderInfo( self,  dateTo=20140101 ):
		" Method senderInfo() "
		return self._call( 'sender.info', self._auth, dateTo )


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

	def sourceDelete( self,  sourceId=0 ):
		" Method sourceDelete() "
		return self._call( 'source.delete', self._auth, sourceId )

	def sourceDropoutInfo( self,  sourceId=0, date='2008-01-01' ):
		" Method sourceDropoutInfo() "
		return self._call( 'source.dropout.info', self._auth, sourceId, date )

	def sourceDropoutList( self,  sourceId=0, history=7 ):
		" Method sourceDropoutList() "
		return self._call( 'source.dropout.list', self._auth, sourceId, history )

	def sourceGroupAdd( self,  name='', parametr={} ):
		" Method sourceGroupAdd() "
		return self._call( 'source.group.add', self._auth, name, parametr )

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

	def sourceOutputAdd( self, sourceId=0, date='2015-01-01', data=[] ):
		" Method sourceOutputAdd() "
		return self._call( 'source.output.add', self._auth, sourceId, date, data )

	def sourceOutputGroup( self,  sourceId=0, tsGroup=0 ):
		" Method sourceOutputGroup() "
		return self._call( 'source.output.group', self._auth, sourceId, tsGroup )

	def sourceOutputInfo( self,  sourceId=0, date='2008-01-01', limit=2000, FromId=0, outputId=0, countrys=[], checkpointIds=[], dataView='all' ):
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


	# --- 
	# TIMEZONE 

	def timezoneList( self  ):
		" Method timezoneList() "
		return self._call( 'timezone.list', self._auth )



methodArgs =  {'seleniumList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.list'}, 'contactGroupAdd': {'params': {'parametr': {}, 'client': '', 'name': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.add'}, 'timezoneList': {'params': {'client': ''}, 'parent': 'timezone', 'rpcMethod': 'timezone.list'}, 'senderInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'sender', 'rpcMethod': 'sender.info'}, 'seleniumTestInfo': {'params': {'seleniumTestId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.info'}, 'sourceStatMonthlyList': {'params': {'sourceId': 0, 'client': '', 'history': 12}, 'parent': 'source', 'rpcMethod': 'source.stat.monthly.list'}, 'seleniumInfo': {'params': {'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.info'}, 'availabilityInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'availability', 'rpcMethod': 'availability.info'}, 'operatorUpdate': {'params': {'client': '', 'operatorDict': {}, 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.update'}, 'sourceActive': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.active'}, 'operatorInfo': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.info'}, 'langList': {'params': {'client': ''}, 'parent': 'lang', 'rpcMethod': 'lang.list'}, 'contactInfo': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.info'}, 'sourceGroupDelete': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.delete'}, 'contactGroupList': {'params': {'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.list'}, 'contactDelete': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.delete'}, 'sourceUpdate': {'params': {'sourceId': 0, 'sourceDict': {}, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.update'}, 'sourceDeactive': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.deactive'}, 'filterInfo': {'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.info'}, 'seleniumAdd': {'params': {'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.add'}, 'domainList': {'params': {'client': ''}, 'parent': 'domain', 'rpcMethod': 'domain.list'}, 'apikeyList': {'params': {'client': ''}, 'parent': 'apikey', 'rpcMethod': 'apikey.list'}, 'sourceOutputGroup': {'params': {'sourceId': 0, 'tsGroup': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.output.group'}, 'sourceStatList': {'params': {'hostname': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.stat.list'}, 'contactDeactive': {'params': {'client': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.deactive'}, 'filterViewList': {'params': {'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.view.list'}, 'filterList': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.list'}, 'sourceList': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.list'}, 'contactUpdate': {'params': {'contactGroup': [], 'contactId': 0, 'client': '', 'parametr': {}}, 'parent': 'contact', 'rpcMethod': 'contact.update'}, 'sourceGroupList': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.group.list'}, 'operatorLogList': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.log.list'}, 'seleniumAdvancedInfo': {'params': {'client': '', 'advancedId': 0}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.info'}, 'contactGroupInfo': {'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.info'}, 'sourceOutputInfo': {'params': {'sourceId': 0, 'dataView': 'all', 'checkpointIds': [], 'outputId': 0, 'countrys': [], 'client': '', 'limit': 2000, 'date': '2008-01-01', 'FromId': 0}, 'parent': 'source', 'rpcMethod': 'source.output.info'}, 'countryList': {'params': {'client': ''}, 'parent': 'country', 'rpcMethod': 'country.list'}, 'sourceDropoutList': {'params': {'sourceId': 0, 'client': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.dropout.list'}, 'operatorAdd': {'params': {'surname': '', 'name': '', 'passwd': '', 'parametr': {}, 'client': '', 'email': ''}, 'parent': 'operator', 'rpcMethod': 'operator.add'}, 'seleniumTestList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.list'}, 'seleniumUpdate': {'params': {'status': 'active', 'seleniumId': 0, 'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.update'}, 'checkpointInfo': {'params': {'client': '', 'checkpointId': 0}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.info'}, 'contactGroupDelete': {'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.delete'}, 'operatorDelete': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.delete'}, 'availabilityList': {'params': {'sourceId': 0, 'dateInput': 20140101, 'client': '', 'history': 30}, 'parent': 'availability', 'rpcMethod': 'availability.list'}, 'filterAdd': {'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.add'}, 'browserList': {'params': {'client': ''}, 'parent': 'browser', 'rpcMethod': 'browser.list'}, 'sourceDelete': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.delete'}, 'sourceGroupAdd': {'params': {'parametr': {}, 'client': '', 'name': ''}, 'parent': 'source', 'rpcMethod': 'source.group.add'}, 'operatorList': {'params': {'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.list'}, 'sourceDropoutInfo': {'params': {'sourceId': 0, 'date': '2008-01-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.dropout.info'}, 'contactList': {'params': {'status': 'all', 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.list'}, 'seleniumAdvancedAdd': {'params': {'code': '', 'name': '', 'targetUrl': '', 'client': '', 'inputUrl': '', 'nickname': '', 'desc': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.add'}, 'sourceOutputAdd': {'params': {'sourceId': 0, 'date': '2015-01-01', 'client': '', 'data': []}, 'parent': 'source', 'rpcMethod': 'source.output.add'}, 'dropoutList': {'params': {'dateInput': 2040101, 'client': '', 'history': 7}, 'parent': 'dropout', 'rpcMethod': 'dropout.list'}, 'checkpointList': {'params': {'active': -1, 'client': ''}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.list'}, 'seleniumOutputInfo': {'params': {'date': '2015-01-01', 'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.output.info'}, 'seleniumAdvancedList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.list'}, 'filterDelete': {'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.delete'}, 'seleniumTestAdd': {'params': {'searchType': 'css_selector', 'searchValue': '', 'advancedId': 0, 'client': '', 'urlInput': '', 'urlTarget': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.add'}, 'apikeyAdd': {'params': {'readOnly': 0, 'client': '', 'name': ''}, 'parent': 'apikey', 'rpcMethod': 'apikey.add'}, 'sourceInfo': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.info'}, 'filterExist': {'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.exist'}, 'sourceAdd': {'params': {'url': '', 'client': '', 'parameter': {}, 'name': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.add'}, 'contactAdd': {'params': {'contactGroup': [], 'parametr': {}, 'client': '', 'name': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.add'}, 'apikeyDelete': {'params': {'apiId': 0, 'client': ''}, 'parent': 'apikey', 'rpcMethod': 'apikey.delete'}, 'dropoutInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'dropout', 'rpcMethod': 'dropout.info'}, 'sourceStatDailyList': {'params': {'sourceId': 0, 'date': '2001-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.stat.daily.list'}, 'sourceGroupInfo': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.info'}}
