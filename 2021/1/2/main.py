def main():
    f=open('input','r')
    cnt = 0 
    first = int(f.readline())
    second = int(f.readline())
    third = int(f.readline())
    prev = first+second+third
    for line in f: 
        first = second
        second = third
        third = int(line)
        cur = first+second+third
        if cur > prev:
            cnt+=1
        prev = cur
    print(cnt) 
    return cnt 

if __name__ == "__main__":
    main()
