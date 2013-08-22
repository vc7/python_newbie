# 4.2 for Statements
#
# 2013.08.22

words = ['cat','bunny','dog']

for w in words:
    print w, len (w)

for w in words[:]:
    if len(w) > 4:
        words.insert(0, w)
words
