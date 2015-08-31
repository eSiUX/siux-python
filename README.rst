SiUX
----

To use (with caution), simply do::

    >>> import funniest
    >>> import sys
    >>> sys.path.append( '../src' )
    >>> import siuxlib
    >>> auth = '<YOUR_API_KEY>'
    >>> S = siuxlib.SiUXclient( auth=auth )
    >>> retList = S.sourceList()
    >>> if retList[ 'statusCode' ] == 'OK':
    >>>    for line in retList[ 'data' ]:
    >>>       print line
