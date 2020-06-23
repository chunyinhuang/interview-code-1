import  time



# parameters

s0 = 2
n = 100000
k = 3
b = 3
m = 2
a = 10000
haha = True

# check constraints
# tmp_limit = 10**9
# if n < 1 or n > 6*10**7:
#     return
# elif k < 1 or k > tmp_limit:
#     return
# elif b < 1 or b > tmp_limit:
#     return
# elif m < 1 or m > tmp_limit:
#     return
# elif a < 1 or a > 10**18:
#     return
if haha:
    start = time.time()
    # get s
    s_left = [s0]
    s_right = []
    tmp = s0
    half_a = a**(1/2)
    count = 1
    
    while count < n:
        tmp = ((k*tmp+b)%m) + 1 + tmp
        if tmp > a:
            break
        # if tmp > tmp_limit:
        #     return
        if tmp <= half_a:
            s_left += [tmp]
        else:
            s_right += [tmp]
        count += 1
    
    ans = 0
    
    # those smaller than squared a
    ans += len(s_left)**2

    
    # initialize idx
    idx = len(s_left)-1
    for s_ in s_right:
        if s_ > a:
            break

        q = a/s_
        if q < s_left[0]:
            break
        
        while idx >= 0:
            if s_left[idx] <= q:
                ans += idx+1
                break
            idx -= 1

    # if len(s_left) > len(s_right):
    #     # initialize idx
    #     idx = len(s_left)-1
    #     for s_ in s_right:
    #         if s_ > a:
    #             break

    #         q = a/s_
    #         if q < s_left[0]:
    #             break
            
    #         while idx >= 0:
    #             if s_left[idx] <= q:
    #                 ans += idx+1
    #                 break
    #             idx -= 1
    # else:
    #     # initialize idx
    #     idx = 0
    #     for ii in range(len(s_left)-1, -1, -1):
    #         s_ = s_left[ii]

            
    #         q = a/s_
    #         if q > s_right[-1]:
    #             break
            
    #         while idx < len(s_right):
    #             if s_right[idx] >= q:
    #                 ans += idx+1
    #                 break
    #             idx += 1 

    end = time.time()
# return ans

else:
    start = time.time()
    # get s
    s = []
    s += [s0]
    tmp = s0
    
    while len(s)<n:
        tmp = ((k*tmp+b)%m) + 1 + tmp
        if tmp > a:
            break
        # if tmp > tmp_limit:
        #     return
        s += [tmp]
    
    
    # put squared a in s
    if a**(1/2) in s:
        ans = 1
    else:
        ans = 0

    s += [a**(1/2)]
    s.sort()

    # those smaller than squared a
    a_index = s.index(a**(1/2))
    ans += a_index*a_index 

    # break into half
    s_left = s[:a_index]
    s_right = s[a_index+1:]

    

    # initialize idx
    idx = a_index-1
    
    for s_ in s_right:
        if s_ > a:
            break

        q = a/s_
        if q < s_left[0]:
            break
        
        # idx = a_index-1
        while idx >= 0:
            if s_left[idx] <= q:
                ans += (idx+1)*2
                break
            idx -= 1
    end = time.time()


print(end-start)

print(ans)