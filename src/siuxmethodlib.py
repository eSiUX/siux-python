#!/usr/bin/python
# -*- coding: utf-8 -*-

# generate date: 2015-13-09 17:13:58


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

