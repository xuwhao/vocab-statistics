import pattern.text.en as en


class Vocabs:
    """单词数据集实体类"""

    save_url = "data/vocab_saving/"

    def __init__(self, name="", data=None, uri=None, lemma=False):
        self.name = name
        if data is not None:
            if isinstance(data, list) or isinstance(data, set):
                new_dict = dict()
                for i in data:
                    if new_dict.get(i):
                        new_dict[i] += 1
                    else:
                        new_dict[i] = 1
                self.vocab_dict = new_dict
                self.size = len(self.vocab_dict)
            if isinstance(data, dict):
                self.vocab_dict = data
                self.size = len(data)
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

    # 两个集合的交集
    def intersection(self, obj):
        return self.vocab_dict.keys() & obj.vocab_dict.keys()

    # 此实例相对于obj的差集
    def diff_section(self, obj):
        return self.vocab_dict.keys() - obj.vocab_dict.keys()

    # 并集
    def combine_section(self, obj):
        return self.vocab_dict.keys() | obj.vocab_dict.keys()

    # 保存文件
    def save(self):
        fp = open(Vocabs.save_url + self.name + '.txt', 'w', encoding='utf-8')
        result = list(self.vocab_dict.keys())
        fp.writelines([line + '\n' for line in result])
        fp.close()
