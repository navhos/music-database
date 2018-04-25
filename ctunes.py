#!/usr/bin/python
# -*- coding: utf-8 -*-
# "she-bang" line is a directive to the web server: where to find python
#
# filename: ctunes.py
# cTunes = Clark Tunes = mini iTunes?

import time
import cgi
import cgitb; cgitb.enable()
import musicinterface

################################################################################
def doHTMLHead():

    print("""
    <html>
    <head>
    <title>cTunes</title>
    </head>
    <body>
    """)


################################################################################
def doHTMLTail():

    print("""
    <p>
    <hr>
    This page was generated at %s.
    </body>
    </html>

    """ % time.ctime())


################################################################################
if __name__ == "__main__":

    print("Content-Type: text/html; charset=utf-8")
    print("Cache-Control: no-cache, must-revalidate") # HTTP/1.1 
    print("Expires: Sat, 26 Jul 1997 05:00:00 GMT") # Date in the past 
    print()

    form = cgi.FieldStorage()
    
    doHTMLHead()

    #print("<br><br>")
    #print("Debugging mode with 'print form':<br>")
    #print(form)
    #print("<br><br>")

   
    if "listGenres" in form:       
        musicinterface.listGenres()
   
    elif "listArtists" in form:
        musicinterface.listArtists() 
    
    elif "listAlbums" in form:
        musicinterface.listAlbums()    
    
    elif "insertArtist" in form and "name" in form:
        name = form["name"].value 
        musicinterface.insertArtist(name)    

    elif "insertArtist" in form:
        musicinterface.showInsertArtistForm()

    elif "updateArtist" in form and "name_old" in form and "name_new" in form:
        name_old = form["name_old"].value
        name_new = form["name_new"].value
        musicinterface.updateArtist(name_old, name_new)    

    elif "updateArtist" in form:
        musicinterface.showUpdateArtistForm()

    # search for a name, and we have the name
    elif "searchArtist" in form and "name" in form:
        name = form["name"].value 
        musicinterface.searchArtist(name)
       
    # search for a name, and we DO NOT have the name
    elif "searchArtist" in form:
        musicinterface.showSearchArtistForm()
    
    # default case: show menu
    else:        
        # substitute other functions in here to test from command line
        # musicinterface.listArtists()
        
        # show the default page
        musicinterface.showDefaultPage()

    doHTMLTail()    





