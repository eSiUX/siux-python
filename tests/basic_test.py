import unittest,pprint,sys
sys.path.append( '../src' )
import siuxlib

class TestStringMethods(unittest.TestCase):

	# config
	auth = '<YOUR_API_KEY>'

	def checkBasicStructure( self , retList ):
		"""
		Method tests basic structure for OK api return call
		:param retList: - structure reported by API
		"""
		self.assertTrue( 'status' in retList )
		self.assertTrue( 'statusCode' in retList )
		self.assertTrue( 'statusMessage' in retList )
		self.assertTrue( 'time' in retList )
		self.assertTrue( 'found' in retList )
		self.assertTrue( 'deactiveNo' in retList )
		self.assertTrue( 'activeNo' in retList )
		self.assertTrue( 'cacheTime' in retList )
		self.assertTrue( 'data' in retList )

	def checkSourceInfo( self,retList ):
		"""
		Method tests sourceInfo structure
		:param retList: - structure reported by API
		"""
		self.assertTrue( 'clientId' in retList )
		self.assertTrue( 'domainId' in retList )
		self.assertTrue( 'lastChecktime' in retList )
		self.assertTrue( 'lastErrChecktime' in retList )
		self.assertTrue( 'lastErrNo' in retList )
		self.assertTrue( 'lastErrStatusCode' in retList )
		self.assertTrue( 'lastErrStatusText' in retList )
		self.assertTrue( 'lastStatusCode' in retList )
		self.assertTrue( 'lastStatusText' in retList )
		self.assertTrue( 'name' in retList )
		self.assertTrue( 'parentId' in retList )
		self.assertTrue( 'sourceId' in retList )
		self.assertTrue( 'sourceType' in retList )
		self.assertTrue( 'sourceTypeName' in retList )
		self.assertTrue( 'status' in retList )
		self.assertTrue( 'timeout' in retList )
		self.assertTrue( 'timeoutErr' in retList )
		self.assertTrue( 'timeoutWarn' in retList )
		self.assertTrue( 'url' in retList )
		self.assertTrue( 'urlNice' in retList )


	def testApiListOK(self):
		"""
		Test tests correct api sourceList call
		"""

		# init
		S = siuxlib.SiUXclient( auth = self.auth )
		# source.list()

		retList = S.sourceList()
		#pprint.pprint( retList )

		self.checkBasicStructure( retList )

		if retList['statusCode'] == 'OK':

			for line in retList['data']:

				sourceId = line['sourceId']

				self.assertTrue( isinstance( sourceId , int ) )

				sourceInfo = S.sourceInfo( sourceId )

				self.checkSourceInfo( line )


	def testApiNotOK(self):
		"""
		Test tests correct api unauthorized sourceList call
		"""

		# init
		S = siuxlib.SiUXclient( auth = "" )
		# source.list()

		retList = S.sourceList()
		#pprint.pprint( retList )

		self.assertTrue( 'status' in retList )
		self.assertEqual( 401 , retList['status'])

		self.assertTrue( 'statusCode' in retList )
		self.assertEqual( 'UNAUTHORIZED' , retList['statusCode'] )

		self.assertTrue( 'statusMessage' in retList )
		self.assertEqual( 'Unauthorized' , retList['statusMessage'] )

		self.assertTrue( 'time' in retList )
		self.assertTrue( 'time' in retList )




if __name__ == '__main__':
    unittest.main()