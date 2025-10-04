def car_infos(fabricante, modelo, **kwargs): # ** serve para pares chave=valor (dicionário de argumentos nomeados)
    """Cria um dicionário com informações sobre um carro."""
    car = {} # Dicionário vazio
    car['fabricante'] = fabricante
    car['modelo'] = modelo

    # Adiciona todas as outras informações passadas como kwargs
    for chave, valor in kwargs.items(): # .items() para acessar todos os pares chave–valor do dicionário
        car[chave] = valor # Adicione esse par ao dicionário car

    return car

my_car = car_infos('honda', 'civic', year=2018, color='silver')
print(my_car)