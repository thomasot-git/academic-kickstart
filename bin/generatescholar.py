import sys
import json
from scholarly import scholarly

search_query = scholarly.search_author('Rong Du')
author = next(search_query).fill()

# print(author)

# Take a closer look at the first publication

def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

file = open("publications.json","w")

for pub in author.publications:
  pub.fill()

  pubInfo = '{\n'
  pubInfo += '"author": "' + dequote( pub.bib['author'] ) + '"\n'
  pubInfo += '"title": "' + dequote( pub.bib['title'] ) + '"\n'
  
  if pub.bib['journal']:
    pubInfo += '"journal": "' + dequote( pub.bib['journal'] ) + '"\n'
  
  pubInfo += '"volume": "' + myJSONClean( pub.bib['volume'] ) + '"\n'
  pubInfo += '"year": "' + myJSONClean( pub.bib['year'] ) + '"\n'
  pubInfo += '"pages": "' + myJSONClean( pub.bib['pages'] ) + '"\n'
  pubInfo += '"link": "' + myJSONClean( pub.bib['eprint'] ) + '"\n'
  pubInfo += '"bibtex": ' + dequote( pub.bibtex ) + '"\n'
  pubInfo += '}'
  
  print(pubInfo)
  file.write(pubInfo)

file.close()
