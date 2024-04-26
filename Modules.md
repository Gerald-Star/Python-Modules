
# Modules are files containing Python code that other Python programs can use.

# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

# Within a module, the module’s name (as a string) is available as the value of the global variable __name__. 
# For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:
#

#? TWO TYPES OF MODULES

# 1. Built-in Modules
# 2. User-defined Modules

#? BUILT-IN MODULES

# Python has a set of built-in modules which you can use whenever you like. 
# Some of the most popular built-in modules in Python are:

# 1. os
# 2. sys
# 3. math
# 4. random
# 5. data time
# 6. JSON
# 7. RegEx
# 8. Email
# 9. SQLite3
# 10. tkinter

#? USER-DEFINED MODULES

# You can create your own modules in Python. A module can be written in Python itself. A module can define functions, classes, and variables. A module can also include runnable code.

# Example: Create a module called mymodule.py, and use the function greeting() in it:

# def greeting(name):
#   print("Hello, " + name)

# To use the module, we can import it using the import statement. The following example imports the mymodule module:

# import mymodule

# mymodule.greeting("Jonathan")

# Note: When using a function from a module, use the syntax: module_name.function_name.

#? NAMING A MODULE

# You can name the module file whatever you like, but it must have the file extension .py


#? RE-NAMING A MODULE

# You can create an alias when you import a module, by using the as keyword:

# import mymodule as mx

# mx.greeting("Jonathan")


#? USES CASES OF MODULES

# 1. You can use any Python source file as a module by executing an import statement in some other Python source file.
# 2. When the interpreter encounters an import statement, it imports the module if the module is present in the search path.

# The search path is a list of directories that the interpreter searches before importing a module.

# 3. To import a module, you can use the import statement. For example, to import the module support.py, 
# you need to put the following command at the top of the script:

#? import support

# print(help('modules'))# lists of modules available in python

#? PYTHON MODULE SEARCH PATH

# When you import a module, the Python interpreter searches for the module in the following sequences −

# 1. The current directory.

# 2. If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.

# 3. If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.


