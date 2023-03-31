
# Author: Wu MinLang
import requests
def get_triples(name, filePath):
    obj = requests.get('http://api.conceptnet.io/c/en/' + name).json()
    triples = obj['edges']

    for triple in triples:
        if 'language' not in triple['start'] or 'language' not in triple['end']:
            continue
        if (triple['start']['language'] != 'en' and triple['start']['language'] != 'zh') or (triple['end']['language'] != 'en' and triple['end']['language'] != 'zh'):
            continue
        rela = triple['rel']['label']
        head = triple['start']['term'].split('/')[-1]
        tail = triple['end']['term'].split('/')[-1]
        line = head + '\t' + rela + '\t' + tail
        with open(filePath, "a", encoding='UTF-8') as f:
            f.write(line + '\n')