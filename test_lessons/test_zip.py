import zipfile, os

pdf_file_path = os.path.join('resources/docs-pytest-org-en-latest.pdf')
xls_file_path = os.path.join('resources/file_example_XLS_10.xls')
xlsx_file_path = os.path.join('resources/file_example_XLSX_50.xlsx')
csv_file_path = os.path.join('resources/new_csv.csv')

zip_file_name = 'tmp.zip'

with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    zipf.write(pdf_file_path, 'docs-pytest-org-en-latest.pdf')
    zipf.write(xls_file_path, 'file_example_XLS_10.xls')
    zipf.write(xlsx_file_path, 'file_example_XLSX_50.xlsx')
    zipf.write(csv_file_path, 'new_csv.csv')


def test_zip():
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        assert zipf.namelist() == ['docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls',
                                   'file_example_XLSX_50.xlsx', 'new_csv.csv']

    os.remove(os.path.join('tmp.zip'))