=============
UC Calculator
=============

UC Calculator (CalCalc) provides a calculator that returns the 
value of any expression or query written given as a string. CalCalc
can interface with Wolfram|Alpha for more complex questions.  

CalCalc can be used from either the command line or imported from
within Python.  You might find it most useful for tasks involving 
simple arithmetic and also looking up constants (i.e. mass of the 
earth).  

Typical usage often looks like this::

    $ python CalCalc.py -s '34*28'
    $  952

    $ python CalCalc.py 'mass of the moon in kg'
    $  7.3459e+22

    ---- AND, from within Python ----
    >>> from CalCalc import calculate
    >>> calculate('34*20')
    >>> 952

    >>> from CalCalc import calculate
    >>> calculate('mass of the moon in kg',  return_float=True) * 10
    >>> 7.3459e+23
