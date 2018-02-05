# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
JUPYTERBUILD  = jupyter-nbconvert
JUPYTERDIR    = notebooks
SPHINXPROJ    = LearningMoreWithTwitterData
SOURCEDIR     = source
BUILDDIR      = build


SITETAG       =  "<!-- Global site tag (gtag.js) - Google Analytics --> <script async src=\"https://www.googletagmanager.com/gtag/js?id=UA-30775-108\"></script> <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'UA-30775-108'); </script>"


NOTEBOOKSOURCES := $(shell find $(JUPYTERDIR) -name '*.ipynb')
NOTEBOOK_BASENAMES := $(basename $(notdir $(NOTEBOOKSOURCES)))


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile


jupyter:
	for notebook in $(NOTEBOOK_BASENAMES); do \
	  $(JUPYTERBUILD) --to rst $(JUPYTERDIR)/$$notebook.ipynb --stdout | sed 's/ipython3/python/' | sed 's/.*parsed-literal.*/::/' > $(JUPYTERDIR)/$$notebook.rst ;\
	done
	mv $(JUPYTERDIR)/*.rst $(SOURCEDIR)
	mv $(JUPYTERDIR)/*files $(SOURCEDIR)


add-sitetag:
	echo $(SITETAG)
	for page in $(NOTEBOOK_BASENAMES); do \
	  sed -i '<meta name="apple-mobile-web-app-capable" content="yes">/a \n '$$SITETAG'' build/html/$$page.html ;\
	done



# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
