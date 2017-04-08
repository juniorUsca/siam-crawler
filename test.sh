#!/bin/bash

for i in {20110634..99999999..90000}
do
	{ echo ========desde "$i" hasta "$(($i + 90000 - 1))"===============; `scrapy crawl siam -a ini=$i -a fin=$(($i + 90000 - 1))` ; echo ejecuntando proceso "$i"; } &
	wait
done


echo all jobs are done!
