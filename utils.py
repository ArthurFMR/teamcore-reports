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
