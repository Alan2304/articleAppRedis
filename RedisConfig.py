import redis as rd

HOSTNAME = 'localhost'
PORT = 6379
DB = 0

def connect():
    try:
        r = rd.StrictRedis(host=HOSTNAME, port=PORT, db=DB)
        return r, r.ping()
    except:
        return r, False