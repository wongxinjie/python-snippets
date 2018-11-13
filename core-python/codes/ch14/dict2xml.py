from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString


BOOKS = {
    "0132269937": {
        "title": "Core Python Programming",
        "edition": 2,
        "year": 2006
    },
    "0132356139": {
        "title": "Python Web Development With Django",
        "authors": "Jeff Forcier:Paul BIssex:Wesly Chun",
        "year": 2009
    },
    "0137143419": {
        "title": "Python Fundamentals",
        "year": 2009
    }
}

books = Element("books")
for isbn, ctx in BOOKS.items():
    book = SubElement(books, "book")
    ctx.setdefault("authors", "Wesly Chun")
    ctx.setdefault("edition", 1)
    for k, v in ctx.items():
        SubElement(book, k).text = ", ".join(str(v).split(":"))


xml = tostring(books)
print("*** RAM XML ***")
print(xml)

print("*** Pretty XMl")
dom = parseString(xml)
print(dom.toprettyxml('    '))

print('*** FLAT STRUCTURES ***')
for elem in books.getiterator():
    print('%s - %s' % (elem.tag, elem.text))


for book in books.findall('.//title'):
    print(book.text)
