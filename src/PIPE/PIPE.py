from src.NODE.NODE import NODE

class PIPE(object):
    def __init__(self, form):
        self._name, self._kwargs = *form.keys(), *form.values()
        self.__gen_nodes__(); 
        self._transformed = self.__execute__({'Data1':1, 'Data2':1})

    def __gen_nodes__(self):
        self._nodes = [NODE(kw) for kw in self._kwargs]
        self._nodes = {f"{self._name}_{node._name}": node \
                           for node in self._nodes}

    def __execute__(self, Xs):
        node = self._nodes[f"{self._name}_HEAD"]
        while True: 
            print(Xs, node._name)
            Xs = {                                                       \
                  name:                                                  \
                  (node._map._apply_(data) if name in node._on else data)\
                  for name, data in Xs.items()                           \
                  }
            if "TAIL" in node._name:
                return Xs
            node = self._nodes[f"{self._name}_{next(node)}"]
        return Xs
