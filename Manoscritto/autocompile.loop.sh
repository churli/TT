#!/bin/bash

evince Out/tesi.pdf &
EPID="$!"

OLD=`find . -name "*.tex" -exec cat '{}' \;`
while true; do
    ERUN=`ps aux | awk '{print $2}' | grep "^$EPID$"`
    if [ ! "$ERUN" ]; then
	evince Out/tesi.pdf &
	EPID="$!"
    fi
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
