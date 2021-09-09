#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print(0)
        sys.exit(0)
    n = 0
    for i in range(1, args):
        n += int(sys.argv[i])
    print(n)
