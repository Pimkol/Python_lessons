def st_len(text):
    return len(text)

def word_count(text):
    words=text.split(' ')
    count=0
    for i in words:
        count+=1
    return count

def change_up_down (text):
    if text.islower():
        chan_tex=text.upper()
    else: 
        chan_tex=text.lower()
    return chan_tex