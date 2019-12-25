# how is this going to work? II need to make HEAD and TAIL nodes for 
# each pipe that's aware of the PIPE it came from and the PIPE it's
# going to. They start execution and either begin or end execution 
# of the system. 

# I don't think this will be a proper yml. file. There's a need to 
# process the configuration of the individual pipes. 

class HEAD(object):
    def __init__(self, form):
