# Python Best practices

## 1. Introduction to Python
Python is a high-level, interpreted, general-purpose programming language. It was created by Guido van Rossum, and released in 1991.

### *Comparison to other languages ([source](https://www.w3schools.com/python/python_intro.asp))*

- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

### *When do we use Python?*

- Scripting - ArcGis API for Python
- To automate the Gis Content (ArcGis Entterprise, Data Publishing, Deployment)
- Automating with ArcGIS Notebooks - Jupyter Notebook
- Quick data model transformations directly in a database (ESRI ArcPy toolbox)


## 2. Follow [PEP8](https://peps.python.org/pep-0008/) Guidelines
 PEP8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.
 
 In the sections below, the most important guidelines are described below, enriched with what's currently applied in Geostenen.
 

## 3. Python version
In Geostenen, we have older applications that rely on the ArcGIS Python 2.7 version. All newer application should use ArcGIS Python 3.6.5.

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

> Add the following snippet (Docstring) to the beginning of your Python script:
```python
"""
-------------------------------------------------------------------------------
Name:				Name of Py script
Purpose:			Purpose of Py scripts
Author:				User(ADM account)

Created:			Date of creation
History:			19/04/2022 cruzg: Initial version
-------------------------------------------------------------------------------
"""
```
Further edits should be documented when commiting to GitHub.


###  *Functions & Classes*
When a function/class is created, add the following snippet at the beginning as documentation:
```python
def my_function(Var1, Var2):
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
	
	print("This function is amazing!")
	
	return(Var3)
```
By giving the information above, each developer should know what the purpose, input and output are for each function or class.

### *Creating a logfile*
Usually, messages from Python script are printed in the console instead of in a seperate logging file. The module *logging* gives developers all the tools to write a logfile after running their code. The snippet below enables writing a logfile in the same directory as the code during its run.

```python
import logging
"""
filename = Name of the logfile
filemode = Which filemode is applied. 
 		W = overwrite existing logfile
format = Format of logging rows
level = Which level of logging is the threshold
"""

logging.basicConfig(filename='Test.log', 
		filemode='w', 
		format='%(name)s - %(levelname)s - %(message)s', 
		level= logging.WARN) 
					
logging.info('This will not get logged to a file')
logging.warn('This will get logged to a file')

```

The snippet above generates the log file content below:


*root - WARNING - This will get logged to a file*











## 5. Python IDE
PyCharm 2021.2.1. (Community edition) with Python 3.6.x from ArcGIS Pro 2.2.x

Location of Python executable: "D:\Apps\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

Visual Studio Code (Recommend): https://code.visualstudio.com/











## 6. Code Lay-Out
The PEP8 guidelines describe multiple ways to make the your code more readible and accesible for adjustments from other developers.

### Maximum line length
Try not make your code lines too long. The readibility and clarity of your code will be affected by having code lines exceed a certain length. According to the PEP8 guides, the code lines need to fit a single screen without side scrolling. Below, some examples are giving how to combat long code lines

```python
#### Long path names
bad_var = fcpath =  r"\\ad.rws.nl\test-dfs01\Appsdata\GEOstenen\mock-up\pathisverylong\subdir\file.txt"

good_var = os.path.join(
            r"\\ad.rws.nl\test-dfs01\Appsdata\GEOstenen",
            r"\mock-up\pathisverylong\subdir",
            r"file.txt")
			
#### Calling function/modules with variables
bad_var = arcpy.management.FeatureCompare(in_base_features = sourceDB, in_test_features = targetDB, sort_field = "OBJECTID", continue_compare = continue_compare,out_compare_file = "continue_compare")

good_var = arcpy.management.FeatureCompare(
			in_base_features = sourceDB,
			in_test_features = targetDB,
			sort_field = "OBJECTID",
			continue_compare = continue_compare,
			out_compare_file = "continue_compare")

#### Defining functions/classes
def my_bad_function(var1, var2, var3 = "default", var5, var6):
	print("Bad formatting!")

def my_good_function(var1, var2,
		     var3 = "default",
		     var5, var6):
	print("Great formatting!")

```

### Commenting in Python
Whenever you want to clarify your code, consider placing comments above the line to prevent long code lines. If you comment exceeds one line, then consider placing your comments in a docstring.

```python
# Simple comment to explain actions below
# Developers' name is defined.
dev_name = "John Doe"
```

```python
"""
Docstring
The standard deviation is calculated by taking the root of 
the variance.
To calculate the variance, the mean of your sample is needed.
"""

import math

# values (must be floats!)
xs = [0.5,0.7,0.3,0.2]   

  
mean = sum(xs) / len(xs) 
var  = sum(pow(x-mean,2) for x in xs) / len(xs)

# standard deviation
std  = math.sqrt(var)  
```













## 7. Config file: What's the best practice using a settings file in Python?
The most common and standardized format is JSON. A good configuration file should meet at least these 3 criteria:

- Easy to read and edit: It should be text-based and structured in such a way that is easy to understand. Even non-developers should be able to read.
- Allow comments: Configuration file is not something that will be only read by developers. It is extremely important in production when non-developers try to understand the process and modify the software behavior. Writing comments is a way to quickly explain certain things, thus making the config file more expressive.
- Easy to deploy: Configuration file should be accepted by all the operating systems and environments. It should also be easily shipped to the server via a CDaaS pipeline.

Quick Start

Let’s take a very basic configuration file that looks like this:

config.py (config - settings file)

```python
	# database connection
	database = dict(
		username = 'db_username',
		password = 'db_password',
		host = '127.0.0.1',
		port = '5432',
		db = 'db_name'
	)
	# application settings
	app = dict(
		envirement = 'test',
		engine = dict(
			debug = True,
			displau = False,
    )
```

app.py (application file)

```python
	# import config - settings
	import config

	# get db username
	db_username = config.database['username']
	print(f'db username: {db_username}')

	# get db password
	db_password = config.database['password']
	print(f'db password: {db_password}')
```

output result should be like this:

```
	db username: db_username
	db password: db_password
```


