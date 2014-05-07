#!/usr/bin/env python

import os,sys

import bsddb

#location of the db file 
dbdir='/var/www/hlsdb/'


#create db file 
def mkbtree(dbname):
	btree=bsddb.btopen('%s%s'%(dbdir,dbname),'c')
	return btree


def stuffbtree(tstup):
	tsfile=tstup[0]
    	dbname=tstup[1]
        tspath=tstup[2]+'/'
	btree=mkbtree(dbname)
        if tsfile[-3:]=='.ts':
		k=tsfile
                vbfile=open(tspath+tsfile,'rb')
                btree[k]=vbfile.read()



def showts(dbname):
	btree=mkbtree(dbname)
	for k,v in btree.iteritems():
		print k


# pass dbname and path to mpeg-ts files on the command line 
# I think I should pass an m3u8 file here.


if sys.argv[1] and sys.argv[2]:
	dbname=sys.argv[1]
	print dbname
	tspath=sys.argv[2]	
	tsfiles=os.listdir(tspath)
	for t in tsfiles:
		tstup=(t,dbname,tspath)
		stuffbtree(tstup)
		print 'blob %s added,'%t
	
