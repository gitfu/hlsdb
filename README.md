hlsdb
=====

HLS mpeg-ts video segments stored in a btree db

I hated having ts segments everywhere, so I did what you're supposed to do with data, 
I stuck it in a database.

### Usage

* Use mkhlsbtree.py to insert segments into bdb. 
* pass dbname and path to mpeg-ts files on the command line 
```
python mkhlstree.py dbname /dir/of/ts-segments
```

* Use hlsbtree.cgi to serve the segments 
```
http://example.com/cgi-bin/hlsbtree.cgi?db=dbname&ts=segment30.ts
```

* mm3u8 creation not included ( Check out manifesto for a more complete HLS tool. 
