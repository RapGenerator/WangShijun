from pypinyin import lazy_pinyin, Style
import fool

yun = {
    'i': 'i',
    'u': 'u',
    'v': 'v',
    'a': 'a', 'ia': 'a', 'ua': 'a',
    'o': 'o', 'uo': 'o',
    'e': 'e', 'ie': 'e', 'ue': 'e', 've': 'e', 'er': 'e',
    'ai': 'ai', 'uai': 'ai',
    'ei': 'ei', 'uei': 'ei',
    'ao': 'ao', 'iao': 'ao',
    'ou': 'ou', 'iou': 'ou',
    'an': 'an', 'ian': 'an', 'uan': 'an', 'van': 'an',
    'en': 'en', 'uen': 'en', 'eng': 'en',
    'in': 'in', 'ing': 'in',
    'vn': 'vn',
    'ang': 'ang', 'iang': 'ang', 'uang': 'ang',
    'ong': 'ong', 'iong': 'ong'
}

def load_word_dict():
    with open('word_dict_c.json', 'r') as f:
        word_dict = f.dump()
    return word_dict

word_dict = load_word_dict()

def get_expand_words(test : str, num : int):
    test_list = fool.pos_cut(test)
    pp = set([p for _, p in fool.pos_cut(test)[0]])
    pinyin = [yun[tone] for tone in lazy_pinyin(test, style = Style.FINALS, strict=True, errors = 'ignore')]
    expand = {}
    front = 0
    while len(expand) + 1 < num and front < len(pinyin):
        yy = '_'.join(pinyin[front:][::-1])
        front += 1
        if yy in word_dict:
            for p in pp:
                if p in word_dict[yy]:
                    for w, c in word_dict[yy][p].items():
                        expand[w] = expand.get(w, 0) + c
            if len(expand) < num:
                for p in word_dict[yy]:
                    for w, c in word_dict[yy][p].items():
                        expand[w] = expand.get(w, 0) + c
        for w in expand:
            expand[w] *= num
        if test in expand:
            del expand[test]
    mid_c = sorted(list(expand.values()), reverse = True)[num]
    out = [w for w, c in expand.items() if c >= mid_c][:num]
    return out

get_expand_words('萌新', 10)