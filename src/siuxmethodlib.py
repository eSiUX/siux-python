#!/usr/bin/python
# -*- coding: utf-8 -*-

# generate date: 2015-35-09 18:35:00


class SiUXmethod:

	def availabilityInfo( self, client='', dateTo=20140101 ):
		return self._call( 'availability.info', client, dateTo )

	def availabilityList( self, client='', dateInput=20140101, history=30, sourceId=0 ):
		return self._call( 'availability.list', client, dateInput, history, sourceId )

	def browserList( self, client='' ):
		return self._call( 'browser.list', client )

	def checkpointInfo( self, client='', checkpointId=0 ):
		return self._call( 'checkpoint.info', client, checkpointId )

	def checkpointList( self, client='', active=-1 ):
		return self._call( 'checkpoint.list', client, active )

	def clientUpdate( self, client='', clientDict={} ):
		return self._call( 'client.update', client, clientDict )

	def contactActive( self, client='', value='' ):
		return self._call( 'contact.active', client, value )

	def contactAdd( self, client='', name='', value='', parametr={}, contactGroup=[] ):
		return self._call( 'contact.add', client, name, value, parametr, contactGroup )

	def contactCheckSend( self, client='', contactId=0, text='' ):
		return self._call( 'contact.check.send', client, contactId, text )

	def contactCheckSet( self, client='', contactId=0 ):
		return self._call( 'contact.check.set', client, contactId )

	def contactDeactive( self, client='', value='' ):
		return self._call( 'contact.deactive', client, value )

	def contactDelete( self, client='', contactId=0 ):
		return self._call( 'contact.delete', client, contactId )

	def contactGroupAdd( self, client='', name='', parametr={} ):
		return self._call( 'contact.group.add', client, name, parametr )

	def contactGroupDelete( self, client='', contactGroupId=0 ):
		return self._call( 'contact.group.delete', client, contactGroupId )

	def contactGroupInfo( self, client='', contactGroupId=0 ):
		return self._call( 'contact.group.info', client, contactGroupId )

	def contactGroupList( self, client='' ):
		return self._call( 'contact.group.list', client )

	def contactInfo( self, client='', contactId=0 ):
		return self._call( 'contact.info', client, contactId )

	def contactLinkAdd( self, client='', contactId=0, contactGroupId=0 ):
		return self._call( 'contact.link.add', client, contactId, contactGroupId )

	def contactLinkDelete( self, client='', contactId=0, contactGroupId=0 ):
		return self._call( 'contact.link.delete', client, contactId, contactGroupId )

	def contactList( self, client='', status='all' ):
		return self._call( 'contact.list', client, status )

	def contactTypeList( self, client='' ):
		return self._call( 'contact.type.list', client )

	def contactUpdate( self, client='', contactId=0, parametr={}, contactGroup=[] ):
		return self._call( 'contact.update', client, contactId, parametr, contactGroup )

	def countryList( self, client='' ):
		return self._call( 'country.list', client )

	def dailyInfo( self, client='', dateTo=20140101 ):
		return self._call( 'daily.info', client, dateTo )

	def domainList( self, client='' ):
		return self._call( 'domain.list', client )

	def dropoutInfo( self, client='', dateTo=20140101 ):
		return self._call( 'dropout.info', client, dateTo )

	def dropoutList( self, client='', dateInput=2040101, history=7 ):
		return self._call( 'dropout.list', client, dateInput, history )

	def filterAdd( self, client='', filterData={}, sourceIds=[] ):
		return self._call( 'filter.add', client, filterData, sourceIds )

	def filterDelete( self, client='', filterId=0 ):
		return self._call( 'filter.delete', client, filterId )

	def filterExist( self, client='', filterData={}, sourceIds=[] ):
		return self._call( 'filter.exist', client, filterData, sourceIds )

	def filterInfo( self, client='', filterId=0 ):
		return self._call( 'filter.info', client, filterId )

	def filterList( self, client='', sourceId=0 ):
		return self._call( 'filter.list', client, sourceId )

	def filterViewList( self, client='' ):
		return self._call( 'filter.view.list', client )

	def langList( self, client='' ):
		return self._call( 'lang.list', client )

	def maintenanceAdd( self, client='', maintenanceDict={}, sources=[] ):
		return self._call( 'maintenance.add', client, maintenanceDict, sources )

	def maintenanceInfo( self, client='', maintenanceId=0 ):
		return self._call( 'maintenance.info', client, maintenanceId )

	def maintenanceList( self, client='' ):
		return self._call( 'maintenance.list', client )

	def maintenanceUpdate( self, client='', maintenanceId=0, maintenanceDict={}, sources=[] ):
		return self._call( 'maintenance.update', client, maintenanceId, maintenanceDict, sources )

	def operatorAdd( self, client='', email='', name='', surname='', passwd='', parametr={} ):
		return self._call( 'operator.add', client, email, name, surname, passwd, parametr )

	def operatorAuth( self, client='', session='' ):
		return self._call( 'operator.auth', client, session )

	def operatorDelete( self, client='', operatorId=0 ):
		return self._call( 'operator.delete', client, operatorId )

	def operatorInfo( self, client='', operatorId=0 ):
		return self._call( 'operator.info', client, operatorId )

	def operatorList( self, client='' ):
		return self._call( 'operator.list', client )

	def operatorLogin( self, client='', login='', passwd='' ):
		return self._call( 'operator.login', client, login, passwd )

	def operatorLogout( self, client='', session='' ):
		return self._call( 'operator.logout', client, session )

	def operatorUpdate( self, client='', operatorId=0, operatorDict={} ):
		return self._call( 'operator.update', client, operatorId, operatorDict )

	def seleniumAdd( self, client='', name='', browser='chromelin', timeout=30, testType='content', testIds=[], paramJS=1, paramScreen='' ):
		return self._call( 'selenium.add', client, name, browser, timeout, testType, testIds, paramJS, paramScreen )

	def seleniumAdvancedAdd( self, client='', name='', desc='', code='' ):
		return self._call( 'selenium.advanced.add', client, name, desc, code )

	def seleniumAdvancedCodeAdd( self, client='', advancedId=0, code='', desc='' ):
		return self._call( 'selenium.advanced.code.add', client, advancedId, code, desc )

	def seleniumAdvancedInfo( self, client='', advancedId=0 ):
		return self._call( 'selenium.advanced.info', client, advancedId )

	def seleniumAdvancedList( self, client='' ):
		return self._call( 'selenium.advanced.list', client )

	def seleniumInfo( self, client='', seleniumId=0 ):
		return self._call( 'selenium.info', client, seleniumId )

	def seleniumList( self, client='' ):
		return self._call( 'selenium.list', client )

	def seleniumOutputInfo( self, client='', seleniumId=0, date='2015-01-01' ):
		return self._call( 'selenium.output.info', client, seleniumId, date )

	def seleniumTestAdd( self, client='', urlInput='', searchType='css_selector', searchValue='', urlTarget='' ):
		return self._call( 'selenium.test.add', client, urlInput, searchType, searchValue, urlTarget )

	def seleniumTestInfo( self, client='', seleniumTestId=0 ):
		return self._call( 'selenium.test.info', client, seleniumTestId )

	def seleniumTestList( self, client='' ):
		return self._call( 'selenium.test.list', client )

	def seleniumUpdate( self, client='', seleniumId=0, name='', browser='chromelin', timeout=30, testType='content', testIds=[], status='active', paramJS=1, paramScreen='' ):
		return self._call( 'selenium.update', client, seleniumId, name, browser, timeout, testType, testIds, status, paramJS, paramScreen )

	def senderInfo( self, client='', dateTo=20140101 ):
		return self._call( 'sender.info', client, dateTo )

	def sourceActive( self, client='', sourceId=0 ):
		return self._call( 'source.active', client, sourceId )

	def sourceAdd( self, client='', sourceGroupId=0, name='', url='', parametr={} ):
		return self._call( 'source.add', client, sourceGroupId, name, url, parametr )

	def sourceCheckqueueInfo( self, client='', sourceId=0, date='2008-01-01', limit=2000, FromId=0, countrys=[], checkpointIds=[] ):
		return self._call( 'source.checkqueue.info', client, sourceId, date, limit, FromId, countrys, checkpointIds )

	def sourceDeactive( self, client='', sourceId=0 ):
		return self._call( 'source.deactive', client, sourceId )

	def sourceDelete( self, client='', sourceId=0 ):
		return self._call( 'source.delete', client, sourceId )

	def sourceDropoutInfo( self, client='', sourceId=0, date='2008-01-01' ):
		return self._call( 'source.dropout.info', client, sourceId, date )

	def sourceDropoutList( self, client='', sourceId=0, history=7 ):
		return self._call( 'source.dropout.list', client, sourceId, history )

	def sourceGroupAdd( self, client='', name='', parametr={} ):
		return self._call( 'source.group.add', client, name, parametr )

	def sourceGroupDelete( self, client='', sourceGroupId=0 ):
		return self._call( 'source.group.delete', client, sourceGroupId )

	def sourceGroupInfo( self, client='', sourceGroupId=0 ):
		return self._call( 'source.group.info', client, sourceGroupId )

	def sourceGroupList( self, client='' ):
		return self._call( 'source.group.list', client )

	def sourceGroupSet( self, client='', sourceGroupId=0, contactGroupIds=[] ):
		return self._call( 'source.group.set', client, sourceGroupId, contactGroupIds )

	def sourceInfo( self, client='', sourceId=0 ):
		return self._call( 'source.info', client, sourceId )

	def sourceList( self, client='', sourceGroupId=0 ):
		return self._call( 'source.list', client, sourceGroupId )

	def sourceOutputAdd( self, client='',sourceId=0, date='2015-01-01', data=[] ):
		return self._call( 'source.output.add', client, sourceId, date, data )

	def sourceOutputInfo( self, client='', sourceId=0, date='2008-01-01', limit=2000, FromId=0, outputId=0, countrys=[], checkpointIds=[], dataView='all' ):
		return self._call( 'source.output.info', client, sourceId, date, limit, FromId, outputId, countrys, checkpointIds, dataView )

	def sourceStatDailyList( self, client='', sourceId=0, date='2001-01' ):
		return self._call( 'source.stat.daily.list', client, sourceId, date )

	def sourceStatList( self, hostname, history=7 ):
		return self._call( 'source.stat.list', hostname, history )

	def sourceStatMonthlyList( self, client='', sourceId=0, history=12 ):
		return self._call( 'source.stat.monthly.list', client, sourceId, history )

	def sourceTypeList( self, client='' ):
		return self._call( 'source.type.list', client )

	def sourceTypeValue( self, client='' ):
		return self._call( 'source.type.value', client )

	def sourceUpdate( self, client='', sourceId=0, sourceDict={} ):
		return self._call( 'source.update', client, sourceId, sourceDict )

	def testFilterList( self, client='' ):
		return self._call( 'test.filter.list', client )

	def testStatusList( self, client='' ):
		return self._call( 'test.status.list', client )

	def testValueList( self, client='', sourceGroupId=0 ):
		return self._call( 'test.value.list', client, sourceGroupId )

	def timePlanList( self, client='' ):
		return self._call( 'time.plan.list', client )

	def timeSchemeInfo( self, client='', timeSchemeId=0 ):
		return self._call( 'time.scheme.info', client, timeSchemeId )

	def timeSchemeList( self, client='' ):
		return self._call( 'time.scheme.list', client )

	def timezoneList( self, client='' ):
		return self._call( 'timezone.list', client )



