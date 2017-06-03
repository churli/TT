#!/bin/bash

ECHECK=$(ps aux | grep "evince Out/presentation.pdf" | awk '{print $2}')
if [ "$ECHECK" ]; then
    EPID="$ECHECK"
else
    evince Out/presentation.pdf &
    EPID="$!"
fi

OLD=$(find . -name "*.tex" -exec cat '{}' 2>/dev/null \; | md5sum | grep -o "^[^ ]*")
OLDCITE=$(find . -name "*.tex" -exec cat '{}' 2>/dev/null \; | grep -o "\\\cite{[^}]*}" | md5sum | grep -o "^[^ ]*")
while true; do
    ERUN=`ps aux | awk '{print $2}' | grep "^$EPID$"`
    if [ ! "$ERUN" ]; then
	evince Out/presentation.pdf &
	EPID="$!"
    fi
    CUR=$(find . -name "*.tex" -exec cat '{}' 2>/dev/null \; | md5sum | grep -o "^[^ ]*")
    CITE=$(find . -name "*.tex" -exec cat '{}' 2>/dev/null \; | grep -o "\\\cite{[^}]*}" | md5sum | grep -o "^[^ ]*")
    if [[ "$CUR" != "$OLD" ]]; then
	if [[ "${CITE}" == "${OLDCITE}" ]]; then
	    echo "Starting target COMPILE"
	    make compileauto
	    echo "Target COMPILE completed"
	else
	    echo "Starting target BIBCOMPILE"
	    make bibcompileauto
	    echo "Target BIBCOMPILE completed"
	fi
	OLD=$CUR
	OLDCITE=${CITE}
	date
    fi
    sleep 2s
done
