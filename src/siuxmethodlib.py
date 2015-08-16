#!/usr/bin/python
# -*- coding: utf-8 -*-

# generate date: 2015-57-16 10:57:50


class SiUXmethod:

	def availabilityInfo( self,  dateTo=20140101 ):
		return self._call( 'availability.info', self._auth, dateTo )

	def availabilityList( self,  dateInput=20140101, history=30, sourceId=0 ):
		return self._call( 'availability.list', self._auth, dateInput, history, sourceId )

	def browserList( self,  ):
		return self._call( 'browser.list', self._auth )

	def checkpointInfo( self,  checkpointId=0 ):
		return self._call( 'checkpoint.info', self._auth, checkpointId )

	def checkpointList( self,  active=-1 ):
		return self._call( 'checkpoint.list', self._auth, active )

	def clientUpdate( self,  clientDict={} ):
		return self._call( 'client.update', self._auth, clientDict )

	def contactActive( self,  value='' ):
		return self._call( 'contact.active', self._auth, value )

	def contactAdd( self,  name='', value='', parametr={}, contactGroup=[] ):
		return self._call( 'contact.add', self._auth, name, value, parametr, contactGroup )

	def contactCheckSend( self,  contactId=0, text='' ):
		return self._call( 'contact.check.send', self._auth, contactId, text )

	def contactCheckSet( self,  contactId=0 ):
		return self._call( 'contact.check.set', self._auth, contactId )

	def contactDeactive( self,  value='' ):
		return self._call( 'contact.deactive', self._auth, value )

	def contactDelete( self,  contactId=0 ):
		return self._call( 'contact.delete', self._auth, contactId )

	def contactGroupAdd( self,  name='', parametr={} ):
		return self._call( 'contact.group.add', self._auth, name, parametr )

	def contactGroupDelete( self,  contactGroupId=0 ):
		return self._call( 'contact.group.delete', self._auth, contactGroupId )

	def contactGroupInfo( self,  contactGroupId=0 ):
		return self._call( 'contact.group.info', self._auth, contactGroupId )

	def contactGroupList( self,  ):
		return self._call( 'contact.group.list', self._auth )

	def contactInfo( self,  contactId=0 ):
		return self._call( 'contact.info', self._auth, contactId )

	def contactLinkAdd( self,  contactId=0, contactGroupId=0 ):
		return self._call( 'contact.link.add', self._auth, contactId, contactGroupId )

	def contactLinkDelete( self,  contactId=0, contactGroupId=0 ):
		return self._call( 'contact.link.delete', self._auth, contactId, contactGroupId )

	def contactList( self,  status='all' ):
		return self._call( 'contact.list', self._auth, status )

	def contactTypeList( self,  ):
		return self._call( 'contact.type.list', self._auth )

	def contactUpdate( self,  contactId=0, parametr={}, contactGroup=[] ):
		return self._call( 'contact.update', self._auth, contactId, parametr, contactGroup )

	def countryList( self,  ):
		return self._call( 'country.list', self._auth )

	def dailyInfo( self,  dateTo=20140101 ):
		return self._call( 'daily.info', self._auth, dateTo )

	def domainList( self,  ):
		return self._call( 'domain.list', self._auth )

	def dropoutInfo( self,  dateTo=20140101 ):
		return self._call( 'dropout.info', self._auth, dateTo )

	def dropoutList( self,  dateInput=2040101, history=7 ):
		return self._call( 'dropout.list', self._auth, dateInput, history )

	def filterAdd( self,  filterData={}, sourceIds=[] ):
		return self._call( 'filter.add', self._auth, filterData, sourceIds )

	def filterDelete( self,  filterId=0 ):
		return self._call( 'filter.delete', self._auth, filterId )

	def filterExist( self,  filterData={}, sourceIds=[] ):
		return self._call( 'filter.exist', self._auth, filterData, sourceIds )

	def filterInfo( self,  filterId=0 ):
		return self._call( 'filter.info', self._auth, filterId )

	def filterList( self,  sourceId=0 ):
		return self._call( 'filter.list', self._auth, sourceId )

	def filterViewList( self,  ):
		return self._call( 'filter.view.list', self._auth )

	def langList( self,  ):
		return self._call( 'lang.list', self._auth )

	def maintenanceAdd( self,  maintenanceDict={}, sources=[] ):
		return self._call( 'maintenance.add', self._auth, maintenanceDict, sources )

	def maintenanceInfo( self,  maintenanceId=0 ):
		return self._call( 'maintenance.info', self._auth, maintenanceId )

	def maintenanceList( self,  ):
		return self._call( 'maintenance.list', self._auth )

	def maintenanceUpdate( self,  maintenanceId=0, maintenanceDict={}, sources=[] ):
		return self._call( 'maintenance.update', self._auth, maintenanceId, maintenanceDict, sources )

	def operatorAdd( self,  email='', name='', surname='', passwd='', parametr={} ):
		return self._call( 'operator.add', self._auth, email, name, surname, passwd, parametr )

	def operatorAuth( self,  session='' ):
		return self._call( 'operator.auth', self._auth, session )

	def operatorDelete( self,  operatorId=0 ):
		return self._call( 'operator.delete', self._auth, operatorId )

	def operatorInfo( self,  operatorId=0 ):
		return self._call( 'operator.info', self._auth, operatorId )

	def operatorList( self,  ):
		return self._call( 'operator.list', self._auth )

	def operatorLogList( self,  operatorId=0 ):
		return self._call( 'operator.log.list', self._auth, operatorId )

	def operatorLogin( self,  login='', passwd='' ):
		return self._call( 'operator.login', self._auth, login, passwd )

	def operatorLogout( self,  session='' ):
		return self._call( 'operator.logout', self._auth, session )

	def operatorUpdate( self,  operatorId=0, operatorDict={} ):
		return self._call( 'operator.update', self._auth, operatorId, operatorDict )

	def seleniumAdd( self,  name='', browser='chromelin', timeout=30, testType='content', testIds=[], paramJS=1, paramScreen='' ):
		return self._call( 'selenium.add', self._auth, name, browser, timeout, testType, testIds, paramJS, paramScreen )

	def seleniumAdvancedAdd( self,  name='', desc='', code='', nickname='', inputUrl='', targetUrl='' ):
		return self._call( 'selenium.advanced.add', self._auth, name, desc, code, nickname, inputUrl, targetUrl )

	def seleniumAdvancedInfo( self,  advancedId=0 ):
		return self._call( 'selenium.advanced.info', self._auth, advancedId )

	def seleniumAdvancedList( self,  ):
		return self._call( 'selenium.advanced.list', self._auth )

	def seleniumInfo( self,  seleniumId=0 ):
		return self._call( 'selenium.info', self._auth, seleniumId )

	def seleniumList( self,  ):
		return self._call( 'selenium.list', self._auth )

	def seleniumOutputInfo( self,  seleniumId=0, date='2015-01-01' ):
		return self._call( 'selenium.output.info', self._auth, seleniumId, date )

	def seleniumTestAdd( self,  urlInput='', searchType='css_selector', searchValue='', urlTarget='', advancedId=0 ):
		return self._call( 'selenium.test.add', self._auth, urlInput, searchType, searchValue, urlTarget, advancedId )

	def seleniumTestInfo( self,  seleniumTestId=0 ):
		return self._call( 'selenium.test.info', self._auth, seleniumTestId )

	def seleniumTestList( self,  ):
		return self._call( 'selenium.test.list', self._auth )

	def seleniumUpdate( self,  seleniumId=0, name='', browser='chromelin', timeout=30, testType='content', testIds=[], status='active', paramJS=1, paramScreen='' ):
		return self._call( 'selenium.update', self._auth, seleniumId, name, browser, timeout, testType, testIds, status, paramJS, paramScreen )

	def senderInfo( self,  dateTo=20140101 ):
		return self._call( 'sender.info', self._auth, dateTo )

	def sourceActive( self,  sourceId=0 ):
		return self._call( 'source.active', self._auth, sourceId )

	def sourceAdd( self,  sourceGroupId=0, name='', url='', parameter={} ):
		return self._call( 'source.add', self._auth, sourceGroupId, name, url, parameter )

	def sourceAllActive( self,  ):
		return self._call( 'source.all.active', self._auth )

	def sourceAllDeactive( self,  ):
		return self._call( 'source.all.deactive', self._auth )

	def sourceCheckqueueInfo( self,  sourceId=0, date='2008-01-01', limit=2000, FromId=0, countrys=[], checkpointIds=[] ):
		return self._call( 'source.checkqueue.info', self._auth, sourceId, date, limit, FromId, countrys, checkpointIds )

	def sourceDeactive( self,  sourceId=0 ):
		return self._call( 'source.deactive', self._auth, sourceId )

	def sourceDelete( self,  sourceId=0 ):
		return self._call( 'source.delete', self._auth, sourceId )

	def sourceDomainList( self,  ):
		return self._call( 'source.domain.list', self._auth )

	def sourceDropoutInfo( self,  sourceId=0, date='2008-01-01' ):
		return self._call( 'source.dropout.info', self._auth, sourceId, date )

	def sourceDropoutList( self,  sourceId=0, history=7 ):
		return self._call( 'source.dropout.list', self._auth, sourceId, history )

	def sourceGroupAdd( self,  name='', parametr={} ):
		return self._call( 'source.group.add', self._auth, name, parametr )

	def sourceGroupDelete( self,  sourceGroupId=0 ):
		return self._call( 'source.group.delete', self._auth, sourceGroupId )

	def sourceGroupInfo( self,  sourceGroupId=0 ):
		return self._call( 'source.group.info', self._auth, sourceGroupId )

	def sourceGroupList( self,  ):
		return self._call( 'source.group.list', self._auth )

	def sourceGroupSet( self,  sourceGroupId=0, contactGroupIds=[] ):
		return self._call( 'source.group.set', self._auth, sourceGroupId, contactGroupIds )

	def sourceInfo( self,  sourceId=0 ):
		return self._call( 'source.info', self._auth, sourceId )

	def sourceList( self,  sourceGroupId=0 ):
		return self._call( 'source.list', self._auth, sourceGroupId )

	def sourceOutputAdd( self, sourceId=0, date='2015-01-01', data=[] ):
		return self._call( 'source.output.add', self._auth, sourceId, date, data )

	def sourceOutputGroup( self,  sourceId=0, tsGroup=0 ):
		return self._call( 'source.output.group', self._auth, sourceId, tsGroup )

	def sourceOutputInfo( self,  sourceId=0, date='2008-01-01', limit=2000, FromId=0, outputId=0, countrys=[], checkpointIds=[], dataView='all' ):
		return self._call( 'source.output.info', self._auth, sourceId, date, limit, FromId, outputId, countrys, checkpointIds, dataView )

	def sourceStatDailyList( self,  sourceId=0, date='2001-01' ):
		return self._call( 'source.stat.daily.list', self._auth, sourceId, date )

	def sourceStatList( self, hostname, history=7 ):
		return self._call( 'source.stat.list', hostname, history )

	def sourceStatMonthlyList( self,  sourceId=0, history=12 ):
		return self._call( 'source.stat.monthly.list', self._auth, sourceId, history )

	def sourceTypeList( self,  ):
		return self._call( 'source.type.list', self._auth )

	def sourceTypeValue( self,  ):
		return self._call( 'source.type.value', self._auth )

	def sourceUpdate( self,  sourceId=0, sourceDict={} ):
		return self._call( 'source.update', self._auth, sourceId, sourceDict )

	def testFilterList( self,  ):
		return self._call( 'test.filter.list', self._auth )

	def testStatusList( self,  ):
		return self._call( 'test.status.list', self._auth )

	def testValueList( self,  sourceGroupId=0 ):
		return self._call( 'test.value.list', self._auth, sourceGroupId )

	def timePlanList( self,  ):
		return self._call( 'time.plan.list', self._auth )

	def timeSchemeInfo( self,  timeSchemeId=0 ):
		return self._call( 'time.scheme.info', self._auth, timeSchemeId )

	def timeSchemeList( self,  ):
		return self._call( 'time.scheme.list', self._auth )

	def timezoneList( self,  ):
		return self._call( 'timezone.list', self._auth )



