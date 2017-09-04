area = {
    'S': 26,
    'T': 27,
}

while 1:
    id = input('Please input id number? ')
    sum = 0

    areaCode = area[id[0]]

    sum += areaCode // 10 + areaCode % 10 * 9

    for i in range(len(id)):
        if i == 0:
            continue
        elif i == len(id) -1:
            sum += int(id[i])
        else:
            sum += int(id[i]) * (len(id) - i - 1)

    if sum % 10 == 0:
        print('real')
    else:
        print('fake')
