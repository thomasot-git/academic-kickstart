import sys
import json
from scholarly import scholarly

search_query = scholarly.search_author('Rong Du')
author = next(search_query).fill()

# print(author)

# Take a closer look at the first publication

file = open("publications.json","w")

for pub in author.publications
  pub.fill()
  print(pub)
  pubInfo = '{\n'
  pubInfo += '"author": ' + pub.bib['author'] + '\n'
  pubInfo += '"title": ' + pub.bib['title'] + '\n'
  pubInfo += '}'
  file.write(pub)

file.close()
