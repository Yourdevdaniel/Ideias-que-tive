while True:
    Kg = input("Quantos kg (kilogramas) você tem? ")
    
    numeros_validos = None
    kg_float = 0 
    
    # Codigo para analisar se os numeros são realmente numeros
    # Se souber algum jeito mais simples aceito dicas nos comentarios
    
    try:
        kg_float = float(Kg)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print("Numero Inválido")
        continue
    
    # Cálculo dos carbo e prot
    carboidratos_proteinas = kg_float*2
    
    print("Veja seu Resultado abaixo!")
    
    print(f"A quantidade de Carboidratos e Proteínas que você vai ingerir no seu dia é : {carboidratos_proteinas} gramas \n A gordura não precisa se preocupar, deixa no própio resquício da proteína. \n LEMBRE INCLUI CARBOIDRATO E PROTEINAS" )
    
    print("Fracione em 4 refeições. caso você não goste de comer comidas nas 4, \n você pode usar 2 refeições para fazer um sanduiche ou shake proteico ")

    # fração entre as refeições

    fracionado = carboidratos_proteinas / 4

    print("fracionando nas 4 alimentações ficaria: ")
    print(f"café: {fracionado} gramas ")
    print(f"almoço {fracionado} gramas ")
    print(f"lanche {fracionado} gramas")
    print(f"janta {fracionado} gramas")

    print("________________________________________________________________")


    print("Deve-se calcular tambem quantos litros de agua tem que beber")

    agua = kg_float * 35

    print(f"Voce tem que beber {agua} ml litros no seu dia")
    print("__________________________________________________________________________________")

    print(f"No final temos os seguintes resultados, \n voce deve ingerir essa quantidade de carboidratos e proteina por dia {carboidratos_proteinas} gramas e ficou {fracionado} gramas divido nas refeições \n Também tem que beber {agua} ml Litros por dia ")

    print("Tenha uma boa Dieta")


    print("_____________________________________________________________________")

    print("Esse calculo foi retirado do perfil @onutridasestrelas no TikTok lembre-se que sempre é bom consultar um profissional da saúde para resultados mais específicos \n e dieta mais específica")
    
    sair = input("Deseja sair do programa? [s]im: ").lower().startswith('s')
    
    if sair is True:
        break
