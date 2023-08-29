import pypdf, os

current_path = os.path.join('../resources/docs-pytest-org-en-latest.pdf')


def test_pdf():
    reader = pypdf.PdfReader(current_path)
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    print('Кол-во страниц: ', number_of_pages)
    print('Первая страница: ', first_page)
    print('Текст на 1ой странице:', text)
    assert number_of_pages == 412
    assert text == ('pytest Documentation\n'
                    'Release 0.1\n'
                    'holger krekel, trainer and consultant, https://merlinux.eu/\n'
                    'Jul 14, 2022')

    count = 0
    for image_file in first_page.images:
        with open(str(count) + image_file.name, 'wb') as fp:
            fp.write(image_file.data)
            count += 1
    assert count == 1