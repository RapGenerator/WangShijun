import re
from pypinyin import lazy_pinyin, Style
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

yun_prob = {'ang': 2.81899644267293,
 'i': 1.8746812359990923,
 'a': 2.7619321420512524,
 'ou': 2.8233348442715283,
 'ong': 3.5930650655851006,
 'e': 2.402363610799362,
 'in': 3.8881211984895967,
 'en': 3.63729421842697,
 'ing': 3.2522291856761143,
 'u': 3.047424022133745,
 'eng': 4.01727621651432,
 'ei': 2.8622682641039154,
 'an': 2.059847244368534,
 'v': 3.9479922665796727,
 'ao': 2.7758958490686387,
 '': 3.968575174933067,
 'ai': 2.9318509321281643,
 'o': 2.883723199105175,
 'vn': 6.875119792074833}

def get_number(a : list, b : list):
    count = 0
    for i in range(1, 1 + min(len(a), len(b))):
        if a[-i] == b[-i]:
            count += 1
        else:
            break
    return count

def ranking(paragraph : list):

    test_paragraph = [re.sub(' ', '', line) for line in paragraph]
    pp = [lazy_pinyin(line, style=Style.FINALS, strict = True) for line in test_paragraph]
    pp = [[yun.get(k, '') for k in line] for line in pp]
    
    pairs = [get_number(pp[0], pp[1]),
        get_number(pp[0], pp[2]),
        get_number(pp[0], pp[3]),
        get_number(pp[1], pp[2]),
        get_number(pp[1], pp[3]),
        get_number(pp[2], pp[3])]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    sort_index = sorted(range(6), key = lambda k : pairs[k], reverse=True)
    
    if not any(pairs): #ABCD
        pass
    elif len(set(pairs)) == 1: #AAAA
        score1 = 4
        score2 = pairs[0]
        for y in pp[0][-score2:]:
            score3 += yun_prob[y]
    elif sort_index[0] == 0 and sort_index[1] == 5 or sort_index[0] == 5 and sort_index[1] == 0: #AABB
        score1 = 3
        score2 = (pairs[0] + pairs[5]) / 2
        for y in pp[0][-pairs[0]:]:
            score3 += yun_prob[y]
        for y in pp[2][-pairs[5]:]:
            score3 += yun_prob[y]
        score3 /= 2
    elif sort_index[0] == 1 and sort_index[1] == 4 or sort_index[0] == 4 and sort_index[1] == 1: #ABAB
        score1 = 3
        score2 = (pairs[1] + pairs[4]) / 2
        for y in pp[0][-pairs[1]:]:
            score3 += yun_prob[y]
        for y in pp[1][-pairs[4]:]:
            score3 += yun_prob[y]
        score3 /= 2
    elif sort_index[0] == 2 and sort_index[1] == 3 or sort_index[0] == 3 and sort_index[1] == 2: #ABBA
        score1 = 3
        score2 = (pairs[2] + pairs[3]) / 2
        for y in pp[0][-pairs[2]:]:
            score3 += yun_prob[y]
        for y in pp[1][-pairs[3]:]:
            score3 += yun_prob[y]
        score3 /= 2
    elif max(pairs) == pairs[0]: ##AABC
        score1 = 1
        score2 = pairs[0]
        for y in pp[0][-score2:]:
            score3 += yun_prob[y]
    elif max(pairs) == pairs[1]: ##ABAC
        score1 = 1
        score2 = pairs[1]
        for y in pp[0][-score2:]:
            score3 += yun_prob[y]
    elif max(pairs) == pairs[2]: ##ABCA
        score1 = 1
        score2 = pairs[2]
        for y in pp[0][-score2:]:
            score3 += yun_prob[y]
    elif max(pairs) == pairs[3]: ##BAAC
        score1 = 1
        score2 = pairs[3]
        for y in pp[1][-score2:]:
            score3 += yun_prob[y]
    elif max(pairs) == pairs[4]: ##BACA
        score1 = 2
        score2 = pairs[4]
        for y in pp[1][-score2:]:
            score3 += yun_prob[y]
    elif max(pairs) == pairs[5]: ##BCAA
        score1 = 1
        score2 = pairs[5]
        for y in pp[2][-score2:]:
            score3 += yun_prob[y]
    
    score2 = score2 * score2
    score = score1 * score2 *score3
    
    return score
