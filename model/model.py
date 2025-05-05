import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap = {}
        for v in self._nodes:
            self._idMap[v.id] = v

    def getInfoConnessa(self, idInput):
        """
        Identifica la componente connessa che contiene idInput e ne restiutisce la dimensione
        """
        if not self.hasNode(idInput):
            return None

        source = self._idMap[idInput]

        #modo 1: conto i successori
        succ = nx.dfs_successors(self._graph, source).values()
        res = []
        for s in succ:
            res.extend(s)
        print("Size connessa con modo 1:", len(res))

        # modo 2: conto i predecessori
        pred = nx.dfs_predecessors(self._graph, source)
        print("Size connessa con modo 2:", len(pred.values()))

        # modo 3: conto i nodi dell'albero di visita
        dfsTree = nx.dfs_tree(self._graph, source)
        print("Size connessa con modo 3:", len(dfsTree.nodes()))

        # modo 4: uso il metodo nodes connected components di networkx
        conn = nx.node_connected_component(self._graph, source)
        print("Size connessa con modo 4:", len(conn))

    def hasNode(self,idInput):
        #return self._idMap[idInput] in self._graph
        return idInput in self._idMap


    def buildGraph(self):
        self._graph.add_nodes_from(self._nodes)
        self.addAllEdges()

    def addEdgesV1(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getPeso(u,v)
                if peso is not None:
                    self._graph.add_edge(u, v, weight = peso)

    def addAllEdges(self):
        allEdges = DAO.getAllArchi(self._idMap)
        for e in allEdges:
            self._graph.add_edge(e.o1,e.o2,weight = e.peso)


    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getIdMap(self):
        return self._idMap

    def getObjectFromId(self,idInput):
        return self._idMap[idInput]