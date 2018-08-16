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
def get_target_lyrics(yuns : list):
    target_lines = []
    ya_len = len(yuns)
    for line in lyrics:
        pinyin_list = lazy_pinyin(line, style = Style.FINALS, strict = True)
        if ya_len <= len(pinyin_list):
            is_rhyme = True
            for i in range(1, ya_len+1):
                if yun.get(pinyin_list[-i], '') !=  yun[yuns[-i]]:
                    is_rhyme = False
                    break
            if is_rhyme:
                target_lines.append(line)
    return target_lines