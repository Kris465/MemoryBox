
import csv

def find_delimiter(path):
    sniffer = csv.Sniffer()
    with open(path, 'r') as f:
        delimiter_in_file = sniffer.sniff(f.read(5000)).delimiter
        if delimiter_in_file == ' ':
            delimiter_in_file = '\t'
        return delimiter_in_file


def extract_parsing(extract, delimiter):
    with open(extract, 'r') as f:
        f_csv = csv.DictReader(f, delimiter=f'{delimiter}')
        result_list = []
        fields = alfa_bank_fields
        if delimiter == ';':
            fields = dot_bank_fields
        for row in f_csv:
            spam_list = []
            for field in fields:
                spam_list.append(row[field])
            result_list.append(spam_list)
        return result_list