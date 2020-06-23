import  time

start = time.time()

# l0 = ['code', 'doce', 'ecod', 'framer', 'frame', 'farmer']
l0 = ['poke', 'pkoe', 'okpe', 'ekop', 'lope']

ans = []
i = 0
while i < len(l0):
    l = l0[i]

    found_new = True

    set_tmp = {}
    for ll in l:
        if ll in set_tmp:
            set_tmp[ll] += 1
        else:
            set_tmp[ll] = 1
    
    # find match
    for a in ans:
        if a == set_tmp:
            l0.pop(i)
            i -= 1
            found_new = False
            break

    if found_new:
        set_tmp = {}
        for ll in l:
            if ll in set_tmp:
                set_tmp[ll] += 1
            else:
                set_tmp[ll] = 1
        ans += [set_tmp]
        
    i += 1

end = time.time()
print(end-start)

print(ans)
print(l0)