import locale
from collections import defaultdict

from pyquery import PyQuery as pq


def parse(name):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    pages = get_pages()
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_pages():
    page = pq(url='http://bashorg.org/page/1', parser='html')
    hrefs = page('#page .navigation a')
    count = hrefs.length
    max_page = int(hrefs[count - 2].text)
    i = 0
    pages = []
    quotes = defaultdict(list)
    for page_num in range(max_page):
        i = i + 1
        page = pq(url='http://bashorg.org/page/' + str(page_num), parser='html')
        for q_num in range(max_page):
            q = page.find('.q').eq(q_num)
            if q and q.text:
                i = int(q.text().split(':')[0].split('|')[0].split('#')[1].strip())  # id
                dt = q.text().split('\n')[0].split('|')[1].strip()
                # d = datetime.strptime(dt, u'%d %b %Y')
                q = "".join(q.text().split('\n')[1:])
                l = len(q)
                i = i + 1
                quotes[i].append({
                    'i': i, # index
                    'd': dt, # date
                    'q': q, # quote
                    'l': l, # length
                    'v': 1 # allowed
                })
                # ['q'].append(q.text())

        # quotes = page.find('.q').eq
        # quotes.each(lambda q: print(quotes[q].text))
        print('-------------------------------')
        # for quote in quotes:
        #     if quote and hasattr(quote, 'text'):
        #         print(quote.text)
        #         print('-------------------------------')

        # time.sleep(1)
    print((quotes['q']))

    # connect to db

    # print(max_page.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse('--finish--')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
