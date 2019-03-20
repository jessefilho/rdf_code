import rdflib


g=rdflib.Graph()
#g.load('http://dbpedia.org/resource/Semantic_Web')
g.load('human.rdf')


for s,p,o in g:
    print s,p,o