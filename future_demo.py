# coding: utf-8
import concurrent.futures
import urllib.request


def get_page_size(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return url, len(conn.read())


TASKS = [
    (get_page_size, 'https://www.zhihu.com', 60),
    (get_page_size, 'https://www.baidu.com', 60),
    (get_page_size, 'http://cn.bing.com', 60),
    (get_page_size, 'http://www.kugou.com', 60)
]

rvs = {}
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(*task) for task in TASKS]
    for future in concurrent.futures.as_completed(futures):
        try:
            url, size = future.result()
            rv = {url: size}
            rvs.update(rv)
        except Exception as err:
            print("%r generated an exception: %s" % (url, err))
        else:
            print("%r page is %d bytes" % (url, size))


print(rvs)
