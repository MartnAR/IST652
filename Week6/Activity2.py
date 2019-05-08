# Parse xml site 
# Load libraries 
from urllib import request 
import xml.etree.ElementTree as etree
import io 

url = "https://kodi.wiki/view/RssFeeds.xml" 


xmlstring = request.urlopen(url).read().decode("utf8")
len(xmlstring)
xmlstring[:200]

xmlfile = io.StringIO(xmlstring)
tree = etree.parse(xmlfile)

"""
Find some websites that give RSS feeds, noting that some use the XML given in the ATOM specification. Then choose one and use urllib.request to get the document.

Use ElementTree to parse the document and choose some tags to obtain. You can do something simple like get the title tags. Please submit your code and your output, 
but please print only a small amount, for example the first 10 tags. Or you may choose to find some other content from the xml document.

Once you have submitted your code and results, look at those of two or three of your fellow classmates to see what they did.
"""