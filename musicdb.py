#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:24:00 2018

@author: your name here
"""
import pymysql as db

class MusicDB:
    def __init__( self):
      self.conn = db.connect(host = "localhost", user = "nhossain", passwd = "nhossain", db = "nhossain_music", use_unicode=True, charset="utf8")
      
    def __del__(self):
      self.conn.close()
    
    def listGenres(self):       
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor()
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT GenreID, Name FROM Genre")

        # Demonstrates returning a cursor
        return(cur)
        
 
    def listArtists(self):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT ArtistID, Name FROM Artist")
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)
    
    def listAlbums(self):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT AlbumId, Title FROM Album")
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)
 
        
    def searchArtist(self, name):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (name,)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT ArtistID, Name FROM Artist WHERE Name like %s", params)
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Return the results, in this case a list of tuples
        return(result)

    def checkArtist(self, cur, name):              
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (name,)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT ArtistId, Name FROM Artist WHERE Name like %s" ,params)

        #Fetch all the results
        result = cur.fetchall()

        #Return the results, in this case a list of tuples
        return(result)

    def listArtists(self, cur):
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM Artist")

        #Fetch all the results
        result = cur.fetchall()

        return result

    def insertArtist(self, name):       
        cur = self.conn.cursor()
        result = self.checkArtist(cur, name)

        #no of artists with the name
        l = len(result)

        #no of artists
        s = len(self.listArtists(cur))  

        if(l >> 0):
            return 0
        # Create a cursor object to execute queries and retrieve results
        else:
            #tuple to store parameters
            params = (s+1, name)

            # Run a query: provide any SQL in a string
            cur.execute("INSERT INTO Artist (ArtistId, Name) VALUES %s" % (params,))

            #commit
            self.conn.commit()

            return 1

    def updateArtist(self, name_old, name_new):       
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor()
        
        #check if name exists
        l = len(self.checkArtist(cur, name_old))

        #if artist name does not exist
        if(l == 0):
            return 0
        #if artist name exists
        else:
            #tuple to store parameters
            params = (name_old, name_new)

            # Run a query: provide any SQL in a string
            cur.execute("UPDATE Artist SET Name = '%s' WHERE Name like '%s'" % params)

            #commit
            self.conn.commit()

            return 1
        
      
        
