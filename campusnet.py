#!/usr/bin/env python
# encoding: utf-8
"""
campusnet.py

Simplifies Connections to a CampusNet Campus Management System

At TU Darmstadt its called TUCaN.

"""

import sys
import os
import re
import urllib2
import urllib
import sys 
reload(sys) 
sys.setdefaultencoding("iso-8859-1")


APPNAME="CampusNet"
CONFIG_FILE="settings.cfg"
DEFAULT_CONFIG={"user":"","password":""}


class CampusNetSession(object):
    """Manages a Campusnet Session"""
    def __init__(self, base_url, user, password):
        super(CampusNetSession, self).__init__()
        self.base_url = base_url
        self.user = user
        self.password = password
        self.clino="000000000000001"
        self.login()
        
    def login(self):
        """docstring for login"""
        content = self.post_request("LOGINCHECK",(self.user,self.password,"000294","",""))
        clino_match = re.search(r"<input name=\"clino\".*value=\"(\d+)\"",content)
        clino=clino_match.group(1)
        if clino==self.clino:
            raise Exception("Invalid credentials")
        self.clino=clino
            
    def post_request(self, prgname, arguments):
        """docstring for post_request"""
        argcount = 0
        data = []
        for a in arguments:
            data.append(("arg%d"%argcount, arguments[argcount]))
            argcount+=1
        data[0:0] = [("clino",self.clino)]
        argumentlist = ",".join([a[0] for a in data])
        data[0:0] = (("ARGUMENTS",argumentlist),("PRGNAME",prgname),("APPNAME",APPNAME))
        print data
        print urllib.urlencode(data)
        f = urllib2.urlopen(self.base_url,urllib.urlencode(data))
        return f.read()
    request = post_request
    

def main():
    import ConfigParser
    config = ConfigParser.SafeConfigParser(DEFAULT_CONFIG)
    config.read(CONFIG_FILE)
    user = config.get("Credentials","user")
    password = config.get("Credentials", "password")
    url = config.get("URL","campusnet_base")
    cn = CampusNetSession(url, user, password )
    

if __name__ == '__main__':
	main()

