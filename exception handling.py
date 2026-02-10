#Exceptions ae errors encountered in a code

try:            # the main purpose of this "try" block is to check whether the code will run into issues or not when run.
    print(x)
except:# the "except" block runs only if an error, or exception, occurs in the preceding
        print("Something Went Wrong")
finally:
    print("Successfull") # The "finally" block is executed regardless of errors in the code