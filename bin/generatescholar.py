import sys
import json
from scholarly import scholarly

search_query = scholarly.search_author('Rong Du')
author = next(search_query).fill()

# print(author)

# Take a closer look at the first publication

file = open("publications.json","w")

for pub in author.publications:
  pub.fill()
  print(pub)
  pubInfo = '{\n'
  pubInfo += '"author": ' + pub.bib['author'] + '\n'
  pubInfo += '"title": ' + pub.bib['title'] + '\n'
  
  if pub.bib['journal']:
    pubInfo += '"journal": ' + pub.bib['journal'] + '\n'
  
  pubInfo += '"link": ' + pub.bib['elink'] + '\n'
  pubInfo += '}'
  file.write(json.dumps(pub))

file.close()
