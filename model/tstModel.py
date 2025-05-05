from model.model import Model

mymodel = Model()
mymodel.buildGraph()

print("N nodi:", mymodel.getNumNodes(), ", N edges:", mymodel.getNumEdges())