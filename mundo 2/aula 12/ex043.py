altura = int(input('Sua altura em CM: '))/100
peso = float(input('Seu peso em KG: '))
imc = peso / pow(altura,2)
print('Seu IMC é de {:.2f}.'.format(imc), end=' ')
if imc < 18.5:
    print('Abaixo do peso.')
# elif (imc >= 18.5) and (imc < 25):
elif 25 > imc >= 18.5:
    print('Peso ideal, mantenha assim.')
# elif (imc >= 25) and (imc < 30):
elif 30 > imc >= 25:
    print('Sobrepeso, se cuide.')
# elif (imc >= 30) and (imc < 40):
elif 40 > imc >= 30:
    print('Obesidade, atenção.')
elif imc >= 40:
    print('Obesidade mórbida, procure ajuda.')
