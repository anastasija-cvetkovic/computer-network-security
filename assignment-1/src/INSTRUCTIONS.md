UPUTSTVO ZA POKRETANJE I RAD SA PROGRAMOM

ZAHTEVI:

- Python 3.x mora biti instaliran na sistemu

SIFRIRANJE:
python encrypt.py
ili
python3 encrypt.py

DESIFROVANJE:
python decrypt.py
ili
python3 decrypt.py

KREIRANJE IZVRSNIH VERZIJA (.exe):

Instalirajte PyInstaller:
pip install pyinstaller

Zatim izvrsite komande:
python -m PyInstaller --onefile --name encrypt encrypt.py
python -m PyInstaller --onefile --name decrypt decrypt.py

UPUTSTVO ZA KORISCENJE:

Program ce zatraziti unos matrice kljuca 4x4. Za svaki red unesite 4 broja izmedju 0 i 26 odvojena razmakom.

Nakon unosa kljuca, program ce proveriti validnost kljuca (da li postoji inverzna matrica po modulu 27).

Ako je kljuc validan, program ce zatraziti unos teksta za sifriranje ili desifrovanje.

Ako kljuc nije validan, program se prekida sa porukom o gresci.

NAPOMENA:

- Program radi sa osnovnim latiničkim slovima (a-z) bez dijakritika zbog modula 27 (26 slova + 1 razmak). Karakteri sa dijakriticima (š, č, ć, ž, đ) će biti uklonjeni tokom obrade teksta.
- Slova lj, nj i dž se tretiraju kao par slova razdvojenih blanko znakom (npr. "l j")
- Program automatski dodaje razmake na kraju teksta ako je potrebno za blokove od 4 karaktera
