#!/usr/bin/python

import xmlrpclib, socket, ConfigParser, os, os.path, time
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

		self._auth = auth

		# default config
		self.__repeat = 3
		self.__url = 'http://api.esiux.net:3035/RPC2'

		# server connect
		t = TimeoutTransport( timeout=timeout )
		self.__server = xmlrpclib.ServerProxy( self.__url, transport=t)

	
	def _call( self, methodName, *args ):
		""" call rpc method """

		# call rpc method
                for no in range( self.__repeat+1 ):

                        try:
                                methodTest = getattr( self.__server, methodName )
                                ret = methodTest( *args )

                        # rpc error
                        except rpc.Fault, fe:
                                log.ni( 'RPC Err: method %s(%s) : %s [repeat=%d]', (methodName, str(args), fe, no), ERR=3 )
                                ret = { 'status':503, 'statusMessage':'Service Unavailable', 'errorMessage':str(fe), 'statusCode':'SERVER_UNAVAILABLE', 'found':0 }

                        # method error
                        except Exception, msg:
				if msg == "SiUXclient instance has no attribute '%s'" % (methodName):
                                	log.ni( 'RPC Err: method %s(%s) : %s [repeat=%d]', (methodName, str(args), msg, no), ERR=3 )
                                	ret = { 'status':501, 'statusMessage':'Not Implemented', 'errorMessage':str(msg), 'statusCode':'NOT_IMPLEMENTED', 'found':0 }
					break
			
				log.ni( 'RPC Err: method %s(%s) : %s [repeat=%d]', (methodName, str(args), msg, no), ERR=3 )
				ret = { 'status':500, 'statusMessage':'Server Error', 'errorMessage':str(msg), 'statusCode':'SERVER_ERR', 'found':0 }
			

			if ret['status'] < 500:
				break

			time.sleep(1)

		return ret


	def methodList( self ):
		"list methods for SiUX api"
	
		try:
			listMethod = self.__server.system.listMethods()

              	except rpc.Fault, fe:
                	log.ni( 'RPC Err: method system.listMethods() : %s', (fe,), ERR=3 )
                      	ret = { 'status':503, 'statusMessage':'Service Unavailable', 'errorMessage':str(fe), 'statusCode':'SERVER_UNAVAILABLE', 'found':0 }

              	except Exception, msg:
                	log.ni( 'RPC Err: method system.listMethods() : %s', (msg,), ERR=3 )
                	return { 'status':500, 'statusMessage':'Server Error', 'errorMessage':str(msg), 'statusCode':'SERVER_ERR', 'found':0 }

		data = []
		found = 0
		for methodName in listMethod:

			if methodName.startswith( 'system.'):
				continue

			methods = []
			no = 0
			for name in methodName.split('.'):
				if no == 0:
					methods.append( name.lower() )
				else:
					methods.append( '%s%s' % (name[0].upper(), name[1:].lower()) )
				no = no + 1
			method = ''.join(methods)

			data.append( {'methodName':method} )
			found = found + 1

                return { 'status':200, 'statusMessage':'OK', 'statusCode':'OK', 'data':data, 'found':found }


if __name__ == '__main__':

	import pprint

	# config
	auth = '<YOUR_API_KEY>'

	# init
	S = SiUXclient( auth=auth )

	# test method list
	pprint.pprint( S.methodList() )

	# test method
	pprint.pprint( S.sourceList() )
