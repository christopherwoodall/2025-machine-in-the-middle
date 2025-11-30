Execute the following command:

```
nohup python3 -m http.server 8080 2>&1 | tee /tmp/http_requests.log 2>&1 &
```
