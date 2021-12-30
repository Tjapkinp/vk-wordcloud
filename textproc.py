def remove_empties_from_list(list):
    return [x for x in list if x != '']


def gen_unicode_character_list(index_start, index_stop):
    unicode_characters = [chr(x) for x in range(index_start, index_stop + 1)]
    return unicode_characters


def gen_white_character_set():
    en_abc = gen_unicode_character_list(65, 90)
    en_ABC = gen_unicode_character_list(97, 122)
    ru = gen_unicode_character_list(1040, 1103)
    return en_abc + en_ABC + ru


# Generates symbols list:
def gen_unicode_symbol_ban_list():
    return gen_unicode_character_list(33, 64) + gen_unicode_character_list(123, 126)


# Clean text from symbols:
def cleanse_text(inp_text):
    stopsymbols = gen_unicode_symbol_ban_list()
    n_stopsymbols = len(stopsymbols)
    for i in range(n_stopsymbols):
        inp_text = inp_text.replace(stopsymbols[i], '')
    return inp_text
