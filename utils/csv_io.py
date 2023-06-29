import csv


class CSV_IO:
    __init__(self, file_name):
        self._file_name = file_name
        self._file

    def open(self):
        with open(self._file_name, 'w', newline='') as file:
            self._file = file
    
    def close(self):
        pass

    def write_string(self, string):
        writer = csv.writer(file)
        writer.writerow([string])
            



    def read_string_by_row(self, row_number):
        pass







