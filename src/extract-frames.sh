#!/bin/sh

dir=${0%/*}

echo $dir

for i in $(find $dir -name '*.mp4'); do 
	fn=${i##*/}
	mkdir $dir/frames/${fn%.*}
	ffmpeg -i $i -r 0.5 $dir/frames/${fn%.*}/frame_%05d.jpg 
done