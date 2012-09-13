#/usr/bin/env python

#print 'hello github'
import argparse, sys
'''
    DO SHiT
'''


def calculator(args):
    if args.print_switch:
    #print eval(args.str0)
        print 'asdfads'
        if args.str0:
            print args.str0
        else:
            print 'baha'
#return eval(args.str0)

if len(sys.argv)==2:
    print sys.argv[:]

parser = argparse.ArgumentParser(description='CalCalc Parser')
   
parser.add_argument('-p', action='store_true', default=True,
                    dest='print_switch',
                    help='Print the output to the screen')

parser.add_argument('-s', action='store', dest='str0',
                    help='Specify the expression to evaluate')

    #parser.add_argument('-s', action='store', dest='str0',
    #                help='Specify the expression to evaluate',
#                default='(Enter a String)')


inputs = parser.parse_args()

calculator(inputs)





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
    import sys
    print 'main'
        #if len(sys.argv)>1:
    #calculator((sys.argv[1]))
        #else:
#calculator(inputs)
