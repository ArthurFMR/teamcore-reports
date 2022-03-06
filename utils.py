import os

BASE_URL = "https://www.datosabiertos.gob.pe"


# Get name and page url from html elements
def get_elment_info(index, element, sep=""):
    # Getting text of the content type
    name = element.a.get_text()

    # for reusing this block of code it is
    # Specify if you wanna split the name for cleaning purpose
    if sep != "":
        name = name.split(sep)[0].rstrip()  # Cleaning the name
    name = name.rstrip()

    enpoint = element.a['href']  # Getting endpoint

    el_info = {
        "number": index,  # Sum 1 to not start from 0
        "name": name,
        "url": BASE_URL + enpoint
    }
    return el_info


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)


def create_path(folder_name, file_name=""):
    """
    If want to create folder path without file
    do not specify file_name argument" 
    """
    root_dir = os.path.abspath(os.curdir)  # Get project root
    if file_name != "":
        file_path = os.path.join(root_dir, folder_name + file_name)
    else:
        file_path = os.path.join(root_dir, folder_name)

    return file_path


def general_screen(options):
    print()
    for option in options:
        number = option['number']
        name = option['name']

        message = f"{number} - {name}"
        print(message)


def search_option(number: int, options: list):
    for option in options:
        if option['number'] == number:
            return option


def input_validation(input, options):
    if input >= 0 and input < len(options):
        return True
    return False


def create_indexed_list(elements: list):
    indexed_list = []
    for index, el in enumerate(elements):
        indexed_el = {'number': index, 'name': el}
        indexed_list.append(indexed_el)

    return indexed_list


def get_files_in_dir(folder_name):
    folder_path = create_path(folder_name)
    files = []

    for file in os.listdir(folder_path):
        if _check_is_file(folder_path, file):
            # Not adding files that start with '.'
            if _check_first_char_in_string('.', file) != True:
                files.append(file)
    return files


def _check_is_file(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        return True


def _check_first_char_in_string(char, string: str):
    if string[0] == char:
        return True
