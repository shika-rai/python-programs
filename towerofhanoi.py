def tower(disk,source,auxi,dest):
    if(disk==1):
        print("move {} from {} to {}".format(disk,source,dest))
        return
    else:
        tower(disk-1,source,dest,auxi)
        print("move {} from {} to {}".format(disk,source,dest))
        tower(disk-1,auxi,source,dest)



disk=int(input("Enter any number: "))
print("Steps involved are")
tower(disk,'A','B','C')