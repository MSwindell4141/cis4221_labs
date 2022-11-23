import hashlib
## prompt the user to input hash type
## prompt the user to input a file having the password list
## prompt the user to input the hashed password to crack

## -----------
#password = qwerty (MD5):  d8578edf8458ce06fbc5bb76a58c5ca4
#password = qwerty (SHA1): b1b3773a05c0ed0176787a4f1574ff0075f7521e
hash_type = input("hash type: ") 
password_file = input("password file (please include .txt)): ")
hashed_password = input("hashed password to crack: ")
## --------------

## with the password file open, read each line
    ## if the hash type is md5:
        ## create a variable storing hashlib.md5(line.strip().encode()).hexdigest()
        ## if it matches the hashed password the user entered, print("password found" + 
#line.strip())
        ## exit
  
    ## repeat the same with hash type sha1
    ## replace hashlib.md5 with hashlib.sha1
    
    ## print('Password not in file') if none of the password matches
    
## -----------
file = open(password_file, 'r')
found_password = False
for line in file:
    hash
    if hash_type == "md5": 
        hash = hashlib.md5(line.strip().encode()).hexdigest()
    elif hash_type == "sha1": 
        hash = hashlib.sha1(line.strip().encode()).hexdigest()

    if hash == hashed_password:
        print("password found: " + line.strip())
        found_password = True
        break
    
file.close()
if not found_password:
    print('Password not in file')
exit
## --------------
