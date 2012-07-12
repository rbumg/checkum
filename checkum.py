import sys
import hashlib

class checkum:
    def __init__(self):

        if len(sys.argv) == 1:
            self.usage()
        else:
            file = sys.argv[1]
            print self.md5checksum(r'%s' % file)

    def usage(self):
        print 'Please provide a valid file to check. \n'
        print 'Usage: \n\t checkum.py FILENAME'
        
    def md5checksum(self, file):
        md5 = hashlib.md5()
        with open(file,'rb') as f:
            for chunk in iter(lambda: f.read(128*md5.block_size), b''):
                md5.update(chunk)
        return md5.hexdigest()

if __name__ == '__main__':
    md5 = checkum()
    
