# 《Aries Translator v3.0》
# By:
    Aries Cs
# Credits:
    Aries Cs (github.com/aries0d0f)
# Usage:
   
* This project is basic on python2.7, be sure that you have installed it.
* This project is basic on microsoft_translator api, got your own client-id and password from microsoft for free first before start.
   
* First you must to clone or download this repository.
  Open your terminal and type:
```
git clone https://github.com/Aries0d0f/Aries-Translator.git
```
* Second
edit 'config.json' and past your own id and password.
```json
{
    "client_id" : "your_client_id",
    "password" : "your_password"
}
```
* Third, type the following things in your terminal:
```sh
python ./main.py <input> <language>
```
# Install
* Copy 'main.py' and rename it as translate
```
cd /path/to/Aries-Translator
cp main.py translate
chmod 775 translate
chmod +x translate
```
* link it
```
ln -s /path/to/Aries-Translator /usr/local/bin/translate
```
* After finish all, open your terminal and type:
```
translate <input> <language>
```
# Language Chooses:
    
      Chinesse Tranditional (繁體中文)：zh-CHT
      Chinesse Simplified (简体中文)：zh-CHS
      Japan (日本語)：ja
      English：en
      Deutsch (German)：de
      Russian (русский)：ru
Get more chooses from [https://github.com/openlabs/Microsoft-Translator-Python-API](https://github.com/openlabs/Microsoft-Translator-Python-API)
# Support:
    microsofttranslator api by Microsoft
