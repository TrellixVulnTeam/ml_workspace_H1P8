import opennlptagger as tagger
import akcje
import pandas as pd
import narzedzia
import random



START_REGULY=pd.Series(['jeśli','gdy','jeżeli'])

KONIEC_REGULY=pd.Series(['wtedy','to'])

W_PRZECIWNYM_WYPADKU=pd.Series(['w przeciwnym wypadku'])

def utworz_reguly(aFrazyWarunkow:pd.Series):

    AKCJE=akcje.utworz_akcje()

    wynik_mnozenia=narzedzia.wylicz_iloczyn_kartezjanski([START_REGULY, aFrazyWarunkow, KONIEC_REGULY,AKCJE],['a','b','c','d'])
    # wypłaszczenie
    #wynik = pd.Series(tagger.taguj(wynik_mnozenia['a'],'regula_start')+' '+wynik_mnozenia['b']+' '+tagger.taguj(wynik_mnozenia['c'],'regula_stop')+' '+wynik_mnozenia['d']+' '+tagger.taguj('w przeciwnym wypadku', 'w_przeciwnym_wypadku')+' '+wynik_mnozenia['d']+' .')
    wynik = pd.Series(
        tagger.taguj(wynik_mnozenia['a'], 'regula_start') + ' ' + wynik_mnozenia['b'] + ' ' + tagger.taguj(
            wynik_mnozenia['c'], 'regula_stop') + ' ' + wynik_mnozenia['d'] +' .')

    print("Ilość rekordów w próbce=>"+str(len(wynik)))

    return wynik
'''
    print(len(wynik))

    w_przeciwnym_otagowane = pd.Series(tagger.taguj(W_PRZECIWNYM_WYPADKU, 'w_przeciwnym_wypadku'))
    w_przeciwnym_x_akcje=narzedzia.wylicz_iloczyn_kartezjanski([w_przeciwnym_otagowane,AKCJE],['a','b'])
    w_przeciwnym_x_akcje_wyplaszczone=pd.Series(w_przeciwnym_x_akcje['a']+w_przeciwnym_x_akcje['b'])

    wynik_kopia = pd.Series(tagger.taguj(wynik_mnozenia['a'], 'regula_start') + ' ' + wynik_mnozenia['b'] + ' ' + tagger.taguj(wynik_mnozenia['c'], 'regula_stop') + ' ' + wynik_mnozenia['d'])
    reguly_x_w_przeciwnym=narzedzia.wylicz_iloczyn_kartezjanski([wynik_kopia,w_przeciwnym_x_akcje_wyplaszczone],['a','b'])
    wynik_w_przeciwny_wyplaszczony=pd.Series(reguly_x_w_przeciwnym['a']+' '+reguly_x_w_przeciwnym['b']+' .')

    probka_wyplaszczona_w_przeciwnym_rand=wynik_w_przeciwny_wyplaszczony.sample(n=20000)
    wynik_rand=wynik.sample(n=90000)



    return wynik.sample(n=140000)#_rand.append(probka_wyplaszczona_w_przeciwnym_rand,ignore_index=True)
'''
