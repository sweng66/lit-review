from flask.ext.login import (UserMixin, AnonymousUser)
                             
HOST = '0.0.0.0'
PORT = 5000
DEBUG = 'TRUE'
SECRET_KEY = "this is a super secret! =)"

DBTYPE = 'oracle'
DBHOST = 'SERVER:PORT'
DBNAME = 'DBNAME_HERE'
DBUSER = 'USER_NAME_HERE'
DBPASS = 'PASSWORD_HERE'
SCHEMA = 'SCHEMA_HRRE'

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active

class Anonymous(AnonymousUser):
    name = u"Anonymous"

    
USERS = {
    1: User(u"maria", 1),
    2: User(u"john", 2),
    3: User(u"mary", 3),
    4: User(u"julie", 4),
    5: User(u"guest", 6, False),
}

USER_NAMES = dict((u.name, u) for u in USERS.itervalues())

