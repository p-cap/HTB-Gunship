# HTB-Gunship
Redid the Gunship application that focuses on the vulnerability at hand

# Minimized version Gunship from HTB

## Pre-requisites
- docker 
  https://docs.docker.com/engine/install/

- requests (HTTP Library for Python)
  https://docs.python-requests.org/en/master/user/install/

## POC
1. ```build-docker.sh``` for Mac / Linux | ```win-build-docker.ps1``` for Windows
2. ```localhost:1555```
3. Run ```python payload.py```
4. In the response, you should see a file listing inside "/app" directory
5. In ```payload.py```, line key inside the __proto__.block json object, you can change the commands based on your need
