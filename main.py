import http.client
import base64
import re

credentials = '[ENTER YOUR CREDENTIALS HERE]'

encoded = base64.urlsafe_b64encode(credentials.encode("utf-8"))
encodedString = str(encoded, "utf-8")

teamNumber = input("Enter a valid FTC team number: ")

conn = http.client.HTTPSConnection("ftc-api.firstinspires.org")
headers = {
    'Authorization': 'Basic ' + encodedString,
}
conn.request("GET", "/v2.0/2021/teams?teamNumber=" + teamNumber + "&page=1", headers=headers)
res = conn.getresponse()
data = res.read()
teamInfo = data.decode("utf-8")

print('')

parts = teamInfo.split(',')
teamName = re.sub('"', '', parts[2]).split('nameShort:')
print("Team", teamNumber, "-", teamName[1])

teamCity = re.sub('"', '', parts[4]).split('city:')
teamProv = re.sub('"', '', parts[5]).split('stateProv:')
teamCount = re.sub('"', '', parts[6]).split('country:')
print("Location:", teamCity[1] + ',', teamProv[1] + ',', teamCount[1])

teamWebsite = re.sub('"', '', parts[7]).split('website:')
print("Website:", teamWebsite[1])

teamYear = re.sub('"', '', parts[8]).split('rookieYear:')
print("Rookie year:", teamYear[1])
