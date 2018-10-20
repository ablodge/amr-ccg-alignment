import os

dir = 'js'

content = ''

for f in os.listdir(dir):
    if f.endswith(".js") and not f.endswith('main.js'):
        with open(os.path.join(dir,f),'r',encoding='utf8') as r:
            content += r.read()
with open('main.js','w',encoding='utf8') as w:
    w.write(content)