import sys
import json
from scholarly import scholarly

search_query = scholarly.search_author('Rong Du')
author = next(search_query).fill()

# print(author)

# Take a closer look at the first publication
pub = author.publications[4].fill()

print(pub)

file = open("publications.json","w")
file.write(json.dumps(pub))
file.close()
