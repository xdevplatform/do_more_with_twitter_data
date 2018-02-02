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


NOTEBOOKSOURCES := $(shell find $(JUPYTERDIR) -name '*.ipynb')


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile


jupyter:
	echo $(NOTEBOOKSOURCES)
	# for notebook in $(NOTEBOOKSOURCES); do \
	#   echo $$notebook; \
	# done
	for notebook in $(NOTEBOOKSOURCES); do \
	  $(JUPYTERBUILD) --to rst $$notebook ; \
	done
	mv $(JUPYTERDIR)/*.rst $(SOURCEDIR)
	mv $(JUPYTERDIR)/*files $(SOURCEDIR)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
