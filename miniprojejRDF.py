import rdflib


#Goals of this script

#1 - programme simple comment exploiter	par	programme un jeu de	données RDF	et RDFS
#2 - ouvrir [DONE]
#3 - modifier [TO DO]
#4 - sauvegarder [TO DO]
#5 - rechercher	des	parties [DOING]
#6 - les exploiter d’une manière ou	d’une autre	et sauvegarder les résultats obtenus [DOING]
#7 - tester	des	requêtes SPARQL, sans schéma en	RDFS [TO DO]
#8 - tester	des	requêtes SPARQL, avec schéma en	RDFS [TO DO]

g=rdflib.Graph()
#g.load('http://dbpedia.org/resource/Semantic_Web')
#g.load('human.rdf')
g.parse('human.rdf')


#for s,p,o in g:
#    print s,p,o

qres = g.query(
"""
PREFIX humans: <http://www.inria.fr/2007/09/11/humans.rdfs#>
PREFIX xsd:    <http://www.w3.org/2001/XMLSchema#>
	
SELECT ?name ?pointure ?shirtsize ?age ?shoesize ?trouserssize
WHERE {
?x humans:name ?name .
?x humans:shirtsize ?shirtsize .
?x humans:age ?age .
?x humans:shoesize ?shoesize .
?x humans:trouserssize ?trouserssize .

FILTER (xsd:string(?name) = "John" )
}
""")


#for row in qres:
#    print("Name: %s Pointure: %s shirtsize:%s Age:%s shoesize:%s trouserssize:%s" % row)

#List predicates:
qres = g.query(
    """
    PREFIX humans: <http://www.inria.fr/2007/09/11/humans.rdfs#>
    PREFIX xsd:    <http://www.w3.org/2001/XMLSchema#>
    
    SELECT DISTINCT ?predicate
    WHERE {
    ?s ?predicate ?o
    }
    """)

# for row in qres:
#     print(row)


'http://www.inria.fr/2007/09/11/humans.rdfs#trouserssize'
'http://www.inria.fr/2007/09/11/humans.rdfs#shirtsize'
'http://www.inria.fr/2007/09/11/humans.rdfs#name'
'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
'http://www.inria.fr/2007/09/11/humans.rdfs#hasChild'
'http://www.inria.fr/2007/09/11/humans.rdfs#shoesize'
'http://www.inria.fr/2007/09/11/humans.rdfs#hasSpouse'
'http://www.inria.fr/2007/09/11/humans.rdfs#hasParent'
'http://www.inria.fr/2007/09/11/humans.rdfs#hasFriend'
'http://www.inria.fr/2007/09/11/humans.rdfs#hasFather'
'http://www.inria.fr/2007/09/11/humans.rdfs#age'
'http://www.inria.fr/2007/09/11/humans.rdfs#hasMother'

qres = g.query(
    """
    PREFIX humans: <http://www.inria.fr/2007/09/11/humans.rdfs#>
    PREFIX xsd:    <http://www.w3.org/2001/XMLSchema#>

    SELECT ?name ?friend
    WHERE {
    ?name humans:hasFriend ?friend
    
    }
    """)

for row in qres:
    print('name:%s friend:%s' % row)

