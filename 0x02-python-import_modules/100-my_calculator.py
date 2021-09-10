#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == '+':
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    sys.exit(0)
