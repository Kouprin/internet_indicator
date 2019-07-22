#!/bin/bash
(! lsof -i :1743) &&
ANYBAR_PORT=1743 open -na AnyBar &&
/usr/local/bin/python3 /usr/local/bin/indicator.py
