# import dependencies
import sys, keyword

# display python version
print('Python Version:', sys.version)

# display actual location on system of python interpreter
print('Python Interpreter Location:', sys.executable)

# display a list of all directories where Python interpreter looks for modules 
print('Python Module Search Path:')
for folder in sys.path:
    print(folder)

# display list of all python keywords
print('Python Keywords:')
for word in keyword.kwlist:
    print(word)

