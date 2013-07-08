translator
==========

CLI program that can bring the meaning of english words to portuguese. This is
accomplished by making http requests to google transtlator and returning the
results.

## installation

1. `$ cd /opt`
2. `$ sudo git clone https://github.com/allisonmachado/translator`
3. `$ sudo chmod a+x translator/main.py`
4. `$ sudo ln -s /opt/translator/main.py /usr/bin/translate`

## usage

```
$ translate joke
substantivo :
"gracejo","piada","brincadeira","graça","pilhéria","dito de espírito"

verbo :
"brincar","gracejar","dizer graças","rir-se de alguém"


$ translate hello
interjeição :
"Olá!","Oi!"
```
