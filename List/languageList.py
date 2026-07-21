# Q. find language which star with letter p
#languages = ['java','python','php']
#for i in languages:
#    if i.startswith('p'):
#        print(i)
languages = ['java','python','php']
print([language for language in languages if language.startswith('p')])