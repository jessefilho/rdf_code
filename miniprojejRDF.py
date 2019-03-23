#!/usr/bin/python
# -*- coding: utf8 -*-
import rdflib
import rdflib as rd
from rdflib import Namespace

#Goals of this script

#1 - programme simple comment exploiter	par	programme un jeu de	données RDF	et RDFS
#2 - ouvrir [DONE]
#3 - modifier [TO DO]
#4 - sauvegarder [TO DO]
#5 - rechercher	des	parties [DOING]
#6 - les exploiter d’une manière ou	d’une autre	et sauvegarder les résultats obtenus [DONE]
#7 - tester	des	requêtes SPARQL, sans schéma en	RDFS [TO DO]
#8 - tester	des	requêtes SPARQL, avec schéma en	RDFS [TO DO]


#PREDICATES OF humans
# 'http://www.inria.fr/2007/09/11/humans.rdfs#trouserssize'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#shirtsize'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#name'
# 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#hasChild'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#shoesize'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#hasSpouse'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#hasParent'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#hasFriend'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#hasFather'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#age'
# 'http://www.inria.fr/2007/09/11/humans.rdfs#hasMother'

# ------------------------------------- START #1 [DONE]
g=rdflib.Graph()
#g.load('http://dbpedia.org/resource/Semantic_Web')
#g.load('human.rdf')
g.parse('human.rdf')

# ------------------------------------- #2 [DONE]
#for s,p,o in g:
#    print s,p,o
# ------------------------------------- #3 [DOING]
# I will add data of ?name ?pointure ?shirtsize ?age ?shoesize ?trouserssize
#

humans = Namespace("http://www.inria.fr/2007/09/11/humans.rdfs#")

laura = rd.URIRef("http://www.inria.fr/2007/09/11/humans.rdfs-instances#Laura")
lauraShirtsize = rd.Literal('10')
lauraAge = rd.Literal('39')
lauraShoesize = rd.Literal('11')
lauraTrouserssize = rd.Literal('36')

modifG = rd.Graph()

modifG.bind('humans', humans, False)

modifG.add((laura, humans.shirtsize, lauraShirtsize))
modifG.add((laura, humans.age, lauraAge))
modifG.add((laura, humans.shoesize, lauraShoesize))
modifG.add((laura, humans.trouserssize, lauraTrouserssize))

print "Parents, forward from `ex:person`:"
for i in modifG.transitive_objects(laura,humans.shirtsize):
    print i

# fp = open('human_withLauraUPDATE.rdf','wb')
# fp.write(g.serialize(format='turtle'))
# fp.close()



# ck_uptd_g=rdflib.Graph()
# ck_uptd_g.parse('human_withLauraUPDATE.rdf')
# qres = ck_uptd_g.query(
#     """
#     PREFIX humans: <http://www.inria.fr/2007/09/11/humans.rdfs#>
#     PREFIX xsd:    <http://www.w3.org/2001/XMLSchema#>
#
#     select ?name ?shirtsize ?age ?shoesize ?trouserssize
#     where {
#     ?x humans:name ?name .
#     ?x humans:shirtsize ?shirtsize .
#     ?x humans:age ?age .
#     ?x humans:shoesize ?shoesize .
#     ?x humans:trouserssize ?trouserssize .
#
#     FILTER (xsd:string(?name) = "Laura" )
#     }
#     """)
#
# if len(qres) == 0:
#     print("None results")
# else :
#     for row in qres:
#         print('name:%s pointure:%s shirtsize:%s age:%s shoesize:%s trouserssize:%s' % row)


# ------------------------------------- #6 [DONE]
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



qres = g.query(
    """
    PREFIX humans: <http://www.inria.fr/2007/09/11/humans.rdfs#>
    PREFIX xsd:    <http://www.w3.org/2001/XMLSchema#>

    SELECT ?name ?friend ?mother
    WHERE {
    ?name humans:hasFriend ?friend .
    ?name humans:name "David"
    
    
    }
    """)

# for row in qres:
#     print('name:%s friend:%s' % row)

#g.serialize(destination='output.txt', format='turtle')