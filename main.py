from Vocabs import Vocabs
import dataCleaning as cleaner
import painter
import constants as const
import analysis

# cleaner.clean()
#
vocab_objs = analysis.get_all_vocabs()
#
# analysis.words_per_year(vocab_objs, 2001, 2020)
#
# books = ['5495大纲词汇', '恋练有词', '非常词汇']
#
# analysis.book_hit(vocab_objs, books, 2001, 2020)

# dif = vocab_objs['5495大纲词汇'].diff_section(vocab_objs['非常词汇'])
# vocab = Vocabs("大纲词汇_diff_supervocab", data=dif)
# vocab.save()
# print(len(vocab_objs['5495大纲词汇'].intersection(vocab_objs['非常词汇'])))

using_vocabs = analysis.vocabs_using_situation(vocab_objs, outlets_name='5495大纲词汇')
used = using_vocabs['used_vocabs']
never_used = using_vocabs['never_used_vocabs']
