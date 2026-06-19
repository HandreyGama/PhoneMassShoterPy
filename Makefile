py = python
main = main.py
req = requirements.txt

setup:
	pip install req
run-script:
	py main.py --type="script"
run-server:
	py main.py --type="server"	
	