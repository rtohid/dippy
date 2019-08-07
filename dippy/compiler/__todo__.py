__doc__ = """
1. frontend: generate the IR- for now from Python, but it would be nice to make it 
    plugable so people can write their own transducers from other languages to dippy's IR.
2. optimizer: optimization based on:
    a. application domain.
    b. computation patterns.
    c. available resources in the launch environment.
    ...
3. backend: to generate PhySL from the (hopefully optimized) IR. 
"""
