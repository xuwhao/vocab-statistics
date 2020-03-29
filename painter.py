import matplotlib.pyplot as plt

colors = ['r', '', 'b', "deeppink", "darkblue", "goldenrod"]
markers = ['o', '+', '*', 'x', ',', '.']
line_styles = [':', '--', '-', '-.']
img_path = "data/image/"


# 绘制折线图
def line_chart(data=[], x_label=[], y_label=[], f_name='', save=True, img_size=(8, 6), font_size=16, x_gap=1):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.size'] = font_size
    titles = f_name.split('-')
    plt.figure(figsize=img_size)
    x_ticks = list(range(0, len(data[0]['y']), x_gap))
    plt.grid(alpha=0.4, linestyle=':')
    plt.xticks(x_ticks)
    plt.title(titles[-1])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    miny, maxy = get_min(data), get_max(data)
    plt.ylim(miny*0.85, maxy*1.18)
    m_cnt, l_cnt, c_cnt, is_multi = 0, 0, 0, 0
    for dic in data:
        marker = markers[m_cnt]
        line_style = line_styles[l_cnt]
        color = colors[c_cnt]
        m_cnt = (m_cnt + 1) % len(markers)
        l_cnt = (l_cnt + 1) % len(line_styles)
        c_cnt = (c_cnt + 1) % len(colors)
        if dic.get('marker'):
            marker = dic['marker']
        if dic.get('line_style'):
            marker = dic['line_style']
        if dic.get('color'):
            marker = dic['color']
        label = ''
        if dic.get('label'):
            label = dic['label']
            is_multi = 1
        plt.plot(dic['x'], dic['y'], color, label=label, marker=marker, linestyle=line_style)
    if is_multi == 1:
        font = {'weight': 'normal', 'size': 10}
        plt.legend(loc=2, prop=font)
    if save:
        plt.savefig(img_path + f_name + '.png')
    plt.show()


def get_max(data=[]):
    max_of_y = 0
    for line in data:
        temp = max(line['y'])
        if temp > max_of_y:
            max_of_y = temp
    return max_of_y


def get_min(data=[]):
    min_of_y = 999999
    for line in data:
        temp = min(line['y'])
        if temp < min_of_y:
            min_of_y = temp
    return min_of_y