methodArgs =  {'operatorLogin': {'params': {'passwd': '', 'login': '', 'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.login'}, 'contactDeactive': {'params': {'client': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.deactive'}, 'contactTypeList': {'params': {'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.type.list'}, 'availabilityInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'availability', 'rpcMethod': 'availability.info'}, 'operatorUpdate': {'params': {'client': '', 'operatorDict': {}, 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.update'}, 'sourceGroupDelete': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.delete'}, 'contactGroupList': {'params': {'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.list'}, 'contactDelete': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.delete'}, 'sourceDeactive': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.deactive'}, 'filterInfo': {'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.info'}, 'domainList': {'params': {'client': ''}, 'parent': 'domain', 'rpcMethod': 'domain.list'}, 'contactActive': {'params': {'client': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.active'}, 'sourceStatList': {'params': {'hostname': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.stat.list'}, 'filterViewList': {'params': {'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.view.list'}, 'sourceGroupList': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.group.list'}, 'operatorAuth': {'params': {'session': '', 'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.auth'}, 'contactCheckSet': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.check.set'}, 'seleniumUpdate': {'params': {'status': 'active', 'seleniumId': 0, 'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.update'}, 'operatorLogout': {'params': {'session': '', 'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.logout'}, 'testFilterList': {'params': {'client': ''}, 'parent': 'test', 'rpcMethod': 'test.filter.list'}, 'seleniumAdvancedList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.list'}, 'sourceTypeList': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.type.list'}, 'contactCheckSend': {'params': {'text': '', 'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.check.send'}, 'timeSchemeList': {'params': {'client': ''}, 'parent': 'time', 'rpcMethod': 'time.scheme.list'}, 'maintenanceUpdate': {'params': {'sources': [], 'maintenanceDict': {}, 'client': '', 'maintenanceId': 0}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.update'}, 'checkpointInfo': {'params': {'client': '', 'checkpointId': 0}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.info'}, 'sourceCheckqueueInfo': {'params': {'sourceId': 0, 'checkpointIds': [], 'countrys': [], 'client': '', 'limit': 2000, 'date': '2008-01-01', 'FromId': 0}, 'parent': 'source', 'rpcMethod': 'source.checkqueue.info'}, 'seleniumTestInfo': {'params': {'seleniumTestId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.info'}, 'maintenanceInfo': {'params': {'client': '', 'maintenanceId': 0}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.info'}, 'sourceUpdate': {'params': {'sourceId': 0, 'sourceDict': {}, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.update'}, 'sourceList': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.list'}, 'maintenanceAdd': {'params': {'sources': [], 'maintenanceDict': {}, 'client': ''}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.add'}, 'countryList': {'params': {'client': ''}, 'parent': 'country', 'rpcMethod': 'country.list'}, 'seleniumTestList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.list'}, 'sourceGroupSet': {'params': {'client': '', 'contactGroupIds': [], 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.set'}, 'langList': {'params': {'client': ''}, 'parent': 'lang', 'rpcMethod': 'lang.list'}, 'seleniumAdd': {'params': {'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.add'}, 'operatorAdd': {'params': {'surname': '', 'name': '', 'passwd': '', 'parametr': {}, 'client': '', 'email': ''}, 'parent': 'operator', 'rpcMethod': 'operator.add'}, 'sourceDelete': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.delete'}, 'sourceDropoutList': {'params': {'sourceId': 0, 'client': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.dropout.list'}, 'seleniumOutputInfo': {'params': {'date': '2015-01-01', 'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.output.info'}, 'seleniumTestAdd': {'params': {'client': '', 'searchValue': '', 'urlInput': '', 'searchType': 'css_selector', 'urlTarget': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.add'}, 'testValueList': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'test', 'rpcMethod': 'test.value.list'}, 'filterExist': {'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.exist'}, 'seleniumList': {'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.list'}, 'senderInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'sender', 'rpcMethod': 'sender.info'}, 'sourceStatMonthlyList': {'params': {'sourceId': 0, 'client': '', 'history': 12}, 'parent': 'source', 'rpcMethod': 'source.stat.monthly.list'}, 'sourceActive': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.active'}, 'sourceStatDailyList': {'params': {'sourceId': 0, 'date': '2001-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.stat.daily.list'}, 'testStatusList': {'params': {'client': ''}, 'parent': 'test', 'rpcMethod': 'test.status.list'}, 'contactLinkAdd': {'params': {'contactGroupId': 0, 'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.link.add'}, 'seleniumAdvancedAdd': {'params': {'code': '', 'client': '', 'name': '', 'desc': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.add'}, 'seleniumAdvancedCodeAdd': {'params': {'code': '', 'desc': '', 'client': '', 'advancedId': 0}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.code.add'}, 'filterList': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.list'}, 'seleniumAdvancedInfo': {'params': {'client': '', 'advancedId': 0}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.info'}, 'sourceOutputInfo': {'params': {'sourceId': 0, 'dataView': 'all', 'checkpointIds': [], 'outputId': 0, 'countrys': [], 'client': '', 'limit': 2000, 'date': '2008-01-01', 'FromId': 0}, 'parent': 'source', 'rpcMethod': 'source.output.info'}, 'clientUpdate': {'params': {'client': '', 'clientDict': {}}, 'parent': 'client', 'rpcMethod': 'client.update'}, 'contactGroupInfo': {'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.info'}, 'filterAdd': {'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.add'}, 'contactLinkDelete': {'params': {'contactGroupId': 0, 'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.link.delete'}, 'sourceDropoutInfo': {'params': {'sourceId': 0, 'date': '2008-01-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.dropout.info'}, 'contactList': {'params': {'status': 'all', 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.list'}, 'filterDelete': {'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.delete'}, 'sourceInfo': {'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.info'}, 'sourceAdd': {'params': {'url': '', 'parametr': {}, 'client': '', 'name': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.add'}, 'contactAdd': {'params': {'contactGroup': [], 'parametr': {}, 'client': '', 'name': '', 'value': ''}, 'parent': 'contact', 'rpcMethod': 'contact.add'}, 'dropoutInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'dropout', 'rpcMethod': 'dropout.info'}, 'sourceGroupInfo': {'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.info'}, 'contactGroupAdd': {'params': {'parametr': {}, 'client': '', 'name': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.add'}, 'maintenanceList': {'params': {'client': ''}, 'parent': 'maintenance', 'rpcMethod': 'maintenance.list'}, 'seleniumInfo': {'params': {'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.info'}, 'operatorInfo': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.info'}, 'timePlanList': {'params': {'client': ''}, 'parent': 'time', 'rpcMethod': 'time.plan.list'}, 'contactInfo': {'params': {'contactId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.info'}, 'dailyInfo': {'params': {'dateTo': 20140101, 'client': ''}, 'parent': 'daily', 'rpcMethod': 'daily.info'}, 'contactUpdate': {'params': {'contactGroup': [], 'contactId': 0, 'client': '', 'parametr': {}}, 'parent': 'contact', 'rpcMethod': 'contact.update'}, 'timeSchemeInfo': {'params': {'client': '', 'timeSchemeId': 0}, 'parent': 'time', 'rpcMethod': 'time.scheme.info'}, 'sourceTypeValue': {'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.type.value'}, 'contactGroupDelete': {'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'contact', 'rpcMethod': 'contact.group.delete'}, 'operatorDelete': {'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.delete'}, 'availabilityList': {'params': {'sourceId': 0, 'dateInput': 20140101, 'client': '', 'history': 30}, 'parent': 'availability', 'rpcMethod': 'availability.list'}, 'browserList': {'params': {'client': ''}, 'parent': 'browser', 'rpcMethod': 'browser.list'}, 'sourceGroupAdd': {'params': {'parametr': {}, 'client': '', 'name': ''}, 'parent': 'source', 'rpcMethod': 'source.group.add'}, 'operatorList': {'params': {'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.list'}, 'sourceOutputAdd': {'params': {'sourceId': 0, 'date': '2015-01-01', 'client': '', 'data': []}, 'parent': 'source', 'rpcMethod': 'source.output.add'}, 'dropoutList': {'params': {'dateInput': 2040101, 'client': '', 'history': 7}, 'parent': 'dropout', 'rpcMethod': 'dropout.list'}, 'checkpointList': {'params': {'active': -1, 'client': ''}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.list'}, 'timezoneList': {'params': {'client': ''}, 'parent': 'timezone', 'rpcMethod': 'timezone.list'}}
