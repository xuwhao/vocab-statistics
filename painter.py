import matplotlib.pyplot as plt


def line_chart(x, y, xlabel='', ylabel='', fname='', save=False,
               img_size=(8, 6), font_size=16, x_gap=1, y_gap=1, color=''):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.size'] = font_size  #
    plt.figure(figsize=img_size)
    xticks = list(range(0, len(x), x_gap))
    yticks = list(range(0, len(y), y_gap))
    plt.xticks(xticks)
    plt.yticks(yticks)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    titles = fname.split('-')
    plt.title(titles[-1])
    plt.plot(x, y, color)
    plt.show()

