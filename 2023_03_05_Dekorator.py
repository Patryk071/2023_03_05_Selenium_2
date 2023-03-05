import datetime

def cos_wiecej(przywitaj):
    def inner():
        print("Jak się masz?")
        przywitaj()
    return inner()


def dodaj_date(przywitaj2):
    def inner(imie):
        teraz = datetime.datetime.now()
        print("Dzisiaj mamy: ", teraz.strftime('%H:%M:%S'))
        return przywitaj2(imie)
    return inner

@cos_wiecej
def przywitaj1():
    print("Cześć!")

#gdybyśmy nie mieli dekoratora "@cos_wiecej", wówczas tak
#byśmy zdefiniowali tą funkcję
#cos_wiecej(przywitaj)

#a tak wystarczy to zapisać, jeśli mamy użyty dekorator "@cos_wiecej"
przywitaj1


#Przywitanie + dodanie daty + imienia
@dodaj_date
def przywitaj2(imie):
    print("Cześć! ", imie)

przywitaj2("Patryk")


#------------------------------------------------

class KontoBankowe:
    def __init__(self):
        self.__stan = 0

    @property
    def stan(self):
        return self.__stan

    @stan.setter
    def stan(self, o_ile):
        self.__stan = self.__stan + o_ile

    @stan.getter
    def stan(self):
        return self.__stan

    @stan.deleter
    def stan(self):
        return self.__stan


moje_konto = KontoBankowe()
moje_konto.stan = 50
print(moje_konto.stan)