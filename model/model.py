
import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
    def getAllRatings(self, min_rating, max_rating):
        # CHIEDI AL DAO I rating compresi nell' intervallo
        return DAO.getAllRatings(min_rating, max_rating)

    def buildGraph(self,min_rating,max_rating):

        self._graph.clear()
        attori = DAO.getActors(min_rating, max_rating) #FILTRO SULLA SCELTA DI MIN E MAX VIENE APPLICATO GIA' QUI
        for actor in attori:
            actor.Film=DAO.getFilmsByActor(actor.id)
        self._graph.add_nodes_from(attori)

        archi = DAO.getA1A2Peso(min_rating,max_rating)
        attoriMap={}
        for attore in attori:
            attoriMap[attore.id]=attore
        for a1,a2,peso in archi:
            actor1=attoriMap[a1]
            actor2=attoriMap[a2]
            self._graph.add_edge(actor1,actor2,weight=peso)



    def getNodes(self):
        return len(self._graph.nodes())

    def getEdges(self):
        return len(self._graph.edges())

