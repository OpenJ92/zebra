# zebra

Machine Learning Pipeline manager. The user constructs a set of PIPEs
and LOAD forms in an internal PIPES/ directory. These pipes are effective
conditional directed acyclic graphs whose nodes are user written 
python classes treated as stateful functions. zebra takes these forms 
and executes them as directed.
