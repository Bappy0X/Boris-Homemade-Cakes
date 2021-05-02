from importlib import import_module
from os import listdir, getcwd, path

blueprints = [
    import_module(f"routes.{i[:-3]}").bp 
    for i in listdir(path.dirname(__file__))
    if not i in ["__pycache__", "__init__.py"] 
        and i.endswith(".py")
]

# Recycled from my other project: https://github.com/Bappy0X/Modern-Amazon/blob/master/api/app/blueprints/__init__.py