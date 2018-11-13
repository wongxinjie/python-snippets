import re
import time
import threading
from atexit import register
from urllib.request import urlopen, Request


REGEX = re.compile(r'#([\d,]+) in Books')
AMAZON = 'http://www.amazon.com/dp/'
ISBNS = {
    "0132269937": "Core Python Programming",
    "0132356139": "Python Web Development with Django",
    "0137143419": "Python Fundamentals",
}


def get_ranking(isbn):
    url = '%s%s' % (AMAZON, isbn)
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/64.0.3282.119 Safari/537.36",
        }
    )
    with urlopen(request) as page:
        content = page.read().decode("utf-8")
    return REGEX.findall(content)[0]


def show_ranking(isbn):
    print("- %s ranked %s" % (ISBNS[isbn], get_ranking(isbn)))


def main():
    print('At %s on Amazon...' % time.ctime())
    for isbn in ISBNS:
        # show_ranking(isbn)
        threading.Thread(target=show_ranking, args=(isbn,)).start()


@register
def _atexit():
    print("All done at: %s" % time.ctime())


if __name__ == "__main__":
    main()
