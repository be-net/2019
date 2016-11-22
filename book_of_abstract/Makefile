CHAPS_TMP=$(wildcard chap-*.jinja)
CHAPS_CMP=$(patsubst chap-%.jinja, chap-%, $(CHAPS_TMP))
POSTDEST=../content/abs

.PHONY: all clean abs topost

all: program.pdf prog.md boa.pdf

prog.tex: render_jinja.py prog.tex.jinja prog.yaml abs/*.yaml
	rm -f prog.tex
	python render_jinja.py prog.yaml prog.tex.jinja > prog.tex

$(CHAPS_CMP): render_jinja.py prog.yaml $(CHAPS_TMP) abs/*.yaml
	python render_jinja.py prog.yaml $@.jinja > $@

program.pdf: prog.tex program.tex $(CHAPS_CMP)
	latexmk -lualatex program.tex

boa.pdf: prog.tex $(CHAPS_CMP) boa.tex
	latexmk -lualatex boa.tex


prog.md: render_jinja.py prog.yaml prog.md.jinja
	rm -f prog.md
	python render_jinja.py prog.yaml prog.md.jinja > prog.md
	cp -f prog.md ../content/page/prog.md

prog.html: render_jinja.py prog.html.jinja prog.yaml abs
	rm -f prog.html
	python render_jinja.py prog.html.jinja > prog.html

clean:
	latexmk -C
	
toposts: abs/*.yaml render_jinja.py post.md.jinja
	mkdir -p $(POSTDEST)
	rm -f $(POSTDEST)/*
	for f in abs/{talk,graham,poster}*.yaml; \
	do \
	  echo $${f}; \
	  fname=`basename $${f}`;\
	  newf=$${fname/yaml/md};\
	  python render_jinja.py $${f} post.md.jinja > $(POSTDEST)/$${newf}; \
	done;
	
