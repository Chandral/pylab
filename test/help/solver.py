import os
from pathlib import Path

def makedir():
    Path(os.getcwd() + '/Logs').mkdir(parents=True, exist_ok=True)