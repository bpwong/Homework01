#/usr/bin/env python

#print 'hello github'
import argparse, sys, urllib, urllib2
from xml.etree import ElementTree as etree
'''
    DO SHiT
'''

# Credit to http://advencode.wordpress.com/2011/10/17/simple-query-request-with-wolfram-api/

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
        

def calculator(in0, return_float = False):
    try:
        if return_float:
            return float(eval(in0))        
        return eval(in0)

    except:
        print 'Searching W|A...'
        
        xml = _get_xml(in0)
        result_dics = _xmlparser(xml)
        s = result_dics['Result']
        
        if not return_float:
            return s
        
        # Remove units by searching for first space
        s=s[:s.find(' ')]

        # Check for scientific notation
        if not s.find('10^') == -1:
            s = s[:s.find('10^')-1] + 'e' + \
                s[s.find('^')+1:]

        return float(s)



def test_0():
    assert abs(4. - calculator('2**2')) < .001

def test_1():
    assert ([0,0,0,1,2,3] == \
            calculator('[0,0,0]+[1,2,3]')) == True

def test_2():
    assert abs(4. - calculator('2**2')) < .001

def test_3():
    assert abs(4. - calculator('2**2')) < .001

def test_4():
    assert abs(4. - calculator('2**2')) < .001


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
        out = calculator(args.str0, args.return_float)
    else:
        #print 'tagless'
        out = calculator(args.tagless, args.return_float)
    
    print out

