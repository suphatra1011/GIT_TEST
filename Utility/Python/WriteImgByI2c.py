#!/usr/bin/python
## ** The tool is based on python3.7 and i2ctransfer 4.1

import sys , os , stat

byteSize = 16
eepromSize = 512
eepromMaxSize=65535
wrData = [0xff] * eepromSize
rdData = [0xff] * eepromSize    

def parseArgv():
    #busNum=1  
    #slaveAddr="0x54" 
    #fileName="FwImg.bin"

    if len(sys.argv) > 1 : 
        busNum = (sys.argv[1])
        slaveAddr = (sys.argv[2])
        fileName=(sys.argv[3])
        return [busNum , slaveAddr , fileName]
    else :
        print("Usage : WriteImgByI2c.py I2C_busNum I2C_SlaveAddr FileName")
        os.exit(1)
    #return [busNum , slaveAddr , fileName]

def cmpData(wrData,rdData):
    return True if wrData == rdData else False

def getChecksum(array):
    limit = 0x10000
    idx = 0
    checksum = 0
    while idx < eepromSize:
        checksum = (checksum+int(array[idx],16))%limit
        idx = idx + 1
    return checksum    

def getDatas(filename):
    with open(filename, "rb") as binFile:
        idx = 0 
        checksum=0
        limit = 0x10000
        
        while idx < eepromSize :
            dataBlock = binFile.read(1)    
            if not dataBlock:
                break
            wrData[idx] = hex(dataBlock[0])
            idx = idx + 1

def confirmI2cTool():
    myFile = Path("./i2ctransfer")
    if myFile.exists():
        os.chmod(myFile, stat.S_IXUSR|stat.S_IXGRP|stat.S_IXOTH)
        retrun True
    else :
        print("Can't find i2ctransfer.")
        return False

def i2cCmd(busNum, slaveAddr, offset, wr_rd, wrSize, rdSize, data):
    offsetSize = 2
    if confirmI2cTool :
        if wr_rd == "w" :
            cmd = './i2ctransfer -f -y '+ str(busNum) +' w'+str(offsetSize+wrSize)+'@'+ slaveAddr +' '+ hex(int(offset/256)) +' '+ hex(int(offset%256)) + data      
            return os.system(cmd)    

        elif wr_rd in ("r","wr"):
            cmd = './i2ctransfer -f -y '+ str(busNum) +' w'+str(offsetSize)+'@'+ slaveAddr +' '+ hex(int(offset/256)) +' '+ hex(int(offset%256)) +' r'+ str(rdSize) 
            return os.popen(cmd).read()
    else:        
        os.exit(1)

def write_erase_eeprom(busNum, slaveAddr, eraseMode):
    dataBlock =""
    data=""
    offset=0
    status=1

    while offset < eepromSize:       
        for i in range(byteSize):
            if eraseMode == True :
                data = hex(0xff)
            else :
                data = wrData[i+offset]   
            dataBlock = dataBlock +' '+ str(data)
        status=i2cCmd(busNum, slaveAddr, offset, "w", byteSize, 0, dataBlock)

        if status != 0 :
            print("Can't write.")
            return False
        dataBlock =""
        offset = offset + byteSize
    return True

def read_eeprom(busNum, slaveAddr):
    dataBlock =""
    data=""
    offset=0

    while offset < eepromSize :
        if offset == 0:
            dataBlock=i2cCmd(busNum, slaveAddr, offset,"r", 1, byteSize, 0).strip("\n")
        else :
            dataBlock=dataBlock+" "+i2cCmd(busNum, slaveAddr, offset,"r", 1, byteSize, 0).strip("\n")
        data=dataBlock.split(" ")
        offset = offset + byteSize
    
    for i in range(0, len(data)):
        if hex(int(data[i],16)) == False :
            print("Can't read.")
            return False
        rdData[i]= hex(int(data[i],16))
    return True

def cmpResult():
    if cmpData(getChecksum(wrData),getChecksum(rdData)) :
        print("  Checksum match.")
        return True
    else:
        print("Checksum doesn't match.")
        return False

def showImg(imgData):
    item=""
    data=""

    for i in range(0, byteSize):
        item=item + " " + '%02x'%i
    print("    "+item)

    for row in range(0, int(len(imgData)/byteSize)):
        for col in range(0, byteSize):
            data = data+" "+'%02x'%int(imgData[row*byteSize+col],16)
        blockData= '%03x'%(row*byteSize) +" "+data 
        print(blockData)
        data=""


if __name__ == '__main__' :
    if eepromSize >= byteSize and eepromMaxSize >= eepromSize:
        [busNum , slaveAddr , fileName] = parseArgv()
        getDatas(fileName)
        retErase = write_erase_eeprom(busNum,slaveAddr,True)
        if retErase :
            retWr=write_erase_eeprom(busNum, slaveAddr, False)
            if retWr :     
                retRd=read_eeprom(busNum, slaveAddr)
                if retRd :     
                    retCmp=cmpResult()
                    if retCmp :    
                        print("Programming successfully.")
                        showImg(rdData)
                        os._exit(0)
    print("Failed to program.")
        
