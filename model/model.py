
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

    def getArtistMaxDegree(self):
        # TROVO L'ARTISTA CON IL GRADO MAGGIORE
        actor = max(self._graph.nodes, key=self._graph.degree)  # GRADO: proprietà di un nodo
        grado = self._graph.degree(actor)
        return actor, grado

    def getArtistMaxWeight(self):
        # TROVO L'ARTISTA CON LA SOMMA DEI PESI (DEGLI ARCHI INCIDENTI) MASSIMA
        artist= max(
            self._graph.nodes,
            # per ogni rtista a calcola questa somma sum
            key=lambda a: sum(
                self._graph[a][neighbor]["weight"]
                # (3) DAMMI L'ARCO CHE COLLEGA a con quel neighbor, in particolare weight
                # (2) for neighbor in "prendi uno alla volta"
                for neighbor in self._graph.neighbors(a)  # (1) dammi tutti gli artisti collegati all'artista a
            )
        )
        # CALCOLO LA SOMMA DEI PESI DELL'ARTISTA TROVATO
        somma = sum(
            self._graph[artist][neighbor]["weight"]
            for neighbor in self._graph.neighbors(artist)
        )

        return artist, somma

    def getTop5Edges(self):
        # RECUPERO TUTTI GLI ARCHI DEL GRAFO CON IL LORO PESO
        edges = list(self._graph.edges(data=True))

        # ORDINO GLI ARCHI:
        # PRIMA PER PESO DECRESCENTE
        # IN CASO DI PARITÀ PER NOME DEL PRIMO ARTISTA
        # E POI PER NOME DEL SECONDO ARTISTA
        edges.sort(
            key=lambda e: (-e[2]["weight"], e[0].name, e[1].name)
        )

        # RESTITUISCO SOLO I PRIMI 10 ARCHI
        return edges[:5]

    def getYoungestActor(self):
        # Escludo gli attori senza data di nascita
        candidates = [
            a for a in self._graph.nodes
            if a.date_of_birth is not None
        ]

        # Se non ci sono date disponibili, restituisco None
        if not candidates:
            return None

        # La data più recente identifica l'attore più giovane
        return max(candidates, key=lambda a: a.date_of_birth)

    def getOldestActor(self):
        # Escludo gli attori senza data di nascita
        candidates = [
            a for a in self._graph.nodes
            if a.date_of_birth is not None
        ]

        # Se non ci sono date disponibili, restituisco None
        if not candidates:
            return None

        # La data più vecchia identifica l'attore più anziano
        return min(candidates, key=lambda a: a.date_of_birth)
