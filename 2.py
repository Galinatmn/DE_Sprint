x : int = 1233
#M                  MCMLXIV
if x > 1000:
    xth = x%1000 #984
    rth = ['M']
    xh : int = xth // 100 #9
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
        rh  = ['CD']
    if 1 <= xh <= 3:
        rh = ['']
        i = 1
        while i <= xh:
            rh.append('C')
            i = i + 1


    xtt = xth % 100 #84
    xt = xtt // 10 #8
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
        rt : list = ['']
        i = 1
        while i <= xt:
            rt.append('X')
            i = i + 1

    xo = xtt % 10 #4
    if xo == 9:
        ro = ['IX']
    if 6 <= xo <= 8:
        ro = ['L']
        i = 6
        while i <= xo:
            ro.append('X')
            i = i + 1
        ro = ''.join(ro)
    if xo == 5:
        ro = ['V']
    if xo == 4:
        ro = ['IV']

print(''.join(rth + rh + rt +ro))

