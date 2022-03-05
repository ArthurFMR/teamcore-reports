import unittest
import os

import scraper_options_lists as options_lists
import scraper_reports as reports_list


class TestScraperContentTypes(unittest.TestCase):
    url = "https://www.datosabiertos.gob.pe"

    def test_list_len(self):

        result = options_lists.get_content_types_list(self.url)
        elements_number = len(result)

        actual_number_in_page = 5

        self.assertEqual(elements_number, actual_number_in_page)

    def test_data_structure(self):
        # Getting first element
        result = options_lists.get_content_types_list(self.url)[0]

        # Checking if the dict has all the corresponding keys
        self.assertIn('number', result)
        self.assertIn('name', result)
        self.assertIn('url', result)


class TestScraperCategories(unittest.TestCase):
    url = "https://www.datosabiertos.gob.pe/search/type/dataset"

    def test_list_len(self):
        result = options_lists.get_category_list(self.url)
        elements_number = len(result)

        actual_number_in_page = 13

        self.assertEqual(elements_number, actual_number_in_page)

    def test_data_structure(self):
        # Getting first element
        result = options_lists.get_category_list(self.url)[0]

        # Checking if the dict has all the corresponding keys
        self.assertIn('number', result)
        self.assertIn('name', result)
        self.assertIn('url', result)


class TestScraperFileFormats(unittest.TestCase):
    url = "https://www.datosabiertos.gob.pe/search/field_topic/econom%C3%ADa-y-finanzas-29/type/dataset?sort_by=changed"

    def test_list_len(self):
        result = options_lists.get_file_formats_list(self.url)
        elements_number = len(result)

        actual_number_in_page = 10

        self.assertEqual(elements_number, actual_number_in_page)

    def test_data_structure(self):
        # Getting first element
        result = options_lists.get_file_formats_list(self.url)[0]

        # Checking if the dict has all the corresponding keys
        self.assertIn('number', result)
        self.assertIn('name', result)
        self.assertIn('url', result)


class TestScraperReportsInfo(unittest.TestCase):
    url = "https://www.datosabiertos.gob.pe/search/field_resources%253Afield_format/csv-14/field_topic/econom%C3%ADa-y-finanzas-29/type/dataset?query=&sort_by=changed"

    def test_list_len(self):
        result = reports_list.get_reports_titles(self.url)
        elements_number = len(result)

        actual_number_in_page = 10

        self.assertEqual(elements_number, actual_number_in_page)

    def test_data_structure(self):
        # Getting first element
        result = reports_list.get_reports_titles(self.url)[0]

        # Checking if the dict has all the corresponding keys
        self.assertIn('number', result)
        self.assertIn('name', result)
        self.assertIn('url', result)
    
    def test_list_len_with_query(self):
        query = "donaciones"
        url_query = f"https://www.datosabiertos.gob.pe/search/field_resources%253Afield_format/csv-14/field_topic/econom%C3%ADa-y-finanzas-29/type/dataset?query={query}&sort_by=changed"
        
        result = reports_list.get_reports_titles(url_query)
        elements_number = len(result)

        actual_number_in_page = 1

        self.assertEqual(elements_number, actual_number_in_page)


class TestScraperReportFilesInfo(unittest.TestCase):
    url = "https://www.datosabiertos.gob.pe/dataset/donaciones-covid-19-ministerio-de-econom%C3%ADa-y-finanzas-mef"

    def test_list_len(self):
        result = reports_list.get_files_info(self.url)
        elements_number = len(result)

        actual_number_in_page = 3

        self.assertEqual(elements_number, actual_number_in_page)

    def test_data_structure(self):
        # Getting first element to test it
        result = reports_list.get_files_info(self.url)[0]

        # Checking if the dict has all the corresponding keys
        self.assertIn('number', result)
        self.assertIn('name', result)
        self.assertIn('url', result)
    
    def test_download_report_file(self):
        file_url = "https://www.datosabiertos.gob.pe/sites/default/files/pcm_donaciones.zip"

        reports_list.download_report_file(file_url)

        file_name = reports_list._get_file_name_from_url(file_url)

        root_dir = os.path.dirname(os.path.abspath(__file__))
        reports_path = os.path.join(root_dir, 'reports\\' + file_name)

        result = os.path.exists(reports_path)

        self.assertTrue(result)

        if result:
            os.remove(reports_path)
    

if __name__ == '__main__':
    unittest.main()