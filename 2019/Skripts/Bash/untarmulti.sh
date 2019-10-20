#!/bin/bash

i=1000

while [ $i>0 ]
do
	tar -xf ./$i.tar
	let 'i++'
done
