# Makefile per la TESI! :)

# vars
#RSYNC_OPTS=--links
#TEST_FILES=index.html bianucci-custom.less bootstrap photos
#BASEDIR=/home/tommaso/Repo/Tesi_triennale
BASEDIR=`cd .. && pwd`
MANDIR=$(BASEDIR)/Presentation
OUTDIR=$(MANDIR)/Out

TEXOPTS=-output-directory=$(OUTDIR)
BIBENVS=BIBINPUTS=$(MANDIR) TEXMFOUTPUT=$(OUTDIR)
AUTOPTS=-interaction nonstopmode
# end vars

init:
	mkdir -p $(OUTDIR)

compile:
	pdflatex $(TEXOPTS) $(MANDIR)/presentation.tex
bibcompile:
	pdflatex $(TEXOPTS) $(MANDIR)/presentation.tex
	$(BIBENVS) bibtex $(OUTDIR)/presentation.aux
	pdflatex $(TEXOPTS) $(MANDIR)/presentation.tex
	pdflatex $(TEXOPTS) $(MANDIR)/presentation.tex
compileauto:
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/presentation.tex
bibcompileauto:
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/presentation.tex
	$(BIBENVS) bibtex $(OUTDIR)/presentation.aux
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/presentation.tex
	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/presentation.tex
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
