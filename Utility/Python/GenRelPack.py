#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from subprocess import run
from shutil import move, copyfile

bltxtfile = "bootloader.txt"
apptxtfile = "app.txt"

bl_startaddr = 0xc400
blver_startaddr = 0xdbfc
app_startaddr = 0xdc00
appver_startaddr = 0xff7c

size = 0x10000 - bl_startaddr
array = [0] * size

def change_dir(file_dir):
    if file_dir == bltxtfile:
        os.chdir('bootloader/Release')
    elif file_dir == apptxtfile:
        os.chdir('../../app/Release')
    else:
        os.chdir(file_dir)

def get_txtdatas(srcfile):
    change_dir(srcfile)
    with open(srcfile) as in_file:
        lines = (line.rstrip('\n') for line in in_file)
        for line in lines:
            if not len(line) or line.startswith('#'):
                continue
            else:
                if line[0] == "@":
                    addr = get_address(line)
                    Cnt = 0
                    continue
                elif line[0] == "q":
                    break
                else:
                    if addr == 0xff80:
                        continue
                    Cnt = get_datas(line, addr, Cnt)

def get_address(line):
    return int(line[1:5], 16)

def get_datas(line, addr, Cnt):
    words = line.split()
    for byteData in words:
        arridx = addr - bl_startaddr + Cnt
        array[arridx] = int(byteData, 16)
        Cnt = Cnt + 1
    return Cnt

def get_app_checksum():
    limit = 0x10000
    idx = app_startaddr - bl_startaddr
    cs = 0
    while idx < size:
        cs = (cs+array[idx])%limit
        idx = idx + 1
    return [(cs & 0x00ff),((cs & 0xff00) >> 8 )]

def get_off_checksum():
    limit = 0x10000
    idx = 0
    cs = 0
    while idx < size:
        cs = (cs+array[idx])%limit
        idx = idx + 1
    return cs    
 
def get_rstaddr():
    return [array[-2], array[-1]]
    
def write_bl_rstaddr(bl_rstaddr):
    array[-2] = bl_rstaddr[0]
    array[-1] = bl_rstaddr[1]

def get_version():
    count = 0
    bl_idx = blver_startaddr - bl_startaddr
    app_idx = appver_startaddr - bl_startaddr

    return  {
                "bl" : "{:02d}_{:02d}_{:02d}_{:02d}".format(array[bl_idx+3], array[bl_idx+2], array[bl_idx+1], array[bl_idx]),
                "app": "{:02d}_{:02d}_{:02d}_{:02d}".format(
                    array[app_idx+3], array[app_idx+2], array[app_idx+1], array[app_idx])
    }

def get_offline_filename():
    change_dir('../../')
    app_ver=get_version()['app']
    bl_ver = get_version()['bl']
    return ("Galactica_Offline_app_"+app_ver+"_bl_"+bl_ver+".txt")

def write_app_msg(out_file):
    out_file.write("@1800 \n")
    out_file.write("{:02x} {:02x} {:02x} {:02x} \n".format(
        get_rstaddr()[0], get_rstaddr()[1], get_app_checksum()[0], get_app_checksum()[1]))

def write_regdatas(out_file):
    out_file.write("@C400 \n")
    offset = 0
    while offset < size:
        count = 0
        while count < 16:
            i = offset+count
            out_file.write("%02x " % (array[i]))
            count += 1
        out_file.write('\n')
        offset = offset + 16

def creat_offline_txt(output_file, bl_rstaddr):
    with open(output_file, 'w') as out_file:
        write_app_msg(out_file)
        write_bl_rstaddr(bl_rstaddr)
        write_regdatas(out_file)

def get_file_size(fname):
    statinfo = os.stat(fname)
    return statinfo.st_size

def creat_off_checksumfile(offtxt_filename):
    with open('checksum.txt', 'w') as off_cs_file:
        off_cs=get_off_checksum()
        fs= get_file_size(offtxt_filename) / 1024
        off_cs_file.write("%s checksum is %04x \r\n" % (offtxt_filename,off_cs))
        off_cs_file.write("%s filesize is %.2g KB" % (offtxt_filename,fs))

    

def get_off_allfiles():
    get_txtdatas(bltxtfile)
    bl_rstaddr = get_rstaddr()

    get_txtdatas(apptxtfile)

    offtxt_filename = get_offline_filename()
    creat_offline_txt(offtxt_filename, bl_rstaddr)
    creat_off_checksumfile(offtxt_filename)
    return offtxt_filename
####################################################################

def creat_folders():
    rel_dir = ('Galactica_' + get_version()['app'])
    if not os.path.isdir(rel_dir):
        os.makedirs(rel_dir)
    change_dir(rel_dir)

    if not os.path.isdir('online'):
        os.makedirs('online')
    if not os.path.isdir('offline'):
        os.makedirs('offline')
    change_dir('offline')

def pack_rel_allfiles(offtxt_filename):
    creat_folders()
    move('../../'+offtxt_filename, offtxt_filename)
    move('../../checksum.txt', 'checksum.txt')

    change_dir('../online/')
    copyfile('../../app/Release/app.bin', '../online/app.bin')
    copyfile('../../bootloader/Release/bootloader.bin',
             '../online/bootloader.bin')

def main():
    Cnt = 0

    offtxt_filename = get_off_allfiles()
    pack_rel_allfiles(offtxt_filename)

if __name__ == '__main__':
    main()
