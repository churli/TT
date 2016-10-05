#!/bin/bash

OUTFILE="Out/report.pdf"

ECHECK=`ps aux | grep "evince $OUTFILE" | awk '{print $2}'`
if [ "$ECHECK" ]; then
    EPID="$ECHECK"
else
    evince $OUTFILE &
    EPID="$!"
fi

OLD=`find . -name "*.tex" -exec cat '{}' \; | md5sum | grep -o "^[^ ]*"`
while true; do
    ERUN=`ps aux | awk '{print $2}' | grep "^$EPID$"`
    if [ ! "$ERUN" ]; then
	evince $OUTFILE &
	EPID="$!"
    fi
    CUR=`find . -name "*.tex" -exec cat '{}' 2>/dev/null \; | md5sum | grep -o "^[^ ]*"`
    if [[ "$CUR" != "$OLD" ]]; then
	if [[ $RANDOM -ge 6552 ]]; then
	    #succede con 4/5 di prob
	    make compileauto
	else
	    #make bibcompileauto
	    make compileauto
	fi
	OLD=$CUR
	date
    fi
    sleep 2s
done
