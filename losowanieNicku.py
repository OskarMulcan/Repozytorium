kotely = '(ФДФ)'
print(kotely)

owcaUzytkownik = input('Podaj ile kotelow chcesz wygenerowac :) ')
try:
    owcaUzytkownik = int(owcaUzytkownik)
except ValueError as owcaError:
    owcaUzytkownik = 1
    print('Program potrzebuje liczby, a nie ciągu znaków!')

print ('(ФДФ)' * owcaUzytkownik)