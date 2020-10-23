#!/usr/bin/python3
import sys , os , zlib #binascii
def parse_argv(): 
    if len(sys.argv) != 2:
        sys.exit('Usage: %s {filename}' % os.path.basename(sys.argv[0]))

    if not os.path.exists(sys.argv[1]):
        sys.exit('Error: File Not Exist or Access Denied')
    fileName = (sys.argv[1])    
    return fileName

def computeFileCRC(fname):
    try:
        blocksize = 1024 * 64
        f = open(fname, "rb")
        content = f.read(blocksize)
        crc = 0
        while len(content) != 0:
            crc = zlib.crc32(content,crc) & 0xffffffff
            content = f.read(blocksize)
        f.close()
    except:
        print("compute file crc failed!")
        return 0
    print("The checksum(CRC32) of " + '%s' %(fname) + " is " + '%08X' % (crc))
    getFileSize(fname)
    return 1

def getFileSize(fname):
        print("The filesize(CRC32) of " + '%s' %(fname) + " is " + str(int(os.stat(fname).st_size / 1024)) + "K")

if __name__ == '__main__' :
    computeFileCRC(parse_argv())
