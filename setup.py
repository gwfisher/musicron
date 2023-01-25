from distutils.core import setup

author="Wesley Fisher"
author_email="wfisher@praetor.tel"

packages = ["musicron"]

url="https://github.com/gwfisher/musicron"

description="It's Cron...for music!"
long_description="README"

install_requires=[
    "functools",
    "pathlib",
    "importlib",
    "yaml",
    "dbus",
    "psutil"
]
