# jughead

Experimenting with Twilio

## poc

First thing, send an SMS message

```
~/code/jughead $ python poc.py ~/path-to-config.cfg

44      twilio config is TwilioConfig(account='fake-account', token='fake-token', from_number='+fake-from', dest_number='+fake-to)
824     Starting new HTTPS connection (1): api.twilio.com
396     https://api.twilio.com:443 "POST /2010-04-01/Accounts/account-number/Messages.json HTTP/1.1" 201 837
```

## What's with the name?

Named after [Jughead Jones](https://en.wikipedia.org/wiki/Jughead_Jones) for no particular reason.

<img src="doc/jug.gif" alt="Jughead Jones"/>
