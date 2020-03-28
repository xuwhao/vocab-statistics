from Vocabs import Vocabs
import pattern.text.en as en
import dataCleaning as cleaner

# 只留下单词数据
cleaner.clean_data(2001, 2020)

# 词元化
cleaner.word_element(2001, 2020)

# 获取词元化后的单词列表
cleaner.get_lemma(2001, 2020)


vocabs = Vocabs("2001", uri=cleaner.accomplish_path+"2001.txt", lemma=True)

list = sorted(vocabs.vocab_dict.items(), key = lambda d:d[1])

print(list)
