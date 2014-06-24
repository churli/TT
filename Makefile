# Makefile per la TESI! :)

# vars
#RSYNC_OPTS=--links
#TEST_FILES=index.html bianucci-custom.less bootstrap photos
BASEDIR=/home/tommaso/Repo/Tesi_triennale
# end vars

compile:
	pdflatex $(BASEDIR)/Manoscritto/tesi.tex
push:
	git push --mirror #Ricordati di settare --mirror=push anche per il repo PHC
	#git push casa #Quando hai fatto il salvataggio anche sul server di casa
	git push --mirror dropbox
sync:
	push
# test:
# 	$(foreach s,$(TEST_FILES),go -m rsync -D -r -i $(s) -o r:~/public_html/etc/development/ phc -- $(RSYNC_OPTS);)
clean:
	echo "Nothing set to clean..."

#EOF
