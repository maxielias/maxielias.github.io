import subprocess
import venv

try:
    venv.create('venv')
except Exception as e:
    raise (e)