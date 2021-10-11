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


num = input("Enter ")
counter = 0
while(num != 6174):
    counter += 1
    print(str(num) + " > ", end="")
    mini = order(num)[0:order(num).find(".")]
    maxi = order(num)[order(num).find(".")+1:]
    num = int(maxi) - int(mini)
print(str(6174))
print("you got to 6174 in {} rounds".format(counter))
