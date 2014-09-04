#!/bin/bash

OLD=`find . -name "*.tex" -exec cat '{}' \;`
while true; do
    CUR=`find . -name "*.tex" -exec cat '{}' \;`
    if [[ "$CUR" != "$OLD" ]]; then
	if [[ $RANDOM -ge 6552 ]]; then
	    #succede con 4/5 di prob
	    make compile
	else
	    make bibcompile
	fi
	OLD=$CUR
	date
    fi
    sleep 2s
done
