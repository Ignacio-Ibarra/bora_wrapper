from bora import SegundaSeccion
import os
from datetime import datetime
import json
import argparse


def main():

    parser = argparse.ArgumentParser(description="Buscar links de la Segunda Sección del BORA")
    parser.add_argument("--start-date", required=True, help="Fecha de inicio en formato dd/mm/YYYY")
    parser.add_argument("--end-date", required=True, help="Fecha de fin en formato dd/mm/YYYY")
    parser.add_argument("--rubro", required=True, help="Rubro a buscar")

    args = parser.parse_args()
    start_date: str = args.start_date
    end_date: str = args.end_date
    rubro: str = args.rubro

    segunda_seccion = SegundaSeccion(rubros=rubro, fecha_desde=start_date, fecha_hasta=end_date)
    links = segunda_seccion.get_result()
    print(f"Se han encontrado {len(links)} resultados\n")
    for link in links:
        print(link)

    n_links = len(links)
    if n_links > 0:
        
        output_folder = "output"
        
        # Parse dates from dd/mm/YYYY to YYYYmmdd
        start_date_parsed = datetime.strptime(start_date, "%d/%m/%Y").strftime("%Y%m%d")
        end_date_parsed = datetime.strptime(end_date, "%d/%m/%Y").strftime("%Y%m%d")
        output_file = f"links_{rubro}_{start_date_parsed}_{end_date_parsed}.json"

        data = {'fecha_desde':start_date,
                'fecha_hasta':end_date,
                'rubro':rubro,
                'links':links}
        
        os.makedirs(output_folder, exist_ok=True)
        path = os.path.join(output_folder, output_file)    
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()