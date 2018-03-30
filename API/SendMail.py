# MailGun API
import requests
import json
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox3327a66d31c2444b810d61f8b6f81665.mailgun.org/messages",
        auth=("api", "key-b9b4b39d759a3594855326e1ba6e2d12"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox3327a66d31c2444b810d61f8b6f81665.mailgun.org>",
              "to": "yajana <yajana.merahkee@gmail.com>",
              "subject": "Hello yajana",
              "text": "Congratulations yajana, you just sent an email with Mailgun!  You are truly awesome!",
              "attachment": "C:/Users/Yajana/PycharmProjects/Distributed-setup-4/API/DropboxAPI.py"})

# You can see a record of this email in your logs: https://app.mailgun.com/app/logs .

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10,000 emails/month for free.



#send_simple_message()

#!/usr/bin/python

import requests
content = "Sword of Omens, give me sight BEYOND sight"
headers = {
    'Authorization': 'e4d2e76d00660dd377fb5c532821368eb53cfac7',
    'Content-Type': 'application/json',
}

data = {"options": {"sandbox": True   },   "content": {
       "from": "sandbox@sparkpostbox.com",   "subject": "Thundercats are GO!!!",
        "text": content, "html":"<h1>hi</h1>"   },   "recipients": [{ "address": "yajana.merahkee@gmail.com" }]}

jsonData = json.dumps(data)

response = requests.post('https://api.sparkpost.com/api/v1/transmissions', headers=headers, data=jsonData)
print(response.json())