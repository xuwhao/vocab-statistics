class Vocabs:
    """单词数据集实体类"""

    def __init__(self, name="", data=None, uri=None):
        self.name = name
        if data is not None:
            if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, dict) or isinstance(data, set):
                self.vocab_dict = dict(data)
                self.size = len(self.vocab_dict)
        else:
            self.vocab_dict = dict()
            self.size = 0
            if uri is not None:
                self.access(uri)

    def access(self, uri):
        f = open(uri, 'r')
        for line in f:
            key, value = line.split()
            self.vocab_dict[key] = int(value)
        self.size = len(self.vocab_dict)
        f.close()
