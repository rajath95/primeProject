#!/bin/sh

a=` ps -aux| grep runserver | cut -d " " -f4-6 `

for process in $a
do 
	
	kill -9 $process >> /dev/null
done



