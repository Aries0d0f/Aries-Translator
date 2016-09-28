#!/usr/bin/env python
# coding=UTF-8
'''嵌入api'''
import sys
import json
'''載入api金鑰'''
from microsofttranslator import Translator
with open('config.json', 'r') as f: 
    account = json.load(f, encoding="utf-8")
translator = Translator(account["client_id"], account["password"])
'''輸出翻譯結果'''
def translate(text, lang):
    awnser = 'Translated: ' + translator.translate(text, lang)
    print(awnser)
'''增加command-line支援'''
if __name__ == "__main__":
    if sys.argv[1] == '-h' or len(sys.argv) < 2:
        print('Usage: translate <text> <language>')
        sys.exit()
    else:
        translate(sys.argv[1].decode('utf-8'), sys.argv[2])