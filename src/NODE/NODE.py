from src2.MAP.MAP import MAP

class NODE(object):
    def __init__(self, form):
        self._name, self._kwargs = *form.keys(), *form.values()
        self.__dict__.update(self._kwargs); del self._kwargs
        self.__dict__.update(self._node); del self._node
        self._map = MAP(self._class, self._init, self._apply)
        del self._class; del self._init; del self._apply
        print(self._name)

    def __call__(self):
        return self._name, self._on, self._from, self._to, self

    def __next__(self):
        # call conditional next if it exists
        if hasattr(self, '_conditional_next'):
            print('Hello World!')
        return self._to[0]


if __name__ == "src2.NODE.NODE":
    pass

