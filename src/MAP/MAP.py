class MAP(object):
    def __init__(self, _class, _init, _apply):
        self._class = _class
        self._init = _init
        self._apply = _apply

    def _import_(self, package, name):
        return getattr(__import__(package, fromlist=[name]), name)

    def _init_(self):
        return self._import_(**self._class)(self._init)

    def _apply_(self, X):
        return self._init_()(X, self._apply)
