#!/usr/bin/python

import xmlrpclib, socket
import siuxmethodlib



class TimeoutTransport (xmlrpclib.Transport):
	"""
    	Custom XML-RPC transport class for HTTP connections, allowing a timeout in
    	the base connection.
    	"""

    	def __init__(self, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, use_datetime=0):
        	xmlrpclib.Transport.__init__(self, use_datetime)
        	self._timeout = timeout

    	def make_connection(self, host):
        	# If using python 2.6, since that implementation normally returns the 
        	# HTTP compatibility class, which doesn't have a timeout feature.
        	#import httplib
        	#host, extra_headers, x509 = self.get_host_info(host)
        	#return httplib.HTTPConnection(host, timeout=self._timeout)

        	conn = xmlrpclib.Transport.make_connection(self, host)
        	conn.timeout = self._timeout
        	return conn



class SiUXclient(siuxmethodlib.SiUXmethod):


	def __init__( self, auth='', timeout=10 ):
		""" init """

		# config
		self.repeat = 3
		url = 'http://api.esiux.net:3035/RPC2'

		# server connect
		t = TimeoutTransport(timeout=timeout)
		self.__server = xmlrpclib.ServerProxy( url, transport=t)

	
	def _call( self, methodName, *args ):
		""" call rpc method """

                for no in range( self.repeat+1 ):

                        try:
                                methodTest = getattr( self.__server, methodName )
                                ret = methodTest( *args )

                        # rpc error
                        except rpc.Fault, fe:
                                log.ni( 'RPC Err: method %s(%s) : %s [repeat=%d]', (methodName, str(args), fe, no), ERR=3 )
                                ret = { 'status':503, 'statusMessage':'Service Unavailable', 'errorMessage':str(fe) }

                        # method error
                        except Exception, msg:
                                log.ni( 'RPC Err: method %s(%s) : %s [repeat=%d]', (methodName, str(args), msg, no), ERR=3 )
                                ret = { 'status':500, 'statusMessage':'Server Error', 'errorMessage':str(msg) }
				

			if ret['status'] < 500:
				break


		return ret

	

if __name__ == '__main__':

	import pprint

	# config
	auth = '<YOUR_API_KEY>'

	# init
	S = SiUXclient( auth=auth )

	# test
	pprint.pprint( S.sourceList(auth) )

