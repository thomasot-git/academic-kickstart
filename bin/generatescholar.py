import sys
import json
from scholarly import scholarly

search_query = scholarly.search_author('Carlo Fischione')
author = next(search_query).fill()

# Take a closer look at the first publication
pub = author.publications[0].fill()

file = open("publications.json","w")
file.write(pub)
file.close()