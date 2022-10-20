def rom_thous(x):
    xth = x // 1000
    if xth == 2:
        rth = ['MM']
    else:
        rth = ['M']
    return rth

def rom_hund(xth):
    xh: int = xth // 100
    if xh == 0:
        rh = ['']
    if xh == 9:
        rh = ['CM']
    if 6 <= xh <= 8:
        rh = ['D']
        i = 6
        while i <= xh:
            rh.append('C')
            i = i + 1
    if xh == 5:
        rh = ['D']
    if xh == 4:
        rh = ['CD']
    if 1 <= xh <= 3:
        rh = ['']
        i = 1
        while i <= xh:
            rh.append('C')
            i = i + 1
    return rh

def rom_ten(xth):
    xtt = xth % 100  # 84
    xt = xtt // 10  # 8
    if xt == 0:
        rt = ['']
    if xt == 9:
        rt = ['XC']
    if 6 <= xt <= 8:
        rt = ['L']
        i = 6
        while i <= xt:
            rt.append('X')
            i = i + 1
    if xt == 5:
        rt = ['L']
    if xt == 4:
        rt = ['XL']
    if 1 <= xt <= 3:
        rt: list = ['']
        i = 1
        while i <= xt:
            rt.append('X')
            i = i + 1
    return rt

def rom_owne(xtt):
    xo = xtt % 10
    if xo == 0:
        ro = ['']
    if xo == 9:
        ro = ['IX']
    if 6 <= xo <= 8:
        ro = ['V']
        i = 6
        while i <= xo:
            ro.append('I')
            i = i + 1
    if xo == 5:
        ro = ['V']
    if xo == 4:
        ro = ['IV']
    if 1 <= xo <= 3:
        ro: list = ['']
        i = 1
        while i <= xo:
            ro.append('I')
            i = i + 1
    return ro


x= int(input("x = "))

if x >= 1000:
    xth = x % 1000
    xtt = xth % 100
    r = rom_thous(x) + rom_hund(xth) +rom_ten(xth) + rom_owne(xtt)

if 100 <= x < 1000:
    xtt = x % 100
    r = rom_hund(x) + rom_ten(x) + rom_owne(xtt)

if x < 100:
    r = rom_ten(x) + rom_owne(x)

print(''.join(r))