
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


