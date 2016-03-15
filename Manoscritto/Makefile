# Makefile per la TESI! :)

# vars
#RSYNC_OPTS=--links
#TEST_FILES=index.html bianucci-custom.less bootstrap photos
#BASEDIR=/home/tommaso/Repo/Tesi_triennale
BASEDIR=`cd .. && pwd`
MANDIR=$(BASEDIR)/Manoscritto
OUTDIR=$(MANDIR)/Out

TEXOPTS=-output-directory=$(OUTDIR)
BIBENVS=BIBINPUTS=$(MANDIR) TEXMFOUTPUT=$(OUTDIR)
AUTOPTS=-interaction nonstopmode
# end vars

compile:
	pdflatex $(TEXOPTS) $(MANDIR)/tesi.tex
bibcompile:
	pdflatex $(TEXOPTS) $(MANDIR)/tesi.tex
	$(BIBENVS) bibtex $(OUTDIR)/tesi.aux
	pdflatex $(TEXOPTS) $(MANDIR)/tesi.tex
	pdflatex $(TEXOPTS) $(MANDIR)/tesi.tex
compileauto:
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/tesi.tex
bibcompileauto:
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/tesi.tex
	$(BIBENVS) bibtex $(OUTDIR)/tesi.aux
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/tesi.tex
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/tesi.tex
autocompile:
	./autocompile.loop.sh
push:
	go phc -- echo "foo" 1>/dev/null
	git push --mirror #Ricordati di settare --mirror=push anche per il repo PHC
	#git push casa #Quando hai fatto il salvataggio anche sul server di casa
	git push --mirror dropbox
	git push -u github master
sync:
	push
# test:
# 	$(foreach s,$(TEST_FILES),go -m rsync -D -r -i $(s) -o r:~/public_html/etc/development/ phc -- $(RSYNC_OPTS);)
clean:
	echo "Cleaning outfiles..."
	rm $(OUTDIR)/*

#EOF
