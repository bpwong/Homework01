#/usr/bin/env python
print 'hello github'
   

def calculator(str0 = '"Enter a string to calculate"'):
    print eval(str0)



if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        calculator((sys.argv[1]))
    else:
        calculator()