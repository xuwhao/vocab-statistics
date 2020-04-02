import constants as const
from Vocabs import Vocabs
import painter
import os


def get_all_vocabs():
    result = {}
    file_urls = os.listdir(const.accomplish_path)
    for url in file_urls:
        name = url.split('.')[0]
        vocabs = Vocabs(name, uri=const.accomplish_path + url, lemma=True)
        result[name] = vocabs
    return result


def get_by_year_from_all(vocabs_objs={}, begin=2001, end=2020):
    vocab_list = list()
    for i in range(begin, end + 1):
        vocabs = vocabs_objs[str(i)]
        vocab_list.append(vocabs)
    return vocab_list


def words_per_year(vocabs_objs={}, begin=2001, end=2020):
    vocab_list = get_by_year_from_all(vocabs_objs, begin, end)

    x, y = [], []
    for vocabs in vocab_list:
        x.append(vocabs.name)
        y.append(vocabs.size)

    data = [{'x': x, 'y': y}]
    painter.line_chart(data, "年份", "单词数", "历年真题单词数(不含简单词汇)", img_size=(12, 6), x_gap=1)


def book_hit(vocabs_objs={}, books=[], begin=2001, end=2020):
    vocabs_list = get_by_year_from_all(vocabs_objs, begin, end)  # 所有年份的真题单词
    data, data_rate = [], []  # 最终结果集

    # 每一本单词书和每一年真题做交集运算
    for book_name in books:  # 每一本单词书的名字

        book = vocabs_objs[book_name]  # 拿到这本单词书
        x, y, y_rate = [], [], []  # 每一本单词数的结果集(x, y, label)

        # 拿到每一年的命中数量
        for vocab_year in vocabs_list:  # 拿到每一年的真题单词
            inter = vocab_year.intersection(book)  # 当年真题单词和单词书做交集运算
            x.append(vocab_year.name)  # 哪一年
            y.append(len(inter))  # 这一年命中的数量
            y_rate.append(len(inter)/book.size)  # 命中/背诵

        # book.name书在x[i]年命中了y[i]个单词
        book_dict = {'x': x, 'y': y, 'label': book.name}
        rate_dict = {'x': x, 'y': y_rate, 'label': book.name}
        data.append(book_dict)
        data_rate.append(rate_dict)

    painter.line_chart(data, "年份", "命中单词数", "词汇书分析-各单词书命中真题单词数", img_size=(14, 6))
    painter.line_chart(data_rate, "年份", "命中单词数", "词汇书分析-背诵性价比", img_size=(14, 6))


def vocabs_using_situation(vocabs_objs={}, outlets_name='', begin=2001, end=2020):
    vocab_list = get_by_year_from_all(vocabs_objs)
    outlets = vocabs_objs[outlets_name]
    used_set_list = []
    used_result = set()
    for vocabs in vocab_list:
        used_vocabs = vocabs.intersection(outlets)
        used_set_list.append(used_vocabs)
    for used_set in used_set_list:
        used_result = used_result | used_set
    objs = dict()
    objs['used_vocabs'] = Vocabs('used_vocabs', data=used_result)
    objs['never_used_vocabs'] = Vocabs('never_used_vocabs', data=outlets.diff_section(objs['used_vocabs']))
    return objs
