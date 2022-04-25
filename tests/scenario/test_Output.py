import csv
import json
import unittest
import os

from scenario.output import OutputScripts


class MyTestCase(unittest.TestCase):
    def test_write_files(self):
        data = [{'first_name': 'Name1', 'last_name': 'Sname1', 'sex': 'male', 'bdate': '1977-11-11', 'city': 'Tomsk',
                 'country': 'Russia'},
                {'first_name': 'Name2', 'last_name': 'Sname2', 'sex': 'male', 'bdate': '1977-11-12', 'city': 'Tomsk',
                 'country': 'Russia'},
                {'first_name': 'Name3', 'last_name': 'Sname3', 'sex': 'female', 'bdate': '1977-11-13', 'city': 'Tomsk',
                 'country': 'Russia'},
                {'first_name': 'Name4', 'last_name': 'Sname4', 'sex': 'female', 'bdate': '1977-11-14', 'city': 'Tomsk',
                 'country': 'Russia'}]
        out = OutputScripts()

        filename_csv = 'testfilename.csv'
        filename_tsv = 'testfilename.tsv'
        filename_json = 'testfilename.json'

        out.to_csv(data, filename_csv)
        out.to_tsv(data, filename_tsv)
        out.to_json(data, filename_json)

        with open(filename_csv) as file:
            reader = csv.DictReader(file)
            data_csv = [dict(x) for x in reader]
            self.assertEqual(data, data_csv)
        os.remove(filename_csv)

        with open(filename_tsv) as file:
            reader = csv.DictReader(file, dialect='excel-tab')
            data_tsv = [dict(x) for x in reader]
            self.assertEqual(data, data_tsv)
        os.remove(filename_tsv)

        with open(filename_json) as file:
            self.assertEqual(data, json.load(file))
        os.remove(filename_json)


if __name__ == '__main__':
    unittest.main()
