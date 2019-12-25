class test():
    def __init__(self, form):
        self.__dict__.update(form)

    def __call__(self, X, form):
        self.__dict__.update(form)
        X = self.specific(X, **form)
        return X 

    def specific(self, X, param_c = 'q', \
            param_d = 'w', param_e = 'f'):
        X = X + 1
        return X
