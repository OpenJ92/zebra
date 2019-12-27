from yaml import load, FullLoader
from os.path import expanduser
from os import listdir

from src.NODE.NODE import NODE
from src.PIPE.PIPE import PIPE

class process(object):
    def __init__(self, conf = None):
        self._pipes = [f"./NETWORK/{pipe}"             \
                 for pipe in listdir('./NETWORK')      \
                 if "PIPE" in pipe]
        self._confs = [self._process_config(pipe) for pipe in self._pipes]
        pipes = [PIPE(conf) for conf in self._confs]

       # self._config = self._process_config(conf)
       # self._pipe = PIPE(self._config)

    def _process_config(self, conf):
        conf=f"{expanduser('~')}/.dt/config.yml"      \
                if not conf else                      \
                f"{conf}" 
        with open(conf, 'r') as config:
            return load(config, Loader=FullLoader)

    def __step__(self):
        pass
