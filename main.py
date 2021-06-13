#author 1 Arkadi yakubov 2088064162
#author 2 Mikhail Diachkov 336426176
from datetime import datetime
now = datetime.now()
time = now.minute + now.hour * 100 + now.day * 10000
def suffix(num):
    global time
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
    num = float(num)
    if num == 0:
        return (float(time)/1000000000)
    singed = False
    if num < 0:
        singed = True
        num *= -1
    suf = []
    suf[:0] = str(time)
    suf = [0, 0, 0, 0, 0] + suf
    listok = []
    listok = str(num).split(".")
    if len(listok[1]) == 1:
        if int(listok[1][0]) == 0:
            ans = int(listok[0]) + (float(time)/10000000000)
        else:
            ans = int(listok[0]) + (float(listok[1])/10) + (float(time)/1000000000000)
        if singed:
            return ans * -1
        else:
            return ans
    x = []
    x[:0] = listok[1]
    num_pref = len(listok[0])
    max_digits = num_after_point(eps()) - 1 - len(listok[0]) - 11
    x = x[0:max_digits - 1]
    last_digit = int(x[-1])
    if last_digit == 0 or last_digit < 5:
        x.pop(-1)
    else:
        x.pop(-1)
        x[-1] = int(x[-1]) + 1
    listok[1] = x + suf
    tmp = str(listok[0]) + '.'
    while len(listok[1]) != 0:
        tmp += str(listok[1][0])
        listok[1].pop(0)
    return tmp

