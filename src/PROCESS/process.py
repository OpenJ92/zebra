from yaml import load, FullLoader
from os.path import expanduser
from os import listdir

from src.NODE.NODE import NODE
from src.PIPE.PIPE import PIPE

class process(object):
    """ Pull configuration files and reform them into PIPES

    Attributes
    ==========
    conf : str
        path configuration directory of pipe.yml files.
    _pipes : list : str
        pipe.yml files in configuration directory
    _confs: list : dict
        loaded configuration dictionaries
    pipes : list : src.PIPE.PIPE.PIPE
        pipe objects formed from loaded configuration files. 
    """
    def __init__(self, conf = None):
        self._conf = conf
        self._pipes = [f"./NETWORK/{pipe}"             \
                 for pipe in listdir('./NETWORK')      \
                 if "PIPE" in pipe]
        self._confs = [self._process_config(pipe) for pipe in self._pipes]
        pipes = [PIPE(conf) for conf in self._confs]
	

    def _process_config(self, conf):
        conf=f"{expanduser('~')}/.dt/config.yml"      \
                if not conf else                      \
                f"{self._conf}" 			      
        with open(conf, 'r') as config:
            return load(config, Loader=FullLoader)

    def __step__(self):
        pass
