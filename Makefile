FRONTEND := $(shell find . -maxdepth 2 -name frontend)
NPM := npm --prefix=$(FRONTEND)
NCU := ncu --cwd=$(FRONTEND)

set_release = \
	find . -maxdepth 2 -name version.py -print0 | \
	xargs -0 sed -i "s/\(__release__ = \).*/\1$1/g"

.PHONY: install
install: dev
	$(NPM) install
	pip install -e .

.PHONY: run
run: dev
	$(NPM) run dev

.PHONY: upgrade
upgrade: upgrade-frontend upgrade-wheel

.PHONY: upgrade-frontend
upgrade-frontend: dev
	npm install --global npm-check-updates
	$(NCU) --upgrade
	$(NPM) update

.PHONY: upgrade-wheel
upgrade-wheel: dev
	pip install pip --upgrade
	pip install -e . --upgrade

.PHONY: build
build: build-frontend build-wheel

.PHONY: build-frontend
build-frontend: release
	$(NPM) run build

.PHONY: build-wheel
build-wheel: release
	python setup.py bdist_wheel

.PHONY: upload
upload:
	twine upload dist/*

.PHONY: dev
dev:
	$(call set_release,False)

.PHONY: release
release:
	$(call set_release,True)
