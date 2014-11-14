#!/bin/bash

ECHECK=`ps aux | grep "evince Out/tesi.pdf" | awk '{print $2}'`
if [ "$ECHECK" ]; then
    EPID="$ECHECK"
else
    evince Out/tesi.pdf &
    EPID="$!"
fi

OLD=`find . -name "*.tex" -exec cat '{}' \;`
while true; do
    ERUN=`ps aux | awk '{print $2}' | grep "^$EPID$"`
    if [ ! "$ERUN" ]; then
	evince Out/tesi.pdf &
	EPID="$!"
    fi
    CUR=`find . -name "*.tex" -exec cat '{}' 2>/dev/null \;`
    if [[ "$CUR" != "$OLD" ]]; then
	if [[ $RANDOM -ge 6552 ]]; then
	    #succede con 4/5 di prob
	    make autocompile
	else
	    make autobibcompile
	fi
	OLD=$CUR
	date
    fi
    sleep 2s
done
