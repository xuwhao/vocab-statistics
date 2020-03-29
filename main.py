from Vocabs import Vocabs
import dataCleaning as cleaner
import painter
import constants as const
import analysis

#cleaner.clean()

vocab_objs = analysis.get_all_vocabs()
#
# analysis.words_per_year(vocab_objs, 2001, 2020)
#
books = ['5495大纲词汇', '恋练有词', '非常词汇']
# analysis.book_hit_number(vocab_objs, books, 2001, 2020)

analysis.book_hit_number(vocab_objs, books, 2001, 2020)
analysis.book_hit_rate(vocab_objs, books, 2001, 2020)