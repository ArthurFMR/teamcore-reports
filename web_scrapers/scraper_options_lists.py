"""
This is the script that is going to get the next options lists:
1-Content Type List
2-Category List depending of content type selected
3-file format  depeding of content type and category selected
"""
import requests
from bs4 import BeautifulSoup

import utils


def get_content_types_list(url):
    ul_id = "facetapi-facet-search-apidatasets-block-type"

    # Storing content types with theirs info(name, url)
    content_types_info = _iterate_ul_elements(url, ul_id, sep="(")

    return content_types_info


def get_category_list(url):
    ul_id = "facetapi-facet-search-apidatasets-block-field-topic"

    # Storing categories with theirs info(name, url)
    categories_info = _iterate_ul_elements(url, ul_id, sep="(")

    return categories_info


def get_file_formats_list(url):
    ul_id = "facetapi-facet-search-apidatasets-block-field-resourcesfield-format"

    # Storing file formats with theirs info(name, url)
    formats_info = _iterate_ul_elements(url, ul_id, sep="(")

    return formats_info


def _iterate_ul_elements(url, ul_id, sep=""):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    elements_info = []

    ul_elements = soup.find(id=ul_id)

    if ul_elements:

        for index, li_content_type in enumerate(ul_elements.find_all('li')):
            li_ul_info = utils.get_elment_info(index, li_content_type, sep)
            # Omitting elements that does not have name
            if li_ul_info['name'].isnumeric() != True and li_ul_info['name'] != '':
                elements_info.append(li_ul_info)

    return elements_info


if __name__ == "__main__":
    pass
