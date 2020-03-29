from Vocabs import Vocabs
import dataCleaning as cleaner
import matplotlib.pyplot as plt
import painter


# # 只留下单词数据
# cleaner.clean_data(2001, 2020)
#
# # 词元化
# cleaner.word_element(2001, 2020)
#
# # 获取词元化后的单词列表
# cleaner.get_lemma(2001, 2020)
# list = sorted(vocabs.vocab_dict.items(), key=lambda d: d[1])

begin, end = 2001, 2020
vocab_list = list()
for i in range(begin, end+1):
    vocabs = Vocabs(str(i), uri=cleaner.accomplish_path + str(i) + ".txt", lemma=True)
    vocab_list.append(vocabs)

x, y = list(), list()

for vocabs in vocab_list:
    x.append(vocabs.name)
    y.append(vocabs.size)

painter.line_chart(x, y, "年份", "单词数", "历年真题单词数(不含简单词汇)", img_size=(12,6), x_gap=2, color='r')

