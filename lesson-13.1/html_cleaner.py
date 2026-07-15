import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<[^>]*>', '', html)
    lines = [line.strip() for line in cleaned_text.splitlines()]
    final_text = '\n'.join(lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)


if __name__ == "__main__":
    try:
        delete_html_tags('draft.html', 'cleaned.txt')
        print("OK")
    except FileNotFoundError:
        pass