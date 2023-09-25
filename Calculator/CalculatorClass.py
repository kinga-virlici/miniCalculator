class Calculator:

    def __init__(self, valoare = 0):
        self.valoare = valoare # valoarea de start la pornirea calculatorului:0


        print(f'{self.valoare}')

    def adaugare(self, numar):
        self.valoare = self.valoare+ numar
        return f'{self.valoare}'

    def scadere(self, numar):
        self.valoare = self.valoare - numar
        return f'{self.valoare}'

    def inmultire(self, numar):
        self.valoare = self.valoare * numar
        return f'{self.valoare}'

    def impartire(self, numar):
        while numar != 0:
            self.valoare = self.valoare/numar
            return f'{self.valoare}'
        else:
            raise Exception('Invalid operation: Impartirea la 0 nu este permisa !')

    def afisare_rezultat(self):
        print(f'Rezultatul este {self.valoare}')

    def alegerea_operatorului(self):
        alegere = input('> Alegeti unul dintre aceste simboluri: (+, -, *, /) \n ')

        while alegere != 'x':
            if alegere == '+':
                numar = float(input('Introduceti numarul: '))
                self.adaugare(numar)  # apelam metoda de adaugare a numerelor
            elif alegere == '-':
                numar = float(input('Introduceti numarul: '))
                self.scadere(numar)  # apelam metoda de scadere a numerelor
            elif alegere == '*':
                numar = float(input('Introduceti numarul: '))
                self.inmultire(numar)  # apelam metoda de inmultire a numerelor
            elif alegere == '/':
                numar = float(input('Introduceti numarul: '))
                self.impartire(numar)  # apelam metoda de impartire a numerelor
            else:
                print('Operatie necunoscuta. Alegeti unul dintre aceste simboluri: +, -, *, /')
                break

            self.afisare_rezultat()

            alegere = input('> Alegeti unul dintre aceste simboluri: (+, -, *, /) \n')
        else:
            print('Iesire din calculator')









