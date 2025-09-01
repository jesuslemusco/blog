# This file is only used for publishing to production
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Set the SITEURL to your final production URL.
# This is the root of your GitHub Pages site.
SITEURL = 'https://jesuslemus.co'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'

# It's a good practice to delete the output directory before building for production
DELETE_OUTPUT_DIRECTORY = True
