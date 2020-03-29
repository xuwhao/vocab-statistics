import pattern.text.en as en


class Vocabs:
    """单词数据集实体类"""

    def __init__(self, name="", data=None, uri=None, lemma=False):
        self.name = name
        if data is not None:
            if isinstance(data, list) or isinstance(data, tuple) \
                    or isinstance(data, dict) or isinstance(data, set):
                self.vocab_dict = dict(data)
                self.size = len(self.vocab_dict)
        else:
            self.vocab_dict = dict()
            self.size = 0
            if uri is not None:
                self.access(uri, lemma)

    def access(self, uri, lemma):
        f = open(uri, 'r')
        for line in f:
            line = line.strip()
            if line != '':
                if lemma is not False:
                    line = en.lemma(line)
                if self.vocab_dict.get(line):
                    self.vocab_dict[line] += 1
                else:
                    self.vocab_dict[line] = 1
        self.size = len(self.vocab_dict)
        f.close()
