x= 12
y= -2.75
z= "Andrew"

print("%d" % x)      #The value stored in x is formatted as a decimal (base 10) integer
print("%f" % y)      #The value stored in y is formatted as a floating-point number.
print("%d and %f" % (x, y))           #The value stored inxis formatted as a decimal (base 10) integer and the value
                                           #stored in y is formatted as a floating-point number. The other characters in
                                         # the string are retained without modification.

print("%.4f" % x)        #The value stored in x is formatted as a floating-point number with 4 digits
                          #to the right of the decimal point

print("%.1f" % y)          #The value stored in y is formatted as a floating-point number with 1 digit to
                            #the right of the decimal point. The value was rounded when it was formatted
                                #because the number of digits to the right of the decimal point was reduced.

print("%10s" % z)        #The value stored in z is formatted as a string so that it occupies at least 10
                          #spaces. Because z is only 6 characters long, 4 leading spaces are included
                            #in the result.

print("%4s" % z)         #he value stored in z is formatted as a string so that it occupies at least 4
                          #spaces. Because z is longer than the indicated minimum length, the resulting
                            #string is equal to z.

print("%8i%8i" % (x, y))   #Both x and y are formatted as decimal (base 10) integers occupying a
                            #minimum of 8 spaces. Leading spaces are added as necessary. The digits to
                             #the right of decimal point are truncated (not rounded) when y (a floating point number) is formatted as an integer.
