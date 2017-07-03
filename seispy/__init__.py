import importlib

submodules = ["constants",
              "fm3d",
              "geometry",
              "topography",
              "ttgrid",
              "velocity"]
for submodule in submodules:
    importlib.import_module(".{}".format(submodule), package="seispy")
