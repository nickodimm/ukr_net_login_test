## Execute from shell:

```
pip3.6 install -r requirements.txt && python3.6 -m pytest --elogin=<user_login> --epass=<user_pass>
```
<br>


__Build need a user credentials, so without them an exception will be raised.__

## To run test with browser window:
__Add additional argument to pytest run command:__
```
--headless=<any_value_differ_from_true>
```

__An additional (optional argument) is:__

```--url=<http://example.com>```

__It is not necessary, so can be skipped.__
