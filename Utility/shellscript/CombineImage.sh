#!/bin/bash

# Combined Binary
#
#

if [ "$#" -ne 4 ]; then
    echo "The argument is error!"
    echo "Usage: $0 source1 source2 target target_size"
    exit
fi

if [ ! -f "$1" ]; then
    echo "$1 is not exist or format error"
    exit 
fi

if [ ! -f "$2" ]; then
    echo "$2 is not exist or format error"
    exit
fi

if [ "$4" -le 32 ]; then
    echo "Target size must be an integer and greater than 32 (e.g., 128, 256)"
    exit
fi

date=`date '+%F'`
temp_file=$date.transfer_temp.bin

tr '\000' '\377' < /dev/zero | dd of=$temp_file bs=$4 count=1k

temp_file_size=`stat -c "%s" $temp_file | awk '{print $1}'`

srcFile1=$1
srcFile2=$2

srcFile1_size=`stat -c "%s" $srcFile1 | awk '{print $1}'`
srcFile2_size=`stat -c "%s" $srcFile2 | awk '{print $1}'`

dd if=$srcFile1 of=$temp_file bs=1 count=$srcFile1_size conv=notrunc
dd if=$srcFile2 of=$temp_file bs=1 count=$srcFile2_size seek=32768 conv=notrunc #Notice-seek address

mv $temp_file $3

echo "successfully..."
