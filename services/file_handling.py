import os

BOOK_PATH = r'book\book1.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    seps = ',.!:;?'
    cut_text = text[start:start+size]
    if start+size >= len(text):
        return cut_text, len(cut_text)

    if cut_text[-1] in seps and (len(text[start:]) >= start+size and text[start+size] not in seps):
        return cut_text, len(cut_text)

    while cut_text[-1] in seps and text[start+size] in seps:
        cut_text = cut_text[:-1]

    while cut_text[-1] not in seps:
        cut_text = cut_text[:-1]

    return cut_text, len(cut_text)

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as file:
        page_no, curr_pos = 1, 0
        all_book = file.read()
        while curr_pos < len(all_book)-1:
            content, length = _get_part_text(all_book, curr_pos, PAGE_SIZE)
            book[page_no] = content.lstrip()
            page_no += 1
            curr_pos += length


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))


