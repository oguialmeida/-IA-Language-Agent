import subprocess

# Para abrir um terminal externo no Windows e rodar o uvicorn
subprocess.Popen(["start", "cmd", "/K", "uvicorn main:app --reload"], shell=True)
