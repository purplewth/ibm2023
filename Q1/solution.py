def fulfill(avail_sizes, req_sizes):
    for size in req_sizes:
        while size not in avail_sizes:
            if size == 'S':
                size = 'M'
            elif size == 'M':
                size = 'L'
            elif 'S' in size:
                size = size[1:]
            elif 'L' in size:
                size = 'X' + size
            if 'L' in size and len(size)==1001:
                return 'No'

        if size in avail_sizes:
            avail_sizes.remove(size)
            continue
    return 'Yes'
                       

def main():
    N = int(input())
    avail_sizes = input().split(' ')
    M = int(input())
    req_sizes = input().split(' ')

    res = fulfill(avail_sizes, req_sizes)
    print(res)


if __name__ == '__main__':
    main()

