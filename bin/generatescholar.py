import sys
import json
from scholarly import scholarly

search_query = scholarly.search_author('Carlo Fischione')
author = next(search_query).fill()

# print(author)

# Take a closer look at the first publication
pub = author.publications[0].fill()

print(pub)

#class MyEncoder(JSONEncoder):
#        def default(self, o):
#            return o.__dict__

#MyEncoder().encode(f)

file = open("publications.json","w")
file.write("a")
# file.write(json.dumps(pub))
file.close()
