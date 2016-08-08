import re
import linkGrabber

links = linkGrabber.Links('http://google.com/')
gb = links.find(limit = 4, pretty = True)

for link in gb:
    print link
