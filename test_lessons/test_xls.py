import xlrd, os

current_path = os.path.join('resources/file_example_XLS_10.xls')


def test_xls():
    book = xlrd.open_workbook(current_path)

    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество колонок  {sheet.ncols}')
    print(f'Количество строк    {sheet.nrows}')
    print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=2)}')
    for rx in range(sheet.nrows):
        print(sheet.row(rx))
    assert book.nsheets == 1
    assert book.sheet_names() == ['Sheet1']
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert rx == 9