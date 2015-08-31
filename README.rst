SiUX
----

To use (with caution), simply do::

    >>> import sys
    >>> sys.path.append( '../siux' )
    >>> import siuxlib
    >>> auth = '<YOUR_API_KEY>'
    >>> S = siuxlib.SiUXclient( auth=auth )
    >>> retList = S.sourceList()
    >>> if retList[ 'statusCode' ] == 'OK':
    >>>    for line in retList[ 'data' ]:
    >>>       print line
