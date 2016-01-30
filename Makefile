default: help

help:
	@echo "make clean|stage|upload"

clean:
	@rm -rf build dist j2t.egg-info

stage:
	./setup.py sdist
	./setup.py bdist_wheel

upload:
	twine upload dist/*
