def my_fun(data):
    have_false = False
    err_list = []
    for row in data:
        if row[1] == 'true':
            continue
        if row[1] == 'false':
            have_false = True
            if row[2] not in err_list:
                err_list.append(row[2])

    if not have_false:
        return ['Yes', err_list]
    else:
        return ['No', err_list] 


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(input().split(' '))
    ret, err_list = my_fun(data)
    print(ret)
    if err_list != []:
        for i in range(len(err_list)):
            if i != len(err_list)-1:
                print(err_list[i], end=' ')
            else:
                print(err_list[i], end='')


if __name__=='__main__':
    main()
