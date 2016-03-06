#!/usr/bin/python
# -*- coding: utf-8 -*-

# generate date: 2016-02-13 18:58:05


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

	def availabilityHourlyList( self,  dateInput=20160201, history=30, view='hourOnly' ):
		" Method availabilityHourlyList() "
		return self._call( 'availability.hourly.list', self._auth, dateInput, history, view )

	def availabilityInfo( self,  dateTo=20150901 ):
		" Method availabilityInfo() "
		return self._call( 'availability.info', self._auth, dateTo )

	def availabilityList( self,  dateInput=20150901, history=30, sourceId=0 ):
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
	# CONTRACT 

	def contractAdd( self,  parameter={}, sources=[] ):
		" Method contractAdd() "
		return self._call( 'contract.add', self._auth, parameter, sources )

	def contractInfo( self,  contractId=0 ):
		" Method contractInfo() "
		return self._call( 'contract.info', self._auth, contractId )

	def contractList( self,  status='all', history=30 ):
		" Method contractList() "
		return self._call( 'contract.list', self._auth, status, history )

	def contractOutputInfo( self,  contractId=0, dateInput=20160201, history=30 ):
		" Method contractOutputInfo() "
		return self._call( 'contract.output.info', self._auth, contractId, dateInput, history )

	def contractUpdate( self,  contractId=0, parameter={}, sources=[] ):
		" Method contractUpdate() "
		return self._call( 'contract.update', self._auth, contractId, parameter, sources )


	# --- 
	# CONTRACTOR 

	def contractorAdd( self,  parameter={} ):
		" Method contractorAdd() "
		return self._call( 'contractor.add', self._auth, parameter )

	def contractorInfo( self,  contractorId=0 ):
		" Method contractorInfo() "
		return self._call( 'contractor.info', self._auth, contractorId )

	def contractorList( self  ):
		" Method contractorList() "
		return self._call( 'contractor.list', self._auth )

	def contractorUpdate( self,  contractorId=0, parameter={} ):
		" Method contractorUpdate() "
		return self._call( 'contractor.update', self._auth, contractorId, parameter )


	# --- 
	# COUNTRY 

	def countryList( self  ):
		" Method countryList() "
		return self._call( 'country.list', self._auth )


	# --- 
	# DEPLOY 

	def deployAdd( self,  tagId=0, version='', env='', operatorId=0 ):
		" Method deployAdd() "
		return self._call( 'deploy.add', self._auth, tagId, version, env, operatorId )

	def deployInfo( self,  deployId=0 ):
		" Method deployInfo() "
		return self._call( 'deploy.info', self._auth, deployId )

	def deployList( self,  environments=[] ):
		" Method deployList() "
		return self._call( 'deploy.list', self._auth, environments )


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
	# LANG 

	def langList( self  ):
		" Method langList() "
		return self._call( 'lang.list', self._auth )


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

	def notifySenderInfo( self,  dateTo=20150101, view='all', From=0, step=20 ):
		" Method notifySenderInfo() "
		return self._call( 'notify.sender.info', self._auth, dateTo, view, From, step )

	def notifySenderList( self,  dateTo=20160101, history=30 ):
		" Method notifySenderList() "
		return self._call( 'notify.sender.list', self._auth, dateTo, history )

	def notifyUpdate( self,  contactId=0, parameter={}, contactGroup=[] ):
		" Method notifyUpdate() "
		return self._call( 'notify.update', self._auth, contactId, parameter, contactGroup )


	# --- 
	# OPERATOR 

	def operatorInfo( self,  operatorId=0 ):
		" Method operatorInfo() "
		return self._call( 'operator.info', self._auth, operatorId )

	def operatorLangSet( self,  operatorId=0, lang='' ):
		" Method operatorLangSet() "
		return self._call( 'operator.lang.set', self._auth, operatorId, lang )

	def operatorList( self  ):
		" Method operatorList() "
		return self._call( 'operator.list', self._auth )

	def operatorLogList( self,  operatorId=0 ):
		" Method operatorLogList() "
		return self._call( 'operator.log.list', self._auth, operatorId )


	# --- 
	# RUM 

	def rumOutputInfo( self,  sourceId=0, date='2015-09-01', outputId=0 ):
		" Method rumOutputInfo() "
		return self._call( 'rum.output.info', self._auth, sourceId, date, outputId )


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

	def sourceGroupUpdate( self,  sourceGroupId=0, parameter={} ):
		" Method sourceGroupUpdate() "
		return self._call( 'source.group.update', self._auth, sourceGroupId, parameter )

	def sourceInfo( self,  sourceId=0 ):
		" Method sourceInfo() "
		return self._call( 'source.info', self._auth, sourceId )

	def sourceList( self,  sourceGroupId=0, tagId=0 ):
		" Method sourceList() "
		return self._call( 'source.list', self._auth, sourceGroupId, tagId )

	def sourceOutputGroup( self,  sourceId=0, tsGroup=0 ):
		" Method sourceOutputGroup() "
		return self._call( 'source.output.group', self._auth, sourceId, tsGroup )

	def sourceOutputHeaderInfo( self,  sourceId=0, date='2015-01-01', outputId=0 ):
		" Method sourceOutputHeaderInfo() "
		return self._call( 'source.output.header.info', self._auth, sourceId, date, outputId )

	def sourceOutputInfo( self,  sourceId=0, date='2015-09-01', limit=2000, FromId=0, outputId=0, countrys=[], checkpointIds=[], dataView='all' ):
		" Method sourceOutputInfo() "
		return self._call( 'source.output.info', self._auth, sourceId, date, limit, FromId, outputId, countrys, checkpointIds, dataView )

	def sourceStatDailyList( self,  sourceId=0, date='2001-01' ):
		" Method sourceStatDailyList() "
		return self._call( 'source.stat.daily.list', self._auth, sourceId, date )

	def sourceStatMonthlyList( self,  sourceId=0, history=12 ):
		" Method sourceStatMonthlyList() "
		return self._call( 'source.stat.monthly.list', self._auth, sourceId, history )

	def sourceStatWeeklyList( self,  sourceId=0, date='2001-01-01' ):
		" Method sourceStatWeeklyList() "
		return self._call( 'source.stat.weekly.list', self._auth, sourceId, date )

	def sourceUpdate( self,  sourceId=0, sourceDict={} ):
		" Method sourceUpdate() "
		return self._call( 'source.update', self._auth, sourceId, sourceDict )

	def sourceVideoInfo( self,  sourceId=0, date='2015-09-01', whatName='session', whatId='' ):
		" Method sourceVideoInfo() "
		return self._call( 'source.video.info', self._auth, sourceId, date, whatName, whatId )


	# --- 
	# TAG 

	def tagAdd( self,  name='', label='default', flagNotify=0, flagDeploy=0 ):
		" Method tagAdd() "
		return self._call( 'tag.add', self._auth, name, label, flagNotify, flagDeploy )

	def tagDelete( self,  tagId=0 ):
		" Method tagDelete() "
		return self._call( 'tag.delete', self._auth, tagId )

	def tagInfo( self,  tagId=0 ):
		" Method tagInfo() "
		return self._call( 'tag.info', self._auth, tagId )

	def tagList( self  ):
		" Method tagList() "
		return self._call( 'tag.list', self._auth )

	def tagReplyAdd( self,  tagId=0, sourceId=0, operatorId=0, senderId=0, date=0 ):
		" Method tagReplyAdd() "
		return self._call( 'tag.reply.add', self._auth, tagId, sourceId, operatorId, senderId, date )

	def tagReplyList( self,  tagId=0, sourceId=0, From=0, step=20 ):
		" Method tagReplyList() "
		return self._call( 'tag.reply.list', self._auth, tagId, sourceId, From, step )

	def tagReplyUpdate( self,  tagReplyId=0, operatorId=0, comment='' ):
		" Method tagReplyUpdate() "
		return self._call( 'tag.reply.update', self._auth, tagReplyId, operatorId, comment )


	# --- 
	# TIMEZONE 

	def timezoneList( self  ):
		" Method timezoneList() "
		return self._call( 'timezone.list', self._auth )


	# --- 
	# VIDEO 

	def videoOutputInfo( self,  sourceId=0, date='2015-09-01', limit=2000, FromId=0, outputId=0, countrys=[], checkpointIds=[], dataView='all', videoId='' ):
		" Method videoOutputInfo() "
		return self._call( 'video.output.info', self._auth, sourceId, date, limit, FromId, outputId, countrys, checkpointIds, dataView, videoId )



