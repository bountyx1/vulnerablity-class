## XSS notes
### DOM-XSS


### Markdown
-  Markdown basically superset of html means it supports html too but developer often under assumption that it only allows markdown like 
- # ### ```code``` it also can contain html characters 
- So developer isn't filtering input neither that third part library function markdown .
- 
 ```
var userinput = markdow("# aaa")

return userinput
// Html Tag
var userinput = markdow("<a href=javascript:alert(1)>aaa")

return userinput 

// Markdown to create link
var userinput = markdow("[Click Me](https://www.example.com/)
")

return userinput
 ```

- Case 2 3rd party library comes with builtin in sanitizers to prevent xss like dompurify
- dompurify 
- basically filters out the harmfull tags/attributes 
- So third party markdown uses dompurify or builtin own devloper library to filter out malicous tag/attributes


```
DOMPurify.sanitize('<img src=x onerror=alert(1)//>'); // becomes <img src="x">

```
```
var userinput = markdown("<a href=javascript:alert`1`>");
return userinput

```
- what could possible go wrong?
- 3rd party library developer build own html santizer
