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


	def __init__( self, auth='', timeout=0 ):
		""" init """

		if auth == '<YOUR_API_KEY>':
			auth = ''

		# read config
		self.__config( auth=auth, timeout=timeout )

		# server connect
		t = TimeoutTransport( timeout=self.__timeout )
		self.__server = xmlrpclib.ServerProxy( self.__url, transport=t)


	def __config( self, auth='', timeout=0 ):
		""" read data from config file """

		# default config
		self.__repeat = 3
		self.__url = 'http://api.esiux.net:3035/RPC2'

		# config filenames	
		filenames = [ 'siux.conf', '../siux.conf' ]
		if os.environ.get( 'SIUX_CONFIG_FILE' ):
			filenames.append( os.environ['SIUX_CONFIG_FILE'] )

		# filename exist?
		configFilename = None
		for filename in filenames:
			if os.path.isfile( filename ):
				configFilename = filename
		
		# default config
		if not configFilename:

			if not timeout:
				self.__timeout = 10

			self.__auth = auth

			return

		# config init
		cfg = ConfigParser.ConfigParser()
		cfg.read( configFilename )
		
		# server config
		self.__url = cfg.get( 'api', 'server' )
		self.__repeat = cfg.getint( 'api', 'repeat' )

		if not timeout:
			self.__timeout = cfg.getint( 'api', 'timeout' )
	
		# client config
		if not auth:
			self.__auth = cfg.get( 'client', 'auth' )

		return

	
	def _call( self, methodName, *args ):
		""" call rpc method """

		# if auth not input 
		if args[0] in ('', '<YOUR_API_KEY>') and self.__auth:
			a = list(args)
			a.remove( args[0] )
			a.insert(0, self.__auth )
			args = a

		# call rpc method
                for no in range( self.__repeat+1 ):

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

			time.sleep(1)

		return ret

	

if __name__ == '__main__':

	import pprint

	# config
	auth = '<YOUR_API_KEY>'

	# init
	S = SiUXclient( auth=auth )

	# test
	pprint.pprint( S.sourceList(auth) )

