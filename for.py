#for each in range(0,8,2):
#    print ("The value of string is "+ str(each))
    # This is the old-school way of concatenating strings


# Newer version is like:

for each in range(0,8,2):
    print ("The value of string is {0} and its double is {1}".format(each,each*2))


#    print ("The value of string is %d" %each)
        # %d means decimal integer, we're typecasting the field

#    print ("The value of string is %s" %str(each))
