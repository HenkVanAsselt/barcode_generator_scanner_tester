# Makefile for Python Barcode generator

.DEFAULT_GOAL := all

# all: develop

install_requirements:
	pip install -r requirements.txt

remember:
	@echo --------------------------------------------------
	@echo "Hello from the Makefile..."
	@echo "Don't forget to run: 'make install_requirements'"
	@echo --------------------------------------------------

clean:
	@rm -f -R src/build
	@rm -f -R src/dist src/log
	@rm -f -R .eggs *egg-info
	@rm -f -R .pytest_cache
	@rm -f -R lib\__pycache__
	@rm -f -R tests\__pycache__
	@rm -f -R doc\doxygen\build
	@rm -f -R doc\sphinx-autodoc\build

pep8: remember
	flake8 --max-complexity 12 --exit-zero --ignore=E501 src/barcode_generator.py

flake8: pep8

lint: remember
	pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" -r n -d E0611,R0201,C0301 src/barcode_generator.py

pylint: lint

coverage:
	coverage report -m

test: lint pep8 nosetests coverage

pytest:
	py.test tests

exe:
	make_exe.cmd

bumpversion:
	cd ./src && python bumpversion.py
	.\src\version_to_env.cmd


#sphinx:
#	cd doc\sphinx-autodoc & make clean & make html & cd ...

#doxygen:
#	cd doc\doxygen & "C:\Program Files\doxygen\bin\doxygen.exe" & cd ...