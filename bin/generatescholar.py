import sys
import json
from scholarly import scholarly

search_query = scholarly.search_author('Rong Du')
author = next(search_query).fill()

# print(author)

# print(author.publications[0].bibtex)

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
  pubInfo += '"year": "' + dequote( pub.bib['year'] ) + '"\n'
  
  if 'journal' in pub.bib:
    pubInfo += '"journal": "' + dequote( pub.bib['journal'] ) + '"\n'
  
  if 'volume' in pub.bib:
    pubInfo += '"volume": "' + dequote( pub.bib['volume'] ) + '"\n'
  
  if 'pages' in pub.bib:
    pubInfo += '"pages": "' + dequote( pub.bib['pages'] ) + '"\n'
  
  if 'eprint' in pub.bib:
    pubInfo += '"link": "' + dequote( pub.bib['eprint'] ) + '"\n'
  
  # pubInfo += '"bibtex": ' + dequote( pub.bibtex ) + '"\n'
  pubInfo += '}'
  
  print(pubInfo)
  file.write(pubInfo)

file.close()
