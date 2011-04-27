#!/usr/bin/env python
# encoding: utf-8
"""
get_calendar.py

Created by David Kreitschmann on 2011-04-08.
Copyright (c) 2011 David Kreitschmann. All rights reserved.
"""
import re
import campusnet
import urllib2

import ConfigParser

from icalendar import Calendar, Event

def get_calender_for_month(cn_session, year, month):
    """docstring for get_calender"""
    export_page = cn_session.request("SCHEDULER_EXPORT_START",("000272", "Y%dM%d"%(year,month)))
    m=re.search(r"<a href=\"([0-9a-z/?]+)\">Kalenderdatei</a>",export_page)
    file_url = url+m.group(1)
    r = urllib2.urlopen(file_url)
    cal = Calendar.from_string(r.read())
    
    
def get_calender_for_range(cn_session, ):
    

def main():
    config = ConfigParser.SafeConfigParser(campusnet.DEFAULT_CONFIG)
    config.read(campusnet.CONFIG_FILE)
    user = config.get("Credentials","user")
    password = config.get("Credentials", "password")
    url = config.get("URL","server_url")
    path = config.get("URL","campusnet_path")
    cn = campusnet.CampusNetSession(url+path, user, password )
    
    
    
    
    export_page = cn.request("SCHEDULER_EXPORT_START",("000272", "Y2011M04"))
    m=re.search(r"<a href=\"([0-9a-z/?]+)\">Kalenderdatei</a>",export_page)
    file_url = url+m.group(1)
    r = urllib2.urlopen(file_url)
    print r.read()
if __name__ == '__main__':
    main()

