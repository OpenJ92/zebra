from yaml import load, FullLoader
from os.path import expanduser

from src2.NODE.NODE import NODE
from src2.PIPE.PIPE import PIPE

class process(object):
    def __init__(self, conf = None):
        # how do we adjust s.t. we read from a directory of 
        # pipes / load files.
        self._config = self._process_config(conf)
        self._pipe = PIPE(self._config)

    def _process_config(self, conf):
        conf = f"{expanduser('~')}/.dt/config.yml" if not conf else f"{conf}" 
        with open(conf, 'r') as config:
            return load(config, Loader=FullLoader)

    def __step__(self):
        pass
