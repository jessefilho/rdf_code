import rdflib


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

for row in qres:
    print(row)
