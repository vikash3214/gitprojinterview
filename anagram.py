def anagramcHECK(l):
    out=[]

    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(sorted(l[i])== sorted(l[j])):
                out.append([i,j])
    return out



if __name__=="__main__":
    list=["geeksquiz", "geeksforgeeks", "abcd",
                 "forgeeksgeeks", "zuiqkeegs"]
    output=anagramcHECK(list)
    print(output)


