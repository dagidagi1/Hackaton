#author 1 Arkadi yakubov 2088064162
#author 2 Mikhail Diachkov 336426176
def suffix(num, time):
    def num_after_point(x):
        s = str(x)
        if not '.' in s:
            return 0
        return len(s) - s.index('.') - 1

    def eps():
        eps = 1
        while 1 + eps > 1:
            eps /= 2
        eps *= 2
        return eps
    #time format: ddhhmm
    suf = []
    suf[:0] = str(time)
    suf = [0,0,0,0,0] + suf
    listok = []
    listok = str(num).split(".")
    if len(listok[1]) == 1:
        if int(listok[1][0]) == 0:
            return int(listok[0]) + (float(time)/10000000000)
        else:
            return int(listok[0]) + (float(listok[1])/10) + (float(time)/1000000000000)
    x = []
    x[:0] = listok[1]
    num_suf = len(x)
    max_digits = num_after_point(eps()) - 1 - len(listok[0]) - 11
    x = x[0:max_digits - 1]
    last_digit = int(x[-1])
    if last_digit == 0 or last_digit < 5:
        x.pop(-1)
    else:
        x.pop(-1)
        x[-1] = int(x[-1]) + 1
    listok[1] = x + suf
    tmp = int(listok[0])
    exp = 10 ** -1
    print(listok)
    while len(listok[1]) != 0:
        tmp += int(listok[1][0]) * exp
        listok[1].pop(0)
        exp *= 0.1
    return tmp






print(suffix(3.123123, 131413))

