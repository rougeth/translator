translator
==========

CLI program that can bring the meaning of english words to portuguese. This is
accomplished by making http requests to google translator and returning the
results.

## installation

1. `$ cd /opt`
2. `$ sudo git clone https://github.com/rougeth/translator`
3. `$ sudo chmod a+x translator/run.py`
4. `$ sudo ln -s /opt/translator/run.py /usr/bin/translator`

## usage

```
$ translator unexpected
pt: inesperado

$ translator joke -d
pt: piada
en: joke

substantivo: gracejo, piada, brincadeira, graça, pilhéria
verbo: brincar, gracejar, dizer graças, rir-se de alguém
```

If you need help, type `$ translator -h`.