methodArgs =  {'notifyGroupList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.list'}, 'notifyGroupDelete': {'paramArr': ['client', 'contactGroupId'], 'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.delete'}, 'availabilityInfo': {'paramArr': ['client', 'dateTo'], 'params': {'dateTo': 20150901, 'client': ''}, 'parent': 'availability', 'rpcMethod': 'availability.info'}, 'tagInfo': {'paramArr': ['client', 'tagId'], 'params': {'tagId': 0, 'client': ''}, 'parent': 'tag', 'rpcMethod': 'tag.info'}, 'sourceGroupDelete': {'paramArr': ['client', 'sourceGroupId'], 'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.delete'}, 'sourceDeactive': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.deactive'}, 'filterInfo': {'paramArr': ['client', 'filterId'], 'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.info'}, 'seleniumTestAdd': {'paramArr': ['client', 'urlInput', 'searchType', 'searchValue', 'urlTarget', 'advancedId'], 'params': {'searchType': 'css_selector', 'searchValue': '', 'advancedId': 0, 'client': '', 'urlInput': '', 'urlTarget': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.add'}, 'sourceStatDailyList': {'paramArr': ['client', 'sourceId', 'date'], 'params': {'sourceId': 0, 'date': '2001-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.stat.daily.list'}, 'sourceGroupList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'source', 'rpcMethod': 'source.group.list'}, 'sourceStatWeeklyList': {'paramArr': ['client', 'sourceId', 'date'], 'params': {'sourceId': 0, 'date': '2001-01-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.stat.weekly.list'}, 'tagDelete': {'paramArr': ['client', 'tagId'], 'params': {'tagId': 0, 'client': ''}, 'parent': 'tag', 'rpcMethod': 'tag.delete'}, 'seleniumUpdate': {'paramArr': ['client', 'seleniumId', 'name', 'browser', 'timeout', 'testType', 'testIds', 'status', 'paramJS', 'paramScreen'], 'params': {'status': 'active', 'seleniumId': 0, 'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.update'}, 'tagAdd': {'paramArr': ['client', 'name', 'label', 'flagNotify', 'flagDeploy'], 'params': {'flagNotify': 0, 'flagDeploy': 0, 'client': '', 'name': '', 'label': 'default'}, 'parent': 'tag', 'rpcMethod': 'tag.add'}, 'contractorAdd': {'paramArr': ['client', 'parameter'], 'params': {'client': '', 'parameter': {}}, 'parent': 'contractor', 'rpcMethod': 'contractor.add'}, 'tagList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'tag', 'rpcMethod': 'tag.list'}, 'seleniumAdvancedList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.list'}, 'contractorList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'contractor', 'rpcMethod': 'contractor.list'}, 'apikeyDelete': {'paramArr': ['client', 'apikeyId'], 'params': {'client': '', 'apikeyId': 0}, 'parent': 'apikey', 'rpcMethod': 'apikey.delete'}, 'notifyAdd': {'paramArr': ['client', 'name', 'value', 'parameter', 'contactGroup'], 'params': {'contactGroup': [], 'client': '', 'parameter': {}, 'name': '', 'value': ''}, 'parent': 'notify', 'rpcMethod': 'notify.add'}, 'notifyGroupInfo': {'paramArr': ['client', 'contactGroupId'], 'params': {'contactGroupId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.info'}, 'contractInfo': {'paramArr': ['client', 'contractId'], 'params': {'client': '', 'contractId': 0}, 'parent': 'contract', 'rpcMethod': 'contract.info'}, 'checkpointInfo': {'paramArr': ['client', 'checkpointId'], 'params': {'client': '', 'checkpointId': 0}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.info'}, 'apikeyList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'apikey', 'rpcMethod': 'apikey.list'}, 'availabilityHourlyList': {'paramArr': ['client', 'dateInput', 'history', 'view'], 'params': {'dateInput': 20160201, 'client': '', 'view': 'hourOnly', 'history': 30}, 'parent': 'availability', 'rpcMethod': 'availability.hourly.list'}, 'seleniumTestInfo': {'paramArr': ['client', 'seleniumTestId'], 'params': {'seleniumTestId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.info'}, 'tagReplyAdd': {'paramArr': ['client', 'tagId', 'sourceId', 'operatorId', 'senderId', 'date'], 'params': {'operatorId': 0, 'sourceId': 0, 'tagId': 0, 'senderId': 0, 'client': '', 'date': 0}, 'parent': 'tag', 'rpcMethod': 'tag.reply.add'}, 'sourceUpdate': {'paramArr': ['client', 'sourceId', 'sourceDict'], 'params': {'sourceId': 0, 'sourceDict': {}, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.update'}, 'sourceList': {'paramArr': ['client', 'sourceGroupId', 'tagId'], 'params': {'tagId': 0, 'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.list'}, 'operatorLogList': {'paramArr': ['client', 'operatorId'], 'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.log.list'}, 'contractorInfo': {'paramArr': ['client', 'contractorId'], 'params': {'contractorId': 0, 'client': ''}, 'parent': 'contractor', 'rpcMethod': 'contractor.info'}, 'countryList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'country', 'rpcMethod': 'country.list'}, 'seleniumTestList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.test.list'}, 'langList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'lang', 'rpcMethod': 'lang.list'}, 'seleniumAdd': {'paramArr': ['client', 'name', 'browser', 'timeout', 'testType', 'testIds', 'paramJS', 'paramScreen'], 'params': {'name': '', 'paramScreen': '', 'testIds': [], 'client': '', 'paramJS': 1, 'timeout': 30, 'testType': 'content', 'browser': 'chromelin'}, 'parent': 'selenium', 'rpcMethod': 'selenium.add'}, 'notifySenderList': {'paramArr': ['client', 'dateTo', 'history'], 'params': {'dateTo': 20160101, 'client': '', 'history': 30}, 'parent': 'notify', 'rpcMethod': 'notify.sender.list'}, 'contractAdd': {'paramArr': ['client', 'parameter', 'sources'], 'params': {'sources': [], 'client': '', 'parameter': {}}, 'parent': 'contract', 'rpcMethod': 'contract.add'}, 'sourceStatMonthlyList': {'paramArr': ['client', 'sourceId', 'history'], 'params': {'sourceId': 0, 'client': '', 'history': 12}, 'parent': 'source', 'rpcMethod': 'source.stat.monthly.list'}, 'contractorUpdate': {'paramArr': ['client', 'contractorId', 'parameter'], 'params': {'contractorId': 0, 'client': '', 'parameter': {}}, 'parent': 'contractor', 'rpcMethod': 'contractor.update'}, 'notifyGroupAdd': {'paramArr': ['client', 'name', 'parameter'], 'params': {'client': '', 'parameter': {}, 'name': ''}, 'parent': 'notify', 'rpcMethod': 'notify.group.add'}, 'seleniumOutputInfo': {'paramArr': ['client', 'seleniumId', 'date'], 'params': {'date': '2015-01-01', 'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.output.info'}, 'notifyUpdate': {'paramArr': ['client', 'contactId', 'parameter', 'contactGroup'], 'params': {'contactGroup': [], 'contactId': 0, 'client': '', 'parameter': {}}, 'parent': 'notify', 'rpcMethod': 'notify.update'}, 'contractList': {'paramArr': ['client', 'status', 'history'], 'params': {'status': 'all', 'client': '', 'history': 30}, 'parent': 'contract', 'rpcMethod': 'contract.list'}, 'filterExist': {'paramArr': ['client', 'filterData', 'sourceIds'], 'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.exist'}, 'tagReplyUpdate': {'paramArr': ['client', 'tagReplyId', 'operatorId', 'comment'], 'params': {'comment': '', 'tagReplyId': 0, 'client': '', 'operatorId': 0}, 'parent': 'tag', 'rpcMethod': 'tag.reply.update'}, 'notifySenderInfo': {'paramArr': ['client', 'dateTo', 'view', 'From', 'step'], 'params': {'dateTo': 20150101, 'step': 20, 'client': '', 'From': 0, 'view': 'all'}, 'parent': 'notify', 'rpcMethod': 'notify.sender.info'}, 'notifyDeactive': {'paramArr': ['client', 'value'], 'params': {'client': '', 'value': ''}, 'parent': 'notify', 'rpcMethod': 'notify.deactive'}, 'contractOutputInfo': {'paramArr': ['client', 'contractId', 'dateInput', 'history'], 'params': {'dateInput': 20160201, 'client': '', 'history': 30, 'contractId': 0}, 'parent': 'contract', 'rpcMethod': 'contract.output.info'}, 'seleniumList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.list'}, 'deployAdd': {'paramArr': ['client', 'tagId', 'version', 'env', 'operatorId'], 'params': {'tagId': 0, 'client': '', 'version': '', 'env': '', 'operatorId': 0}, 'parent': 'deploy', 'rpcMethod': 'deploy.add'}, 'sourceOutputHeaderInfo': {'paramArr': ['client', 'sourceId', 'date', 'outputId'], 'params': {'sourceId': 0, 'date': '2015-01-01', 'client': '', 'outputId': 0}, 'parent': 'source', 'rpcMethod': 'source.output.header.info'}, 'sourceDropoutList': {'paramArr': ['client', 'sourceId', 'history'], 'params': {'sourceId': 0, 'client': '', 'history': 7}, 'parent': 'source', 'rpcMethod': 'source.dropout.list'}, 'sourceActive': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.active'}, 'filterViewList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.view.list'}, 'rumOutputInfo': {'paramArr': ['client', 'sourceId', 'date', 'outputId'], 'params': {'sourceId': 0, 'date': '2015-09-01', 'client': '', 'outputId': 0}, 'parent': 'rum', 'rpcMethod': 'rum.output.info'}, 'seleniumAdvancedAdd': {'paramArr': ['client', 'name', 'desc', 'code', 'nickname', 'inputUrl', 'targetUrl'], 'params': {'code': '', 'name': '', 'targetUrl': '', 'client': '', 'inputUrl': '', 'nickname': '', 'desc': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.add'}, 'sourceVideoInfo': {'paramArr': ['client', 'sourceId', 'date', 'whatName', 'whatId'], 'params': {'sourceId': 0, 'date': '2015-09-01', 'client': '', 'whatName': 'session', 'whatId': ''}, 'parent': 'source', 'rpcMethod': 'source.video.info'}, 'filterList': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'filter', 'rpcMethod': 'filter.list'}, 'seleniumAdvancedInfo': {'paramArr': ['client', 'advancedId'], 'params': {'client': '', 'advancedId': 0}, 'parent': 'selenium', 'rpcMethod': 'selenium.advanced.info'}, 'sourceOutputInfo': {'paramArr': ['client', 'sourceId', 'date', 'limit', 'FromId', 'outputId', 'countrys', 'checkpointIds', 'dataView'], 'params': {'sourceId': 0, 'dataView': 'all', 'checkpointIds': [], 'outputId': 0, 'countrys': [], 'client': '', 'limit': 2000, 'date': '2015-09-01', 'FromId': 0}, 'parent': 'source', 'rpcMethod': 'source.output.info'}, 'operatorLangSet': {'paramArr': ['client', 'operatorId', 'lang'], 'params': {'lang': '', 'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.lang.set'}, 'filterAdd': {'paramArr': ['client', 'filterData', 'sourceIds'], 'params': {'sourceIds': [], 'client': '', 'filterData': {}}, 'parent': 'filter', 'rpcMethod': 'filter.add'}, 'notifyList': {'paramArr': ['client', 'status'], 'params': {'status': 'all', 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.list'}, 'sourceDropoutInfo': {'paramArr': ['client', 'sourceId', 'date'], 'params': {'sourceId': 0, 'date': '2015-09-01', 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.dropout.info'}, 'tagReplyList': {'paramArr': ['client', 'tagId', 'sourceId', 'From', 'step'], 'params': {'sourceId': 0, 'tagId': 0, 'client': '', 'From': 0, 'step': 20}, 'parent': 'tag', 'rpcMethod': 'tag.reply.list'}, 'filterDelete': {'paramArr': ['client', 'filterId'], 'params': {'client': '', 'filterId': 0}, 'parent': 'filter', 'rpcMethod': 'filter.delete'}, 'sourceInfo': {'paramArr': ['client', 'sourceId'], 'params': {'sourceId': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.info'}, 'sourceAdd': {'paramArr': ['client', 'sourceGroupId', 'name', 'url', 'parameter'], 'params': {'url': '', 'client': '', 'parameter': {}, 'name': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.add'}, 'dropoutInfo': {'paramArr': ['client', 'dateTo'], 'params': {'dateTo': 20150901, 'client': ''}, 'parent': 'dropout', 'rpcMethod': 'dropout.info'}, 'sourceGroupInfo': {'paramArr': ['client', 'sourceGroupId'], 'params': {'client': '', 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.info'}, 'deployList': {'paramArr': ['client', 'environments'], 'params': {'client': '', 'environments': []}, 'parent': 'deploy', 'rpcMethod': 'deploy.list'}, 'deployInfo': {'paramArr': ['client', 'deployId'], 'params': {'deployId': 0, 'client': ''}, 'parent': 'deploy', 'rpcMethod': 'deploy.info'}, 'seleniumInfo': {'paramArr': ['client', 'seleniumId'], 'params': {'seleniumId': 0, 'client': ''}, 'parent': 'selenium', 'rpcMethod': 'selenium.info'}, 'sourceGroupUpdate': {'paramArr': ['client', 'sourceGroupId', 'parameter'], 'params': {'client': '', 'parameter': {}, 'sourceGroupId': 0}, 'parent': 'source', 'rpcMethod': 'source.group.update'}, 'operatorInfo': {'paramArr': ['client', 'operatorId'], 'params': {'client': '', 'operatorId': 0}, 'parent': 'operator', 'rpcMethod': 'operator.info'}, 'sourceOutputGroup': {'paramArr': ['client', 'sourceId', 'tsGroup'], 'params': {'sourceId': 0, 'tsGroup': 0, 'client': ''}, 'parent': 'source', 'rpcMethod': 'source.output.group'}, 'apikeyAdd': {'paramArr': ['client', 'name', 'readOnly'], 'params': {'readOnly': 0, 'client': '', 'name': ''}, 'parent': 'apikey', 'rpcMethod': 'apikey.add'}, 'notifyInfo': {'paramArr': ['client', 'contactId'], 'params': {'contactId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.info'}, 'videoOutputInfo': {'paramArr': ['client', 'sourceId', 'date', 'limit', 'FromId', 'outputId', 'countrys', 'checkpointIds', 'dataView', 'videoId'], 'params': {'sourceId': 0, 'dataView': 'all', 'checkpointIds': [], 'videoId': '', 'outputId': 0, 'countrys': [], 'client': '', 'limit': 2000, 'date': '2015-09-01', 'FromId': 0}, 'parent': 'video', 'rpcMethod': 'video.output.info'}, 'availabilityList': {'paramArr': ['client', 'dateInput', 'history', 'sourceId'], 'params': {'sourceId': 0, 'dateInput': 20150901, 'client': '', 'history': 30}, 'parent': 'availability', 'rpcMethod': 'availability.list'}, 'browserList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'browser', 'rpcMethod': 'browser.list'}, 'sourceGroupAdd': {'paramArr': ['client', 'name', 'parameter'], 'params': {'client': '', 'parameter': {}, 'name': ''}, 'parent': 'source', 'rpcMethod': 'source.group.add'}, 'operatorList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'operator', 'rpcMethod': 'operator.list'}, 'contractUpdate': {'paramArr': ['client', 'contractId', 'parameter', 'sources'], 'params': {'sources': [], 'client': '', 'parameter': {}, 'contractId': 0}, 'parent': 'contract', 'rpcMethod': 'contract.update'}, 'dropoutList': {'paramArr': ['client', 'dateInput', 'history'], 'params': {'dateInput': 2040101, 'client': '', 'history': 7}, 'parent': 'dropout', 'rpcMethod': 'dropout.list'}, 'checkpointList': {'paramArr': ['client', 'active'], 'params': {'active': -1, 'client': ''}, 'parent': 'checkpoint', 'rpcMethod': 'checkpoint.list'}, 'notifyDelete': {'paramArr': ['client', 'contactId'], 'params': {'contactId': 0, 'client': ''}, 'parent': 'notify', 'rpcMethod': 'notify.delete'}, 'timezoneList': {'paramArr': ['client'], 'params': {'client': ''}, 'parent': 'timezone', 'rpcMethod': 'timezone.list'}}
