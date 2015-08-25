#!/usr/bin/python

import unittest, pprint, sys

sys.path.append( '../src' )
import siuxlib


class TestSourceInfo(unittest.TestCase):

	# config
	auth = '<YOUR_API_KEY>'


	def checkSourceInfo( self,retList ):
		"""
		Method tests sourceInfo structure
		:param retList: - structure reported by API
		"""

		self.assertTrue( 'browser' in retList )

		self.assertTrue( 'browserFamilyName' in retList )

		self.assertTrue( 'browserId' in retList )
		self.assertTrue( isinstance( retList['browserId']  ,int ))

		self.assertTrue( 'browserName' in retList )

		self.assertTrue( 'clientId' in retList )
		self.assertTrue( isinstance( retList['clientId']  ,int ))

		self.assertTrue( 'clientName' in retList )

		self.assertTrue( 'clientPay' in retList )
		self.assertTrue( isinstance( retList['clientPay']  ,int ))

		self.assertTrue( 'domainId' in retList )
		self.assertTrue( isinstance( retList['domainId']  ,int ))

		self.assertTrue( 'googleGaProfileId' in retList )
		self.assertTrue( isinstance( retList['googleGaProfileId']  ,int ))

		self.assertTrue( 'googleGaTsCreate' in retList )
		self.assertTrue( isinstance( retList['googleGaTsCreate']  ,int ))

		self.assertTrue( 'lastChecktime' in retList )
		self.assertTrue( isinstance( retList['lastChecktime']  ,int ))

		self.assertTrue( 'lastErrChecktime' in retList )
		self.assertTrue( isinstance( retList['lastErrChecktime']  ,int ))

		self.assertTrue( 'lastErrNo' in retList )
		self.assertTrue( isinstance( retList['lastErrNo']  ,int ))

		self.assertTrue( 'lastErrStatusCode' in retList )
		self.assertTrue( isinstance( retList['lastErrStatusCode']  ,int ))

		self.assertTrue( 'lastErrStatusMessage' in retList )

		self.assertTrue( 'lastStatusCode' in retList )

		self.assertTrue( 'lastStatusMessage' in retList )

		self.assertTrue( 'lastStatusText' in retList )

		self.assertTrue( 'minAvailability' in retList )
		self.assertTrue( isinstance( retList['minAvailability']  ,float ))

		self.assertTrue( 'name' in retList )

		self.assertTrue( 'paramCookie' in retList )

		self.assertTrue( 'paramHeaderOnly' in retList )

		self.assertTrue( 'paramPasswd' in retList )

		self.assertTrue( 'paramPost' in retList )

		self.assertTrue( 'paramSearch' in retList )

		self.assertTrue( 'paramServer' in retList )

		self.assertTrue( 'paramServerType' in retList )

		self.assertTrue( 'paramUsername' in retList )

		self.assertTrue( 'parentId' in retList )

		self.assertTrue( 'publicStatActive' in retList )
		self.assertTrue( isinstance( retList['publicStatActive']  ,int ))

		self.assertTrue( 'rumIdent' in retList )

		self.assertTrue( 'serviceCheckType' in retList )

		self.assertTrue( 'serviceCheckTypeId' in retList )
		self.assertTrue( isinstance( retList['serviceCheckTypeId']  ,int ))

		self.assertTrue( 'siuxdbId' in retList )
		self.assertTrue( isinstance( retList['siuxdbId']  ,int ))

		self.assertTrue( 'sourceGroupId' in retList )
		self.assertTrue( isinstance( retList['sourceGroupId']  ,int ))

		self.assertTrue( 'sourceGroupName' in retList )

		self.assertTrue( 'sourceId' in retList )
		self.assertTrue( isinstance( retList['sourceId']  ,int ))

		self.assertTrue( 'sourceType' in retList )

		self.assertTrue( 'sourceTypeName' in retList )

		self.assertTrue( 'status' in retList )

		self.assertTrue( 'timeSchemeId' in retList )
		self.assertTrue( isinstance( retList['timeSchemeId']  ,int ))

		self.assertTrue( 'timeSchemeName' in retList )

		self.assertTrue( 'timeout' in retList )
		self.assertTrue( isinstance( retList['timeout']  ,int ))

		self.assertTrue( 'timeoutErr' in retList )
		self.assertTrue( isinstance( retList['timeoutErr']  ,int ))

		self.assertTrue( 'timeoutWarn' in retList )
		self.assertTrue( isinstance( retList['timeoutWarn']  ,int ))

		self.assertTrue( 'timezone' in retList )
		self.assertTrue( isinstance( retList['timezone']  ,int ))

		self.assertTrue( 'timezoneId' in retList )
		self.assertTrue( isinstance( retList['timezoneId']  ,int ))

		self.assertTrue( 'timezoneName' in retList )

		self.assertTrue( 'timezoneNick' in retList )

		self.assertTrue( 'url' in retList )

		self.assertTrue( 'urlNice' in retList )


	def testSourceInfo(self):
		"""
		Test tests correct api sourceList call
		"""

		# init
		S = siuxlib.SiUXclient( auth = self.auth )
		# source.list()

		retList = S.sourceList()
		#pprint.pprint( retList )

		if retList['statusCode'] == 'OK':

			if sys.version_info.major == 2 and sys.version_info.minor >= 7:
				self.assertGreater(retList['data'].__len__(),0)

			for line in retList['data']:

				sourceId = line['sourceId']

				self.assertTrue( isinstance( sourceId , int ) )

				sourceInfo = S.sourceInfo( sourceId )

				self.checkSourceInfo( sourceInfo['data'] )


if __name__ == '__main__':
    unittest.main()
