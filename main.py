from Vocabs import Vocabs
import dataCleaning as cleaner
import painter
import constants as const
import analysis

# cleaner.clean()
# 获取data/accomplished文件夹下所有单词实例
vocab_objs = analysis.get_all_vocabs()

# # 历年真题单词数
# analysis.words_per_year(vocab_objs, 2001, 2020)
#
# books[]中的单词书命中历年真题的数量以及比例
# books = ['5495大纲词汇', '恋练有词', '非常词汇']
# analysis.book_hit(vocab_objs, books, 2001, 2020)
#
# # 非常词汇和大纲的差集
# dif = vocab_objs['5495大纲词汇'].diff_section(vocab_objs['非常词汇'])
# vocab = Vocabs("大纲词汇_diff_supervocab", data=dif)
# vocab.save()

# 真题和outlets_name单词书的交集和差集
outlets_name = '5495大纲词汇'
using_vocabs = analysis.vocabs_using_situation(vocab_objs, outlets_name=outlets_name)
used = using_vocabs['used_vocabs']
never_used = using_vocabs['never_used_vocabs']
data = [used.size / vocab_objs[outlets_name].size, never_used.size / vocab_objs[outlets_name].size]
label = ['出现过的大纲单词(' + str(used.size) + ')', "未出现过的大纲单词(" + str(never_used.size) + ')']
f_name = "真题分析-2001至2020年大纲词汇考察率(总词汇数：" + str(vocab_objs[outlets_name].size) + ")"
painter.pie_chart(data=data, label=label, f_name=f_name)
