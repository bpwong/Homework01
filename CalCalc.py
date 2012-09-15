#/usr/bin/env python

#print 'hello github'
import argparse, sys
'''
    DO SHiT
'''


def calculator(in0, return_float = False):
    try:
        if return_float:
            return float(eval(in0))
        
        return eval(in0)
    except:
        return 'invalid inputttt'



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
        print 'tagless'
        out = calculator(args.tagless, args.return_float)
    
    print out

