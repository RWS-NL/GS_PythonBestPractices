# Python Best practices

## 1. Introduction to Python
Python is a high-level, interpreted, general-purpose programming language. It was created by Guido van Rossum, and released in 1991.

### 1.1. Comparison to other languages ( [source](https://www.w3schools.com/python/python_intro.asp) )

- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

### 1.2. When do we use Python?

- Scripting - ArcGis API for Python
- To automate the Gis Content (ArcGis Entterprise, Data Publishing, Deployment)
- Automating with ArcGIS Notebooks - Jupyter Notebook
- Quick data model transformations directly in a database (ESRI ArcPy toolbox)


## 2. Follow [PEP8](https://peps.python.org/pep-0008/) Guidelines
*Which guidelines are must-haves to include in the wiki?*

## 3. Python version
3.6.5

*Which Python version is currently installed in all environments? (Asked Erik) Always use ArcGIS Python*
## 4. Documentation in Python
> The general layout of the project and its documentation should be as follows:
```
project_root/
│
├── src/  # project source code
├── docs/ # documentation
├── cofg/ # config file
├── test_data
├── release
├── README
```
> Commenting: In general, commenting is describing your code to/for developers
```
# Code tells you how; Comments tell you why.
```

> Add the following snippet (Docstring) to the beginning of your Python script:
```
"""
-------------------------------------------------------------------------------
Name:				Name of Py script
Purpose:			Purpose of Py scripts
Author:				User(ADM account)

Created:			Date of creation
History:			19/04/2022 cruzg: Initial version
											09/05/2022 cruzg: ....
-------------------------------------------------------------------------------
"""
```


###  4.1. Functions & Classes
When a function/class is created, add the following snippet at the beginning as documentation:
```
def TestFunction(Var1, Var2):
	"""
	-------------------------------------------------------------------------------
	 Input, datatype, explanation:	
	 	Var1 (string): xxxx
	 	Var2 (numeric): xxxx 
		....
	 Output, datatype, explanation:
	 	Var3 (list): xxxx
		....
	-------------------------------------------------------------------------------
	"""
	
	PythonCode
	
	return(Var3)
```

## 5. Python IDE
PyCharm 2021.2.1. (Community edition) with Python 3.6.x from ArcGIS Pro 2.2.x

Location of Python executable: "D:\Apps\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

----------------------------------------------------------
## Handy Python snippets

### 


