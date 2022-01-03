
# This function extract words from .html files

def html_text_extract(html_text):
    clean_text_array = str([])

    n_lines = len(html_text)
    tag_line = ['<div>', '</div>', 'class=', ',', '<div', '"kludges">', '\n']
    tag_line_space = ['<br>']
    n_tags = len(tag_line)
    n_tags_space = len(tag_line_space)
    for i in range(n_lines):
        # Search line with both <div> and </div>:
        if html_text[i].find(tag_line[0]) > 0 and html_text[i].find(tag_line[1]) > 0:
            text_buffer = html_text[i]
            for j in range(n_tags):
                text_buffer = text_buffer.replace(tag_line[j], '')
            for j in range(n_tags_space):
                text_buffer = text_buffer.replace(tag_line_space[j], ' ')
            clean_text_array = clean_text_array + text_buffer
    return clean_text_array
# if tag_line[0] and tag_line[1] in html_text[i]:


def html_audio_extract(html_text):
    band_name = []
    song_name = []
    duration = []
    tag_line = ["<div class=\"fl_l audio__title\">",
                " &mdash;",
                "</div><span class=\"fl_r audio__duration\">",
                "</span>"]
    tag_str_len = [len(x) for x in tag_line]

    n_lines = len(html_text)

    for i in range(n_lines):
        # Search line with div class=\"fl_l audio__title:
        ind_band_start = html_text[i].find(tag_line[0])
        if ind_band_start > 0:
            ind_band_stop = html_text[i].find(tag_line[1])
            ind_song_name_stop = html_text[i].find(tag_line[2])
            ind_duration_stop = html_text[i].find(tag_line[3])
            band_name.append(html_text[i][ind_band_start + tag_str_len[0]:ind_band_stop])
            song_name.append(html_text[i][ind_band_stop + tag_str_len[1]:ind_song_name_stop])
            duration.append(html_text[i][ind_song_name_stop + tag_str_len[2]:ind_duration_stop])

    return band_name, song_name, duration
# if tag_line[0] and tag_line[1] in html_text[i]: