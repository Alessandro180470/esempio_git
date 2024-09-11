"""
Realizzare un programma che analizzi tutti i valori ematici riscontrati durante le varie
analisi del sangue e osservare le evoluzioni dei valori riscontrati.Ricordiamo che il valore
della glicata rappresenta la media della glicemia valutata nel range di un periodo di durata 3 mesi
"""


class patologia_dt1:
    def __init__(self, glicata, mmol, ck, data):
        self.glicata = glicata
        self.mmol = mmol
        self.ck = ck
        self.data = data

        if self.ck >= 200:
            print(f'Attenzio:il valore del ck {self.ck} è alto ,analisi fatte in data :{self.data}')
        if self.glicata == 0:
            raise ValueError(f'Attenzione:valore glicata {self.glicata} non valido')
        if self.glicata > 6.7:
            print(f'Attenzione hai un valore di glicata {self.glicata} inizio PREDIABETE')

    def __str__(self):
          return f'La glicata è: {self.glicata} con {self.mmol} mmol e un ck: {self.ck} analisi eseguita in data {self.data}'


class calcolo_valore:

    def __init__(self):
        self.valore = []

    def append(self, value):
        self.valore.append(value)

    def media_ck(self):
        """
               Questo modulo ci consente di effettuare
               una media di tutti i valori analizzati
               della ck presa in esame
               :return: Il risultato della media del ck
               """
        if len(self.valore) == 0:
            raise ValueError('Attenzione non ci sono valori da valutare')
        risultato = [v.ck for v in self.valore]
        return sum(risultato) / len(risultato)

    def media_glicata(self):
        """
        Questo modulo ci consente di effettuare
        una media di tutti i valori analizzati
        della glicata presa in esame
        :return: Il risultato della media della glicata
        """
        if len(self.valore) == 0:
            raise ValueError('Attenzione non ci sono valori da valutare')
        risultato = [v.glicata for v in self.valore]
        return sum(risultato) / len(risultato)

    def val_min_glicata(self):
        risultato = [v.glicata for v in self.valore]
        return min(risultato)

    def val_max_glicata(self):
        """
        Questo modulo ricerca il valore massimo del ck
        :return: MAX CK
        """
        risultato = [v.glicata for v in self.valore]
        return max(risultato)

    def ck_uguali(self, ck):
        """
        Questo modulo ci consente di rilevare su di
        un'analisi ematica se ci sono valori di ck
        o inserendo opportuni valori di parametri ematici
        confrontarli e vedere si ci sono valori uguali in analisi
        effettuate in date diverse
        :param ck: o altri parametri da confrontare
        :return: il valore da confronare
        """
        rilevazioni = []
        for v in self.valore:
            if v.ck == ck:
                rilevazioni.append(v)

        return rilevazioni

    def find_data(self, data):
        """
        Questo modulo ci consente inserendo la
        data dell'analisi di trovare i valori
        da noi inseriti nell'append della classe
        di analisi_ematiche
        :param data: La data del'analisi
        :return: l'oggetto che appartiene a
        tale data
        """

        rilevazioni = []
        for v in self.valore:
            if v.data == data:
               rilevazioni.append(v)
               return rilevazioni
        raise ValueError(f'Data inserita non trovata ')

    def has_data(self, data):
        """
        Cerca la data dell'analisi se la data non c'è il
        dato non viene trovato
        :param data:la data dell'analisi
        :return: v se il dato è trovato
        altrimenti abbiamo un'eccezione dove non viene
        trovata la data
        """
        for v in self.valore:
            if v.data == data:
                return v
        raise ValueError(f'data non valida {data} ')

    def has_data1(self, data):
        for v in self.valore:
            if v.data == data:
                return v
        return None


if (__name__) == '__main__':
    print('Il nome del modulo di importazione è :', __name__, )
else:
    print('Il modulo importato è :', __name__)
