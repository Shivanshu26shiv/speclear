<h2>speclear - delete specific history in major windows browsers</h2>

With speclear, you can delete sepcific history items in major installed browsers such as chrome, firefox, opera and safari in Windows.
For Internet explorer (IE), specific segregation is not possible hence speclear will delete <b>all history items</b>.

See below for more details.
<h3>Getting it:</h3>
To download speclear, either fork its github repo or simply use 
Pypi via pip.

	$ pip install speclear


<h3>Compatibility:</h3>
speclear is compatible for python version > 3.0

<h3>Package dependency:</h3>
speclear needs sqlite3 to access sqlite databases of browsers, though it is installed as a standard library of python 3. 

<h3>Using it:</h3>


Either via python module:

	import speclear
	speclear.delete_history('string-1', 'string-2',...)

Or via command line:

	C:\Program Files\Python37\speclear_pkg\speclear>python3 -m speclear string-1 string-2
	
Sample output:

	Info:: string(s) to be deleted: string-1 string-2 ...
	Warning:: for chrome (profile 1) database seems locked, please close the browser
	Info:: for chrome (profile 2), number of rows deleted is: 0
	Info:: for chrome (profile 3), number of rows deleted is: 0
	Info:: for firefox (profile 1), number of rows deleted is: 0
	Info:: Browser not found: opera
	Info:: Browser not found: safari
	Info:: IE cleared

<h3>Author contact:</h3>
<ul>
<li>LinkedIn: https://www.linkedin.com/in/shivanshu26shiv/</li>
</ul>
