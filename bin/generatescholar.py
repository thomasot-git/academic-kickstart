from scholarly import scholarly

search_query = scholarly.search_author('Thomas Ohlson Timoudas')
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

pubs = '{\n' + '"publication": [\n'

keys = {  'author' : "author",
          'title' : "title",
          'year' : "year",
          'journal' : "journal",
          'volume' : "volume",
          'pages' : "pages",
          'eprint' : "link" }

for pub in author.publications:
  pub.fill()

  pubInfo = '{\n'
  
  for key in keys:
    if key in pub.bib:
      pubInfo += keys[key] + ': ' + dequote( pub.bib[key] ) + '"\n'
  
  pubInfo += '}'
  
  print(pubInfo)
  
  pubs += pubInfo
  
pubs += ']\n}'

print(pubs)
  
file.write(pubs)

file.close()
