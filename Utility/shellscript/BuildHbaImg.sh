#!/bin/bash
#########################################################################				            
# @ Function  : Check fw and build binary  #
#@ CMD parameter : HexdumpCMD(xxd) -Captical -group Num FileName 
#@ Use Patter : FW
#----@ FW Patter : "05 00 00 00 FF 06" 
#----@ NVdatd Patter(SASParser) : "53 41 53 50 61 72 73 65 72". 
#########################################################################

#== [Way 1] ==#
#== FW Patter : "05 00 00 00 FF 06" ==#
#Key_Cmd=`xxd -u -g 1 Key.fw | grep "05 00 00 00 FF 06"`

Patter="05 00 00 00 FF 06"
FW_FILENAME=`find *.* -name '*.fw'`
Key_Cmd=`xxd -u -g 1 $FW_FILENAME | grep "$Patter"`

if  [ "$?"  -eq 0 ]; then 
#		echo $ECHO
		echo  found "$Key_Cmd "
		echo This is a clear Fw.
		#Build Binary
		echo Build Binary...
		
		read -p "Please select NVdata file : " -t 100 NVdata_Name
		./sas2parser.exe -insert $NVdata_Name.xml nvdata.xsl $FW_FILENAME $NVdata_Name.bin
		
		echo Finish Build Binary.
		
else #NVdatd have String(SASParser) "53 41 53 50 61 72 73 65 72".
	echo No found "$Key_Cmd" .
	echo Include NVdata.
fi


##== [Way 2] ==#
##== #NVdatd Patter(SASParser) : "53 41 53 50 61 72 73 65 72". ==#
##Key_Cmd=`xxd -u -g 1 Key.fw | grep "53 41 53 50 61 72 73 65 72"`


#Patter="53 41 53 50 61 72 73 65 72"
#BIN_FILENAME=`find *.* -name '*.bin'`
#Key_Cmd=`xxd -u -g 1 $BIN_FILENAME | grep "$Patter"`
#if  [ "$?"  -eq 1 ]; then 
#		echo  found "$Key_Cmd"
#		echo Include NVdata.
#else 
#  echo No found NVdata. "$Key_Cmd" 
#	echo Clear Fw.
#	#Build Binary
#	read -p "Please select NVdata file : " -t 100 NVdata_Name
#	./sas2parser.exe -insert $NVdata_Name.xml nvdata.xsl $FW_FILENAME $NVdata_Name.bin
#fi






