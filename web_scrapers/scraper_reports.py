import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from zipfile import ZipFile
import os


import utils


def get_reports_titles(url):
    class_reports = "node-search-result"
    article_reports = _iterate_article_elments(url, class_reports)

    return article_reports


def _iterate_article_elments(url, el_class):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    elements_info = []

    article_elements = soup.find_all("article", class_=el_class)

    if article_elements != None:
        for index, article in enumerate(article_elements):
            element_info = utils.get_elment_info(index, article)
            elements_info.append(element_info)

    return elements_info


def get_files_info(url):
    ul_id = "resource-list"

    files_info = _iterate_ul_elements(url, ul_id)

    return files_info


def _iterate_ul_elements(url, ul_id):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    elements_info = []

    ul_elements = soup.find("ul", class_=ul_id)

    if ul_elements:
        for index, li_element in enumerate(ul_elements.find_all('li')):
            li_ul_info = _get_file_info(index, li_element)  # Getting file info
            if li_ul_info:
                elements_info.append(li_ul_info)

    return elements_info


def _get_file_info(index, element):
    # Getting file title of the content type
    name_a = element.find("a", class_="heading")
    if name_a:
        name = name_a['title']
        name = name.rstrip()

        # Getting url for download file
        url = element.find("a", class_="data-link")['href']

        el_info = {
            "number": index,  # Sum 1 to not start from 0
            "name": name,
            "url": url
        }
        return el_info


def download_report_file(url):
    file_name = _get_file_name_from_url(url)
    file_ext = _get_ext_from_file_name(file_name)

    # path to reports directory with file name
    reports_path_file = utils.create_path('reports/', file_name)

    # download file given specific url
    # and store it in reports folder
    urlretrieve(url, reports_path_file)

    downloaded_files_names = []

    if file_ext == "zip":
        # Maybe the zip contains multiple files
        unziped_file_names = _unzip_file(reports_path_file)
        downloaded_files_names = unziped_file_names
        utils.remove_file(reports_path_file)
    else:
        # if the file downloaded is not zip
        # add original name file
        downloaded_files_names.append(file_name)

    downloaded_files_names = utils.create_indexed_list(downloaded_files_names)

    return downloaded_files_names


def _get_file_name_from_url(url: str):
    name = url.split('/')[-1]
    return name


def _unzip_file(path_file):
    root_dir = os.path.abspath(os.curdir)  # Get project root path
    reports_path = os.path.join(root_dir, 'reports')

    with ZipFile(path_file, 'r') as zip_file:
        zip_file.extractall(reports_path)
        file_names = zip_file.namelist()
        return file_names


def _get_ext_from_file_name(file_name: str):
    ext = file_name.split('.')[-1]
    return ext


if __name__ == '__main__':
    pass
    url = "https://www.datosabiertos.gob.pe/sites/default/files/pcm_donaciones.zip"
    download_report_file(url)
