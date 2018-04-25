#!/usr/bin/python
# -*- coding: utf-8 -*-
# Database User Interface - Web version
#
# Note that these functions contain output
# such as print(), but do NOT contain any 
# actual database code. The database is handled by 
# a separate class.
#
# Also note that unlike the command-line version, you
# CANNOT USER input() because that waits for keyboard input.
# All input must come from CGI forms.
#

from musicdb import MusicDB

# Create a database object that will handle all the DB stuff.
dbobj = MusicDB()

def listGenres():
    cur = dbobj.listGenres()
    
    # Fetch some the results
    result = cur.fetchall()
    
    
    print("""
    <table border=1>
    <tr><th>GenreID</th><td>Genre Name</td></th>
    """)
    for row in result:
        id, name = row
        #print("%d %s" % (id, name))
        print("<tr><td>%d</td><td>%s</td></tr>" % (id, name))
        print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """) 

def listArtists():
    results = dbobj.listArtists()
    
    print("<h1>All artists</h1><p>")
    
    print("""
    <table border=1>
    <tr><th>ArtistID</th><td>Artist Name</td></th>
    """)
    for row in results:
        id, name = row       
        #print("%d %s" % (id, str(name)))
        print("<tr><td>%d</td><td>%s</td></tr>" % (id, name))
        print()
        
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """)     
        
def listAlbums():
    results = dbobj.listAlbums()
    
    print("<h1>All albums</h1><p>")
    
    print("""
    <table border=1>
    <tr><th>AlbumID</th><td>Album Name</td></th>
    """)
    for row in results:
        id, name = row       
        #print("%d %s" % (id, str(name)))
        print("<tr><td>%d</td><td>%s</td></tr>" % (id, name))
        print()
        
        
    print("""
    
    </table>
    
    <br>
    <a href="?">Return Home</a>
    
    """)

def insertArtist(name):
    result = dbobj.searchArtist(name)

    if len(result) >> 0:
            print("<h2>%s already exists in the database</h2>" % name)
    
    else: 
        # Print the results, in this case a list of tuples
        dbobj.insertArtist(name)
        
    print("""

    <h2>%s has been added to the database</h2>
    <br>
    <a href="?">Return Home</a>
    
    """, name)         

def searchArtist(name):    
    # Notice that there is no input() here
    # We must get input from CGI forms and pass in paramters
    result = dbobj.searchArtist(name)
       
    if len(result) == 0:
        print("<h2>%s not found in the database</h2>" % name)
    
    else: 
        # Print the results, in this case a list of tuples
        # This is ugly and unformatted...
        for row in result:
            print(row)
        
    print("""

    
    <br>
    <a href="?">Return Home</a>
    
    """) 
        
def showDefaultPage():    
    print("""
    <h1>Welcome to cTunes</h1>
    <br>
    You can:<br><ul>
    
    <!-- Adding attributes to the end of a URL puts them into the CGI form -->
    <li><a href="?listGenres=1">List all Genres</a>
    <li><a href="?listArtists=1">List all Artists</a>
    <li><a href="?searchArtist=1">Search for an Artist</a>
    <li><a href="?listAlbums=1">List all Albums</a>
    </ul>
    
    <p>    
    """)       
    
    
    
################################################################################
def showSearchArtistForm():

    print("""
    <h2>Add A Profile</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="searchArtist" value="1">
    <table>
        <tr>
            <td>Artist Name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>
    """)

##################################################################################
def showInsertArtistForm():

    print("""
    <h2>Add a Profile</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="insertArtist" value="1">
    <table>
        <tr>
            <td>Artist Name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE=""></td>
        </tr>
        <tr><td>
            
            <input type="submit" name="addProfile" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>
    """)
    