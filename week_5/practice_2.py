def changeme(mylist):
    mylist.append([1,2,3,4])
    print("Values inside function:", mylist)
    return

mylist = [10,20,30]
changeme(mylist)
print("Values outside the function: ", mylist)
