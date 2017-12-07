#!/bin/sh

a=` ps -aux| grep runserver | cut -d " " -f5 `

for process in $a
do 
	
	kill -9 $process >> /dev/null
done



