print("Linguagens permitidas:")
print("EN-English")
print("PT-Portuguese")
response=input("Digite a opção: ")

if (response.upper()=="EN"):
    print('Hello World')
elif (response.upper()=="PT"):
    print('Olá mundo !!')
else:
    print('Linguagem não conhecida !')