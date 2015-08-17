#!/usr/bin/python

import unittest, pprint, sys

sys.path.append( '../src' )
import siuxlib

class TestSummary(unittest.TestCase):

	# config
	auth = '<YOUR_API_KEY>'

	__siux = siuxlib.SiUXclient( auth=auth )


	def testMethod( self ):

		retMethod = self.__siux.methodList()
		return retMethod


	def testList( self ):

		# method list
		retMethod = self.__siux.methodList()

		# todo: bugfix
		blacklist = ( 'sourceDomainList', 'sourceDropoutList', 'sourceStatDailyList', 'sourceStatMonthlyList', 'dropoutList',\
			 'sourceStatList' , 'availabilityList', 'testValueList')
		
		for line in retMethod[ 'data' ]:

			# only list methods
			methodName = line['methodName']
			if not methodName.endswith( 'List' ):
				continue

			if methodName in blacklist:
				continue

			# run list method
			retList = self.runList( line['methodName'] )

			# test parameters
			self.assertTrue( 'status' in retList )
			self.assertTrue( 'statusCode' in retList )
			self.assertTrue( 'statusMessage' in retList )

			self.assertEqual( 200  , retList['status'] )
			self.assertEqual( 'OK' , retList['statusCode'] )


	def runList( self, method='' ):

		try:
			methodTest = getattr( self.__siux, method )
			ret = methodTest()
              	except Exception, msg:
                	return { 'status':500, 'statusMessage':'Server Error', 'errorMessage':str(msg), 'statusCode':'SERVER_ERR', 'found':0 }
			
		return ret	
