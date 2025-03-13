valor = float(input('Qual o valor do financiamento? R$'))
anos = int(input('Em quantos anos você pretende quitar o emprestimo?'))
sal = float(input('Qual a sua renda mensal?'))

meses = anos * 12 #conversão de anos em meses para descobrir o valor da parcela
parcela = meses / valor #valor mensal da parcela
por = 30/100 * sal
print('--------------------')
if parcela <= por:
        print('FINANCIAMENTO APROVADO')
        print('--------------------')
        print('Valor da solicitação: R${}'.format(valor))
        print('O emprestimo será pago em: {} anos totalizando {} meses'.format(anos,meses))
        print('Suas parcelas serão de R${:.2f}'.format(parcela))
        print('--------------------')
elif parcela > por:
        print('FINANCIAMENTO NEGADO')
        print('--------------------')
        print('Valor da solicitação: R${}'.format(valor))
