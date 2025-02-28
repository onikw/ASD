def sort():
    tab=[9,5,4,3,13,2]
    for i in range(1,len(tab)):
        j=i-1
        pam=tab[i]
        while(pam<tab[j] and j>=0):
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=pam
        print(tab)
sort()