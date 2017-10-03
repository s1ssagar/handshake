def handshake():
    tc = input()
    while tc > 0:
        num = input()
        if num >= 2:
            print int(((num-1)/2.0)*(1+(num-1)))#sum of n terms
        else:
            print 0
        tc -= 1

def main():
    handshake()

if __name__ == "__main__":
    main()