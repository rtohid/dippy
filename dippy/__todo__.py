__doc__ = """
diSTRIBUTEDpARALLELpyTHON (dippy)

Please NOTE:
1. this is a rough sketch of the environmnet that Phylanx will run on.
2. I have used Pythonesque directory structure as it is easier to follow, but we probably
   end up implementing most of the functionalities in HPX/Phylanx.
3. I just picked a silly name so there are no assumptions/confusions with the existing
   functionalities.

Quick Overview:
1. the frontend generates the IR from the user program.
2. the compiler optimizer optimizes the execution tree based on launching environment and
   the domain of the application.
3. the backend generates the PhySL code for each node of the launch environment and
   configures the runtime accordingly.
4. the application is launched with an appropriate, domain-configured runtime.
5. runtime runs the application and (optiobally) collects performance data.
6. (optional) the performance data is fed to the visualization module.
7. final results are return to the user- maybe as files(?)
"""
