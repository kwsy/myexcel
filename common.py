# coding=utf-8


def get_cn_string(lst):
    return repr(lst).decode('string-escape')


def get_cn_unicode(lst):
    return repr(lst).decode('unicode-escape')


def print_cn_string(lst):
    print repr(lst).decode('string-escape')


def print_cn_unicode(lst):
    print repr(lst).decode('unicode-escape')


if __name__ == '__main__':
    print repr([u'\u59d3\u540d']).decode('unicode-escape')