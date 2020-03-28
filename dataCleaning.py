import re
import pattern.text.en as en

path = "data/raw/"
clean_path = "data/cleaning/"
element_path = "data/element/"
accomplish_path = "data/accomplish/"

stem = ["[^A-Za-z]", "[{IV}{V}{VI}{VII}{VIII}]"]

simple_word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z',
               'have', 'and', 'the', 'of', 'to',
               'and', 'in', 'a', 'is', 'were', 'was',
               'you', 'I', 'he', 'his', 'there',
               'those', 'she', 'her', 'their',
               'that', 'them', 'or', 'for', 'as',
               'are', 'on', 'it', 'be', 'with', 'by', 'have', 'from', 'not', 'they',
               'more', 'but', 'an', 'at', 'we', 'has', 'can', 'this', 'your', 'which', 'will',
               'one', 'should', 'points', 'all', 'than', 'what',
               'people', 'if', 'been', 'its', 'new', 'our', 'would', 'part', 'may', 'some',
               'who', 'answer', 'when', 'most', 'so', 'section', 'no', 'into', 'do', 'only',
               'each', 'other', 'following', 'had', 'such', 'much', 'out', 'up', 'these',
               'even', 'how', 'directions:', 'use', 'because', 'time', 'thi', '']


def clean_all(content=""):
    for regex in stem:
        content = re.sub(regex, " ", content)
    return content


def clean_data(begin=2001, end=2001):
    for i in range(begin, end + 1):
        result = list()
        file = open(path + str(i) + ".txt", 'r', encoding='utf-8')
        fp = open(clean_path + str(i) + ".txt", 'w', encoding='utf-8')
        for line in file:
            result.append(clean_all(line))
        file.close()
        fp.writelines([line + '\n' for line in result])
        fp.close()


def word_element(begin=2001, end=2001):
    for i in range(begin, end + 1):
        result = list()
        file = open(clean_path + str(i) + ".txt", 'r', encoding='utf-8')
        fp = open(element_path + str(i) + ".txt", 'w', encoding='utf-8')
        for line in file:
            words = re.split(r'\s', line)
            for word in words:
                if word.strip() != '':
                    s = en.lemma(word)
                    if s not in simple_word:
                        result.append(word + " " + s)
        file.close()
        fp.writelines([line + '\n' for line in result])
        fp.close()


def get_lemma(begin=2001, end=2001):
    for i in range(begin, end + 1):
        result = list()
        file = open(element_path + str(i) + ".txt", 'r', encoding='utf-8')
        fp = open(accomplish_path + str(i) + ".txt", 'w', encoding='utf-8')
        for line in file:
            words = re.split(r'\s', line)
            print(words)
            result.append(words[1])
        file.close()
        fp.writelines([line + '\n' for line in result])
        fp.close()
