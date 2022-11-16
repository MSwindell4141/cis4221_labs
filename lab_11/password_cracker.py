import hashlib
## prompt the user to input hash type
## prompt the user to input a file having the password list
## prompt the user to input the hashed password to crack

## -----------
## Your code goes here
## --------------

## with the password file open, read each line
    ## if the hash type is md5:
        ## create a variable storing hashlib.md5(line.strip().encode()).hexdigest()
        ## if it matches the hashed password the user entered, print("password found" + 
line.strip())
        ## exit
  
    ## repeat the same with hash type sha1
    ## replace hashlib.md5 with hashlib.sha1
    
    ## print('Password not in file') if none of the password matches
    
## -----------
## Your code goes here
## --------------
