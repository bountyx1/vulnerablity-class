


# php -S 127.0.0.1:8080

### Jquery 3.4.0 bellow $.extended is vulnerable to protottype Polution

(https://snyk.io/blog/after-three-years-of-silence-a-new-jquery-prototype-pollution-vulnerability-emerges-once-again/)['link']

### Poc
```

http://localhost:8080/?json={"__proto__":{"url":"https://google.com"}}

```
