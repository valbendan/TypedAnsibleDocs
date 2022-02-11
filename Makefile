# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= poetry run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


format:
	poetry run black .

.PHONY: build
build:
	make html
	cp -r docs  build/html

fast-build: gen-all-ansible-collections gen-all-ansible-full
	make build

gen-all-ansible-full:
	poetry run python rst.py gen-ansible-full v5.1
	poetry run python rst.py gen-ansible-full v5.2
	poetry run python rst.py gen-ansible-full v5.3


gen-all-ansible-collections:
	poetry run python rst.py gen-collection azure.azcollection
	poetry run python rst.py gen-collection linode.cloud
