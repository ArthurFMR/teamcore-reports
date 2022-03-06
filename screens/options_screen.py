from web_scrapers import scraper_options_lists
import utils


def set_content_types_screen():
    print("Cargando Tipos de Contenido...")
    content_types = scraper_options_lists.get_content_types_list()

    print("Seleccione tipo de contenido colocando el numero")
    utils.general_screen(content_types)
    print()

    option_number = int(input("Introduzca el numero: "))
    validation = utils.input_validation(option_number, content_types)
    if validation:
        option = utils.search_option(option_number, content_types)
        return option['url']
    print("Opcion Incorrecta")


def set_categories_screen(url):
    print("Cargando Categorias correspondiente a tipo de contenido seleccionado...")
    categories = scraper_options_lists.get_category_list(url)

    print("Seleccione categoria colocando el numero")
    utils.general_screen(categories)
    print()

    option_number = int(input("Introduzca el numero: "))
    validation = utils.input_validation(option_number, categories)
    if validation:
        option = utils.search_option(option_number, categories)
        return option['url']
    print("Opcion Incorrecta")


def set_formats_screen(url):
    print("Cargando formatos correspondiente a tipo de contenido y categoria...")
    formats = scraper_options_lists.get_file_formats_list(url)

    print("Seleccione el formato colocando el numero")
    utils.general_screen(formats)
    print()

    option_number = int(input("Introduzca el numero: "))
    validation = utils.input_validation(option_number, formats)
    if validation:
        option = utils.search_option(option_number, formats)
        return option['url']
    print("Opcion Incorrecta")


if __name__ == "__main__":
    pass
