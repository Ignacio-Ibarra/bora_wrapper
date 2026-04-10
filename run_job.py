import subprocess
from datetime import datetime
from typing import Literal
import argparse

def links_rubro(rubro: Literal["CONSTITUCION SA", "CONSTITUCION SAS", "CONTRATO SRL"])-> None:

    today = datetime.today().strftime(format="%d/%m/%Y")

    print(today)

    try: 
        
        command = [
            'uv', 'run', 'bora-cli', 
            '--start-date', today,
            '--end-date', today,
            '--rubro', rubro
        ]

        subprocess.run(command)
    
    except subprocess.CalledProcessError as e:
        print(f"Error durante la ejecución: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extracción de links de un rubro determinado")
    parser.add_argument("--rubro", required=True, help="Pasar un rubro: Literal['CONSTITUCION SA', 'CONSTITUCION SAS', 'CONTRATO SRL']")
    arg = parser.parse_args()
    rubro = arg.rubro

    return links_rubro(rubro=rubro)

if __name__ == "__main__":

    main()
    