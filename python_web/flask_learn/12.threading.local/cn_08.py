from threading import Thread
try:
    from greenlet import getcurrent as get_ident
except Exception as e:
    from threading import get_ident


class Local(object):

    def __init__(self):
        # self.storage = {}
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][k] = v
        else:
            self.storage[ident] = {k: v}

    def __getattr__(self, k):
        ident = get_ident()
        return self.storage[ident][k]


obj = Local()


def task(arg):
    obj.val = arg
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
