#author 1 Arkadi yakubov 2088064162
#author 2 Mikhail Diachkov 336426176
def suffix(num):
    suf = 0.00000131250


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

print(num_after_point(eps()))