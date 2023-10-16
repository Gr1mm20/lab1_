# Написать функцию, которая принимает путь к HTML и путь к CSS файлам и возвращает словарь,
# в котором ключами выступают теги, идентификаторы или классы в файле CSS, а значениями список списков,
# где первым элементом внутреннего списка будет наименование тега, которые попадают под стили,
# указанные в файле CSS, а вторым – номер строк, в которых они находятся.
# Например, {'#inline-text': [[‘h1’, 29], [‘p’, 50]]}.

from bs4 import BeautifulSoup
import cssutils

def css_styles(html_path, css_path):
    result = {}
    with open(css_path, 'r', encoding='utf-8') as css_file:
        css_content = css_file.read()
    css_parser = cssutils.CSSParser()
    css = css_parser.parseString(css_content)
    with open(html_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    for rule in css:
        if rule.type == rule.STYLE_RULE:
            selectors = rule.selectorText.split(',')
            for selector in selectors:
                selector = selector.strip().replace('.', '')
                elements = soup.select(selector)
                for element in elements:
                    tag_name = element.name
                    line_number = element.sourceline
                    if selector in result:
                        result[selector].append((tag_name, line_number))
                    else:
                        result[selector] = [(tag_name, line_number)]
    return result
result = css_styles('Site.HTML', 'styles.css')
print(result)
