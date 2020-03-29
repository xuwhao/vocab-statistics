import re
import pattern.text.en as en
import os
import constants as const

if not os.path.exists(const.clean_path):
    os.mkdir(const.clean_path)
if not os.path.exists(const.element_path):
    os.mkdir(const.element_path)
if not os.path.exists(const.accomplish_path):
    os.mkdir(const.accomplish_path)


def clean():
    file_urls = os.listdir(const.path)
    clean_data(file_urls)
    word_element(file_urls)
    get_lemma(file_urls)


def clean_data(file_urls=()):
    for url in file_urls:
        result = list()
        file = open(const.path + url, 'r', encoding='utf-8')
        fp = open(const.clean_path + url, 'w', encoding='utf-8')
        for line in file:
            result.append(clean_regex(line))
        file.close()
        fp.writelines([line + '\n' for line in result])
        fp.close()


def word_element(file_urls=()):
    for url in file_urls:
        result = list()
        file = open(const.clean_path + url, 'r', encoding='utf-8')
        fp = open(const.element_path + url, 'w', encoding='utf-8')
        for line in file:
            words = re.split(r'\s', line)
            for word in words:
                if word.strip() != '':
                    s = en.lemma(word)
                    if s not in const.simple_word:
                        result.append(word + " " + s)
        file.close()
        fp.writelines([line + '\n' for line in result])
        fp.close()


def get_lemma(file_urls=()):
    for url in file_urls:
        result = list()
        file = open(const.element_path + url, 'r', encoding='utf-8')
        fp = open(const.accomplish_path + url, 'w', encoding='utf-8')
        for line in file:
            words = re.split(r'\s', line)
            result.append(words[1])
        file.close()
        fp.writelines([line + '\n' for line in result])
        fp.close()


def clean_regex(content=""):
    for regex in const.stem:
        content = re.sub(regex, " ", content)
    return content
