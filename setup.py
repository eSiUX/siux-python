from distutils.core import setup
import sys

if sys.version_info < (2, 7):
    sys.exit("Python 2.7 or newer is required for siux-python")

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
  name = 'siux',
  packages = ['siux'], # this must be the same as the name above
  version = '0.1',
  description = 'Python API library for SiUX (website monitoring)',
  long_description=readme(),
  author = 'Erik Brozek',
  author_email = 'hellocode@esiux.com',
  url = 'https://github.com/eSiUX/siux-python/', # use the URL to the github repo
  download_url = 'https://github.com/eSiUX/siux-python/archive/master.zip', # I'll explain this in a second
  keywords = ['monitoring', 'testing', 'website' ], # arbitrary keywords
  license='MIT',
  classifiers = [
    	# How mature is this project? Common values are
    	#   3 - Alpha
    	#   4 - Beta
    	#   5 - Production/Stable
    	'Development Status :: 4 - Beta',

	# MIT license
	'License :: OSI Approved :: MIT License',

	# List trove classifiers
	'Topic :: System :: Monitoring',
	
	# Specify the Python versions you support here. In particular, ensure
    	# that you indicate whether you support Python 2, Python 3 or both.
 	'Programming Language :: Python :: 2',
    	'Programming Language :: Python :: 2.6',
    	'Programming Language :: Python :: 2.7'
  ],
)