methodArgs =  {'operatorLogin': {'params': {'passwd': '', 'login': '', 'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.login'}, 'contactDeactive': {'params': {'client': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.deactive'}, 'contactTypeList': {'params': {'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.type.list'}, 'availabilityInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'availability', 'rpcMethod': 'availability.info'}, 'operatorUpdate': {'params': {'client': '', 'operatorDict': {}, 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.update'}, 'sourceGroupDelete': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.delete'}, 'contactGroupList': {'params': {'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.list'}, 'contactDelete': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.delete'}, 'sourceDeactive': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.deactive'}, 'filterInfo': {'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.info'}, 'domainList': {'params': {'client': ''}, 'parent': 'domain', 'rpcMethod': 'domain.list'}, 'contactActive': {'params': {'client': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.active'}, 'sourceStatList': {'params': {'hostname': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.stat.list'}, 'filterViewList': {'params': {'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.view.list'}, 'sourceGroupList': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.group.list'}, 'operatorAuth': {'params': {'session': '', 'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.auth'}, 'contactCheckSet': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.check.set'}, 'seleniumUpdate': {'params': {'status': 'active', 'seleniumId': 0, 'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.update'}, 'operatorLogout': {'params': {'session': '', 'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.logout'}, 'testFilterList': {'params': {'client': ''}, 'parent': 'test', 'rpcMethod': 'test.filter.list'}, 'seleniumAdvancedList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.list'}, 'sourceAllDeactive': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.all.deactive'}, 'sourceTypeList': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.type.list'}, 'contactCheckSend': {'params': {'text': '', 'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.check.send'}, 'timeSchemeList': {'params': {'client': ''}, 'parent': 'time', 'rpcMethod': 'time.scheme.list'}, 'maintenanceUpdate': {'params': {'sources': [], 'maintenanceDict': {}, 'client': '', 'maintenanceId': 0}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.update'}, 'checkpointInfo': {'params': {'client': '', 'checkpointId': 0}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.info'}, 'sourceCheckqueueInfo': {'params': {'sourceId': 0, 'checkpointIds': [], 'countrys': [], 'client': '', 'limit': 2000, 'date': '2008-01-01', 'FromId': 0}, 'parent': 'source', 'rpcMethod': 'source.checkqueue.info'}, 'seleniumTestInfo': {'params': {'seleniumTestId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.info'}, 'maintenanceInfo': {'params': {'client': '', 'maintenanceId': 0}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.info'}, 'sourceUpdate': {'params': {'sourceId': 0, 'sourceDict': {}, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.update'}, 'sourceList': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.list'}, 'operatorLogList': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.log.list'}, 'maintenanceAdd': {'params': {'sources': [], 'maintenanceDict': {}, 'client': ''}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.add'}, 'countryList': {'params': {'client': ''}, 'parent': 'country', 'rpcMethod': 'country.list'}, 'seleniumTestList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.list'}, 'sourceGroupSet': {'params': {'client': '', 'contactGroupIds': [], 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.set'}, 'langList': {'params': {'client': ''}, 'parent': 'lang', 'rpcMethod': 'lang.list'}, 'seleniumAdd': {'params': {'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.add'}, 'operatorAdd': {'params': {'surname': '', 'name': '', 'passwd': '', 'parametr': {}, 'client': '', 'email': ''}, 'parent': 'operator', 'rpcMethod': 'operator.add'}, 'sourceDelete': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.delete'}, 'sourceDropoutList': {'params': {'sourceId': 0, 'client': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.dropout.list'}, 'seleniumOutputInfo': {'params': {'date': '2015-01-01', 'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.output.info'}, 'seleniumTestAdd': {'params': {'searchType': 'css_selector', 'searchValue': '', 'advancedId': 0, 'client': '', 'urlInput': '', 'urlTarget': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.add'}, 'testValueList': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'test', 'rpcMethod': 'test.value.list'}, 'filterExist': {'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.exist'}, 'sourceAllActive': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.all.active'}, 'seleniumList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.list'}, 'senderInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'sender', 'rpcMethod': 'sender.info'}, 'sourceStatMonthlyList': {'params': {'sourceId': 0, 'client': '', 'history': 12}, 'parent': 'source', 'rpcMethod': 'source.stat.monthly.list'}, 'sourceActive': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.active'}, 'sourceStatDailyList': {'params': {'sourceId': 0, 'date': '2001-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.stat.daily.list'}, 'testStatusList': {'params': {'client': ''}, 'parent': 'test', 'rpcMethod': 'test.status.list'}, 'contactLinkAdd': {'params': {'contactGroupId': 0, 'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.link.add'}, 'seleniumAdvancedAdd': {'params': {'code': '', 'name': '', 'targetUrl': '', 'client': '', 'inputUrl': '', 'nickname': '', 'desc': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.add'}, 'filterList': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.list'}, 'seleniumAdvancedInfo': {'params': {'client': '', 'advancedId': 0}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.info'}, 'sourceOutputInfo': {'params': {'sourceId': 0, 'dataView': 'all', 'checkpointIds': [], 'outputId': 0, 'countrys': [], 'client': '', 'limit': 2000, 'date': '2008-01-01', 'FromId': 0}, 'parent': 'source', 'rpcMethod': 'source.output.info'}, 'clientUpdate': {'params': {'client': '', 'clientDict': {}}, 'parent': 'client', 'rpcMethod': 'client.update'}, 'contactGroupInfo': {'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.info'}, 'filterAdd': {'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.add'}, 'contactLinkDelete': {'params': {'contactGroupId': 0, 'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.link.delete'}, 'sourceDropoutInfo': {'params': {'sourceId': 0, 'date': '2008-01-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.dropout.info'}, 'contactList': {'params': {'status': 'all', 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.list'}, 'filterDelete': {'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.delete'}, 'sourceInfo': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.info'}, 'sourceAdd': {'params': {'url': '', 'client': '', 'parameter': {}, 'name': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.add'}, 'contactAdd': {'params': {'contactGroup': [], 'parametr': {}, 'client': '', 'name': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.add'}, 'dropoutInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'dropout', 'rpcMethod': 'dropout.info'}, 'sourceGroupInfo': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.info'}, 'contactGroupAdd': {'params': {'parametr': {}, 'client': '', 'name': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.add'}, 'maintenanceList': {'params': {'client': ''}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.list'}, 'seleniumInfo': {'params': {'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.info'}, 'operatorInfo': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.info'}, 'timePlanList': {'params': {'client': ''}, 'parent': 'time', 'rpcMethod': 'time.plan.list'}, 'contactInfo': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.info'}, 'sourceOutputGroup': {'params': {'sourceId': 0, 'tsGroup': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.output.group'}, 'sourceDomainList': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.domain.list'}, 'dailyInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'daily', 'rpcMethod': 'daily.info'}, 'contactUpdate': {'params': {'contactGroup': [], 'contactId': 0, 'client': '', 'parametr': {}}, 'parent': 'contact', 'rpcMethod': 'contact.update'}, 'timeSchemeInfo': {'params': {'client': '', 'timeSchemeId': 0}, 'parent': 'time', 'rpcMethod': 'time.scheme.info'}, 'sourceTypeValue': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.type.value'}, 'contactGroupDelete': {'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.delete'}, 'operatorDelete': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.delete'}, 'availabilityList': {'params': {'sourceId': 0, 'dateInput': 20140101, 'client': '', 'history': 30}, 'parent': 'availability', 'rpcMethod': 'availability.list'}, 'browserList': {'params': {'client': ''}, 'parent': 'browser', 'rpcMethod': 'browser.list'}, 'sourceGroupAdd': {'params': {'parametr': {}, 'client': '', 'name': ''}, 'parent': 'source', 'rpcMethod': 'source.group.add'}, 'operatorList': {'params': {'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.list'}, 'sourceOutputAdd': {'params': {'sourceId': 0, 'date': '2015-01-01', 'client': '', 'data': []}, 'parent': 'source', 'rpcMethod': 'source.output.add'}, 'dropoutList': {'params': {'dateInput': 2040101, 'client': '', 'history': 7}, 'parent': 'dropout', 'rpcMethod': 'dropout.list'}, 'checkpointList': {'params': {'active': -1, 'client': ''}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.list'}, 'timezoneList': {'params': {'client': ''}, 'parent': 'timezone', 'rpcMethod': 'timezone.list'}}
