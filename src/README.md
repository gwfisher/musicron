# Welcome to Musicron #
Do you have a lot of radio shows you enjoy, but forget to tune in? Maybe you like anonradio! Or tilderadio! But miss shows?

## Miss shows no more with Musicron! ##

Here are some of the features of Musicron!

* Easy YAML based configuration
* Trigger shows hourly or daily
* Plugin based architecture! Create your own plugins with an easy to use API
* Supports a variety of services

** How to Use **

Simply populate the shows you want in your config.yml file like so:

```
---
- name: "HBR-1"
  time: "13:20"
  service:
    provider: "VLC"
    url: "http://www.hbr1.com/playlist/trance.aac.m3u"
    plugin: "vlc"
```

```time``` can be in the format of:
* *H:M* for play every day
* *H:M Day* for play on a specified day
* *TEST* for plugin testing

-or-

You can add the prefix *U* to any time for UTC