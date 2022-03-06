import options_screen
import reports_screen
import utils


def main():
    print("Selecciona el proceso que desea realizar: \n")
    print("0 - Proceso completo\n1 - Filtrar reporte por region\n2 - Descargar reporte\n")
    option = int(input("Digite el numero de la opcion: "))

    processes = [run_whole_process, run_just_filter_file, run_just_scrap]
    processes[option]()


def run_just_scrap():
    url = options_screen.set_content_types_screen()
    url = options_screen.set_categories_screen(url)
    url = options_screen.set_formats_screen(url)
    url = reports_screen.set_reports_screen(url)
    url = reports_screen.set_report_files_screen(url)
    downloaded_files = reports_screen.set_downloaded_files_screen(url)
    print("Estos son los archivos descargados: ")
    utils.general_screen(downloaded_files)


def run_just_filter_file():
    print("Loading reports...\n")
    files = utils.get_files_in_dir('reports')
    if len(files) > 0:
        files = utils.create_indexed_list(files)

        file_name = reports_screen.set_select_file_for_filter_screen(files)
        reports_screen.set_filter_files_by_column_screen(file_name, "REGION")
    else:
        print("No hay ningun reporte alojado en la carpeta reports")


def run_whole_process():
    answer = options_screen.set_content_types_screen()
    answer = options_screen.set_categories_screen(answer)
    answer = options_screen.set_formats_screen(answer)
    answer = reports_screen.set_reports_screen(answer)
    answer = reports_screen.set_report_files_screen(answer)
    downloaded_files = reports_screen.set_downloaded_files_screen(answer)

    print("Estos son los archivos descargados: ")
    utils.general_screen(downloaded_files)
    file_name = reports_screen.set_select_file_for_filter_screen(
        downloaded_files)
    reports_screen.set_filter_files_by_column_screen(file_name, "REGION")


if __name__ == '__main__':
    main()
