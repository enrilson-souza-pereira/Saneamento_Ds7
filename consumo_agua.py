tipo_de_imovel = int(input("Qual seu tipo de imóvel? Digite 1 para Casa, 2 para apartamento e 3 para comercial"))
consumo = int(input("Qual o seu consumo mensal em m3?"))

if tipo_de_imovel == 3:
    print("Tarifa comercial aplicada, consulte o plano corporativo")
elif tipo_de_imovel == 2 and consumo <10:
    print("Consumo econômico – excelente controle de água!")
elif (tipo_de_imovel == 2 or tipo_de_imovel ==1) and consumo <=10 or consumo <=25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    