# Python Intermediate course 

Just examples taken from [here](https://www.youtube.com/watch?v=HGOBQPFzWKo)


# enviroment setup 

Pyenv 

    brew install pyenv

List version

    pyenv install --list

    
create your venv

    python3 -m venv venv 

source your venv 

    source venv/bin/activate

install modules 

    pip3 install -r requirements.txt

Issues with pyenv install 

    esta correctamente instalado? 

    atching file 'Tools/ssl/multissltests.py'
    
    python-build: use readline from homebrew
    python-build: use zlib from xcode sdk
    
    
    
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
        import lzma
      File "/Users/xxxxx/.pyenv/versions/3.14.0/lib/python3.14/lzma.py", line 28, in <module>
        from _lzma import *
    ModuleNotFoundError: No module named '_lzma'
    WARNING: The Python lzma extension was not compiled. Missing the lzma lib?
    Installed Python-3.14.0 to /Users/xxxxx/.pyenv/versions/3.14.0

Fix

    brew install xz

Then 

    pyenv install x.x.x --force
