.PHONY: All 

All:
	sudo pip install pycryptodome	
	chmod +x ctr-enc
	chmod +x ctr-dec
	chmod +x cbc-enc
	chmod +x cbc-dec
