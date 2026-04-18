def get():
    a,b = input().split()
    len_a = len(a)
    len_b = len(b)
    for w in range(1,len_a):
        for c in range(0,w):
            t = ''
            for i in range(len_a):
                if i%w == c:
                    t += a[i]
            if t == b:
                return True
    return False
        
    
if get():
    print('Yes')
else:
    print('No')