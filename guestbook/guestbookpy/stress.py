import requests
import random
import string
import time

CMDS = ["get", "set"]

def stress(url):

    cmd = random.choice(CMDS)
    key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

    url = "{0}/guestbook?cmd={1}&key={2}&value={3}".format(url, cmd, key, value)
    print "Hitting {0}".format(url)
    requests.get(url,timeout=5)


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        while True:
            try:
                stress(str(argv[1]))
                time.sleep(1)
            except Exception, e:
                print str(e)
    else:
        print "Needs a url to be passed (format http://$IP"