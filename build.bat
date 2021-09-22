python gen_tids.py dump.json
del /Q result\*.*
xcopy /s /e /y tiddlywiki result\
move *.tid result\tiddlers
tiddlywiki result --build index
