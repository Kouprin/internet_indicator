#!/bin/bash
set -e
brew cask install anybar
/usr/local/bin/pip3 install -r requirements.txt
cp indicator.py /usr/local/bin/
cp run_indicator.sh /usr/local/bin/
cp com.kouprin.osx.indicator.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.kouprin.osx.indicator.plist
