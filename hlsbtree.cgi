#!/usr/bin/env python

import bsddb 
import cgi
import cgitb
import string,sys,os

cgitb.enable()
dbdir='/var/www/hlsdb/'



# http://example.com/cgi-bin/hlsbtree.cgi?db=videoname&ts=segment30.ts

def fetchfields():
	cfs=cgi.FieldStorage()
	hlsdb=cfs.getvalue('db')
	tsfile=cfs.getvalue('ts')
	return hlsdb,tsfile


def openbtree(dbname):
        btree=bsddb.btopen('%s%s'%(dbdir,dbname),'r')
        return btree

def printheaders():
        print 'Content-Type: video/mpeg'
	print


def printvblob():
	hlsdb,tsfile=fetchfields()
	btree=openbtree(hlsdb)
        print btree[tsfile]
	btree.close()

def showts():
	printheaders()
        printvblob()


showts()

	

