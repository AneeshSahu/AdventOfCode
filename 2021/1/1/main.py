def main():
    f = open('input','r')
    prev = int(f.readline())
    cnt=0
    for line in f: 
        cur = int(line)
        if prev< cur: 
            cnt+=1
        prev = cur
    print( cnt)
    return cnt

if __name__ == "__main__":
    main()
