from web_scrapers import scraper_reports
import utils
import data_manage


def set_reports_screen(url):
    msg = "Escriba el nombre del reporte que desea buscar. No es obligatorio colocar el nombre completo del reporte, ej: donaciones.\n"
    print(msg)
    query = input("Nombre del reporte: ")
    url = url + f'&query={query}'  # Appending query to the url

    print("Cargando reporte(s)...")
    reports = scraper_reports.get_reports_titles(url)

    print("Seleccione uno de los reportes encontrados basado en su busqueda")
    utils.general_screen(reports)
    print()

    option_number = int(input("Introduzca el numero: "))
    validation = utils.input_validation(option_number, reports)
    if validation:
        option = utils.search_option(option_number, reports)
        return option['url']
    print("Opcion Incorrecta")


def set_report_files_screen(url):
    print("Cargando archivos del reporte...\n")
    files = scraper_reports.get_files_info(url)

    print("Seleccione el archivo que quiere descargar")
    utils.general_screen(files)
    print()

    option_number = int(input("Introduzca el numero: "))
    validation = utils.input_validation(option_number, files)
    if validation:
        option = utils.search_option(option_number, files)
        return option['url']
    print("Opcion Incorrecta")


def set_downloaded_files_screen(url):
    print("Descargado Archivo(s)...\n")
    downloaded_files = scraper_reports.download_report_file(url)

    return downloaded_files


def set_filter_files_by_column_screen(file_name, column_name):
    print(f"Filtrando {file_name} por {column_name}...")
    data_manage.create_csvs_by_column_value(file_name, column_name)
    print("\nProceso Completado. Los archivos generados estan en la carpera reports.")


def set_select_file_for_filter_screen(downloaded_files):
    print()
    utils.general_screen(downloaded_files)
    print("\nSeleccione el archivo que quiere dividir por region")

    option_number = int(input("Introduzca el numero: "))
    validation = utils.input_validation(option_number, downloaded_files)
    if validation:
        option = utils.search_option(option_number, downloaded_files)
        return option['name']
    print("Opcion Incorrecta")



if __name__ == '__main__':
    pass
