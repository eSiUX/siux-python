#!/usr/bin/python

import unittest, pprint, sys

sys.path.append( '../siux' )
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
		blacklist = ( 'sourceDropoutList', 'sourceStatDailyList', 'sourceStatMonthlyList', 'dropoutList',\
			'sourceStatList' , 'availabilityList', 'seleniumAdvancedList', 'seleniumList', 'sourceStatWeeklyList')
		
		for line in retMethod[ 'data' ]:

			# only list methods
			methodName = line['methodName']
			if not methodName.endswith( 'List' ):
				continue

			if methodName in blacklist:
				continue

			# run list method
			print line
			retList = self.runList( line['methodName'] )

			# method not implemented
			if retList[ 'status' ] == 501:
				continue

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

              	except Exception, emsg:

			msg501 = "SiUXclient instance has no attribute '%s'" % (method)
			if str(emsg) == msg501:
				return { 'status':501, 'statusMessage':'Not Implemented', 'errorMessage':str(emsg), 'statusCode':'NOT_IMPLEMENTED', 'found':0 }

                	return { 'status':500, 'statusMessage':'Server Error', 'errorMessage':str(emsg), 'statusCode':'SERVER_ERR', 'found':0 }
			
		return ret	

