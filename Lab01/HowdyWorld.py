def order(num):
    num = str("{:0>4}").format(num)
    mini = int(num)
    maxi = int(num)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    values = str(i) + str(j) + str(k) + str(l)
                    if( len(set(values)) == len(values)):
                    #if i != j and j != k and k != l and i != k and l != j and i != l:
                        string = str(num[i]) + str(num[j]) + str(num[k]) + str(num[l])
                        mini = min(mini, int(string))
                        maxi = max(maxi, int(string))
    return str("{:0>4}").format(mini) + "." + str(maxi)

list = {"one":1, "two":2}
for i in list:
    print(i)
