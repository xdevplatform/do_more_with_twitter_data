# Minimal makefile for Sphinx documentation
# With hacky additions for directly building from Jupyter

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
JUPYTERBUILD  = jupyter-nbconvert
JUPYTERDIR    = examples
SPHINXPROJ    = LearningMoreWithTwitterData
SOURCEDIR     = docs/source
BUILDDIR      = docs/build


NOTEBOOKSOURCES := $(shell find $(JUPYTERDIR) -name '*.ipynb')
NOTEBOOK_BASENAMES := $(basename $(NOTEBOOKSOURCES))


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile


jupyter:
	$(foreach notebook, $(NOTEBOOKSOURCES), \
	  $(JUPYTERBUILD) --to rst $(notebook)  ;\
	  mv $(basename $(notebook)).rst $(basename $(notebook)).tmp ;\
	  cat $(basename $(notebook)).tmp | sed 's/ipython3/python/' | sed 's/.*parsed-literal.*/::/' | sed 's/code:: \.yaml/code:: yaml/' > $(basename $(notebook)).rst ;\
	  rm $(basename $(notebook)).tmp ;\
	  echo ".. _$(notdir $(basename $(notebook))):" | cat - $(basename $(notebook)).rst > temp ;\
	  mv temp $(basename $(notebook)).rst ;\
	  mv -f $(basename $(notebook)).rst $(SOURCEDIR) ;\
	  rm -r $(SOURCEDIR)/$(notdir $(basename $(notebook)))_files ;\
	  mv -f $(basename $(notebook))_files $(SOURCEDIR) ;\
	  )


bokeh:
	cp ./examples/clustering_users/hdbscan_bokeh.html ./docs/build/html/_static
	cp ./examples/clustering_users/kmeans_bokeh.html ./docs/build/html/_static




# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
