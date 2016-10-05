# Makefile per il lab computazionale! :)

# vars
#RSYNC_OPTS=--links
#TEST_FILES=index.html bianucci-custom.less bootstrap photos
#BASEDIR=/home/tommaso/Repo/Tesi_triennale
BASEDIR=`cd .. && pwd`
REPDIR=$(BASEDIR)/Report
OUTDIR=$(REPDIR)/Out

TEXOPTS=-output-directory=$(OUTDIR)
AUTOPTS=-interaction nonstopmode
# end vars

init:
	mkdir -p $(OUTDIR)

compile:
	pdflatex $(TEXOPTS) $(REPDIR)/report.tex
# bibcompile:
# 	pdflatex $(TEXOPTS) $(MANDIR)/tesi.tex
# 	$(BIBENVS) bibtex $(OUTDIR)/tesi.aux
# 	pdflatex $(TEXOPTS) $(MANDIR)/tesi.tex
# 	pdflatex $(TEXOPTS) $(MANDIR)/tesi.tex
compileauto:
	pdflatex $(AUTOPTS) $(TEXOPTS) $(REPDIR)/report.tex
# bibcompileauto:
# 	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/tesi.tex
# 	$(BIBENVS) bibtex $(OUTDIR)/tesi.aux
# 	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/tesi.tex
# 	pdflatex $(AUTOPTS) $(TEXOPTS) $(MANDIR)/tesi.tex
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
