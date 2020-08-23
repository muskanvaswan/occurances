from collections import OrderedDict

s = input("Enter the string:  ")
k = OrderedDict(); o_d = OrderedDict()
for i in s:
    if i in k.keys():
        k[i] += 1
    else:
        k[i] = 1

for i in k:
    if k[i] in o_d.keys():
        o_d[k[i]] += i
    else:
        o_d[k[i]] = [i]
o = o_d.keys()
o.sort(reverse=True)

p=0
for i in o:

    o_d[i].sort()
    for j in o_d[i]:
        if p<3:
            print(j + " "+ str(i))
        p+=1
