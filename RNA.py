T = str('GATGGAACTTGACTACGTAAATT')
t_list = []

for x in T:
    if x == "T":
       t_list.append("U")
    elif x != "T":
         t_list.append(x)
t = ''.join(t_list)
print(t)