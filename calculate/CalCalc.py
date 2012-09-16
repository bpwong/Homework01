#/usr/bin/env python

import argparse, sys, urllib, urllib2
from xml.etree import ElementTree as etree
'''
calculate() evaluates any string passed to it, and can be used
from either the command line (using argparse with reasonable flags)
or imported within Python.

calculate(in0, return_float = False):
    -in0 : a string that is to be calculated
    -return_float : return a float instead of a string, if possible

Tags:
    -s   : denotes a string input
    -fl  : indicates that a float will be returned, if possible  

sample usage:
    $ python CalCalc.py "mass of the moon in kg"
    $  7.3459e+22
    ---- AND, from within Python ----
    >>> from CalCalc import calculate
    >>> calculate("mass of the moon in kg",  return_float=True) * 10
    >>> 7.3459e+23
'''

# Credit to http://advencode.wordpress.com/2011/10/17/simple-query-request-with-wolfram-api/
# _get_xml() and _xmlparser from the site above 
# were used to parse data returned from a query to W|A

def _get_xml(ip):

    appid = 'UAGAWR-3X6Y8W777Q'
    base_url = 'http://api.wolframalpha.com/v2/query?'
    headers = {'User-Agent':None}
    
    url_params = {'input':ip, 'appid':appid}
    data = urllib.urlencode(url_params)
    req = urllib2.Request(base_url, data, headers)
    xml = urllib2.urlopen(req).read()
    return xml

        
def _xmlparser(xml):
    data_dics = {}
    tree = etree.fromstring(xml)
    #retrieving every tag with label 'plaintext'
    for e in tree.findall('pod'):
        for item in [ef for ef in list(e) if ef.tag=='subpod']:
            for it in [i for i in list(item) if i.tag=='plaintext']:
                if it.tag=='plaintext':
                    data_dics[e.get('title')] = it.text
    return data_dics
        

def calculate(in0, return_float = False):
    try:
        if return_float:
            return float(eval(in0))        
        return eval(in0)

    except:
        print 'Searching W|A...'
        
        xml = _get_xml(in0)
        result_dics = _xmlparser(xml)
        
        try:
            
        
            s = result_dics['Result']
        
            if not return_float:
                return s
        
            # Remove units by searching for first space
            if s.find(' ') > -1:
                s=s[:s.find(' ')]

            # Check for scientific notation
            if not s.find('10^') == -1:
                s = s[:s.find('10^')-1] + 'e' + \
                    s[s.find('^')+1:]

            return float(s)
        except:
            return 'Try rephrasing your question'



def test_0():
    assert abs(4. - calculate('2**2')) < .001

def test_1():
    assert ([0,0,0,1,2,3] == \
            calculate('[0,0,0]+[1,2,3]')) == True

def test_2():
    assert abs(17. - calculate('2+3*len("hello")')) < .001

def test_3():
    assert abs(-1. - calculate('cosine(pi)',return_float=True)) < .001

def test_4():
    assert abs(28. - len(calculate('average lifespan'))) < .001


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='CalCalc Parser')

    parser.add_argument('tagless', nargs='?')
    
    
    parser.add_argument('-s', action='store', dest='str0',
                        help='Specify the expression to evaluate')

    
    parser.add_argument('-fl', action='store_true', default=False,
                        dest='return_float',
                        help='Return the value as a float')
    comm = '''
            parser.add_argument('-p', action='store_true', default=False,
            dest='print_switch',
            help='Print the output to the screen')
           '''


    args = parser.parse_args()
    
    # Has user indicated -s?
    if args.str0:
        out = calculate(args.str0, args.return_float)
    else:
        #print 'tagless'
        out = calculate(args.tagless, args.return_float)
    
    print out

