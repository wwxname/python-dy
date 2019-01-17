import threading
class User(object):
    def __init__(self,roles=()):
        self.roles = roles
class Unauthorized(Exception):
    pass

user = threading.local()

def protect(role):
    def _protect(function):
        def __protect(*args,**kwargs):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized('i can not tell you')
            return function(*args,**kwargs)
        return __protect
    return _protect

wwx = User(('admin'))

wwj = User(('user'))

class MyJob(object):
    @protect('admin')
    def work(self):
        print('admin can job')

job = MyJob()
user = wwx
job.work()
user = wwj
job.work()