#!/usr/bin/env python
# coding: utf-8

# In[40]:


import random

diets = [
    {'desayuno': 'jugo de naranja, huevo a la mexicana, 1 x tortilla, cafe con leche, media pieza de pan dulce',
    'comida': 'sandwich de ensalada de atún',
    'cena': 'cereal con fruta'},
    {'desayuno': 'jugo de mandarina, sincronizadas con jamón y queso, manzana',
    'comida': 'sopa de fideo, pechuga de pollo asada, 1 x tortilla, nieve de vainilla',
    'cena': 'cereal con fruta'},
    {'desayuno': '1 x hot cake, 1 x vaso de leche',
    'comida': 'arroz blanco al vapor, tinga de pollo, 1 x tortilla, 1 tazón de frijoles',
    'cena': 'cereal con fruta'},
    {'desayuno': 'jugo de naranja, chilaquiles con pollo, frijoles, café',
    'comida': 'sopa de letras, huachinango empapelado',
    'cena': 'cereal con fruta'},
    {'desayuno': '1 x café, 2 x quesadillas, fruta',
    'comida': 'fetuccini con vegetales, filete de res a la parrilla, 1 x tortilla, 1 tazón de frijoles',
    'cena': 'Fruta, arroz con leche, 1 pieza de pan dulce'},
    {'desayuno': 'licuado de platano, 2 piezas de pan tostado con crema de cacahuate y fresa',
    'comida': 'consomé de verduras, 1 x tostada de jaiba con frijoles, queso, y crema, 4 mitades de durazno en almibar',
    'cena': 'Fruta, té de manzanilla, una pieza de pan tostado con mantequilla'},
    {'desayuno': 'molletes',
    'comida': 'spaghetti rojo, milanesa de pollo, verduras al vapor, agua de fruta',
    'cena': '1 vaso de leche, 1 pieza de pan tostado con mantequilla'},
    {'desayuno': 'café con leche, 1 pieza de pan dulce, coctel de frutas',
    'comida': 'caldo de res, 1 tortilla, guisado de espinacas y verduras',
    'cena': 'sandwich de 2 rebanadas de jamón y 2 tiras de queso'},
    {'desayuno': 'plato de frijoles de olla, 2 quesadillas, fruta',
    'comida': 'crema de champiñones, pescado a la plancha, ensalada',
    'cena': 'chocolate con leche y pan dulce'},
    {'desayuno': 'jugo de naranja y sandwich de jamón',
    'comida': 'frijoles, bolillo, croquetas de atún, fruta',
    'cena': 'cereal con fruta'},
    {'desayuno': 'sandwich de huevo',
    'comida': 'pozole de pollo, aguacate, 1 x tortilla',
    'cena': 'cereal con fruta'},
    {'desayuno': 'jugo de naranja, huevo con salchicha y frijoles, 1 x tortilla',
    'comida': 'arroz blanco, bistec encebollado, nopales',
    'cena': 'cereal con fruta'},
    {'desayuno': 'cereal con fruta',
    'comida': 'sopa de verduras, pechucha cordon bleu: pechuga de pollo rellena de jamón y queso, 2 x tortillas, ensalada',
    'cena': '2 x enchiladas, 1 x tazón de frijoles, jugo de naranja'},
    {'desayuno': 'cereal con fruta',
    'comida': 'sopa de letras, brochetas de pollo con champiñones y verduras',
    'cena': 'fruta, 2 x sopes con pollo, frijoles, y queso fresco'},
    {'desayuno': 'licuado de plátano y pan dulce',
    'comida': 'sopa de papa y poro, filete de pescado con jitomate, 1 durazno en almibar',
    'cena': 'fruta, 2 x enfrijoladas'},
    {'desayuno': 'ceral con fruta',
    'comida': 'caldo tlalpeño, 4 mitas de durazno en almibar',
    'cena': 'agua de frutas, 1 x tamal verde, 1 tazón de frijoles'},
    {'desayuno': 'ceral con fruta',
    'comida': 'sopa de verduras, 3 tacos dorados de pollo, 1 tazón de frijoles',
    'cena': 'croissant de jamón y queso, agua de fruta'},
    {'desayuno': 'huevo con ejotes, 1 x tortilla',
    'comida': 'sopa de elote con setas, milanesa de ternera, papa al horno',
    'cena': 'tazón de frijoles, 1 pieza de pan de caja, manzana al horno'},
    {'desayuno': 'ceral con fruta',
    'comida': 'sopa de verduras, 3 tacos dorados de pollo, 1 tazón de frijoles',
    'cena': 'croissant de jamón y queso, agua de fruta'},
    {'desayuno': 'arroz con leche',
    'comida': 'arroz blanco, pollo pibil, 1 x tortilla',
    'cena': '3 x enfrijoladas'},
    {'desayuno': 'papa con chorizo',
    'comida': 'sopa de alubia, pechulla de pollo a la parrilla, 2 x tortillas',
    'cena': 'cereal con frutas'},
    {'desayuno': 'cereal con frutas',
    'comida': 'sopa de verduras, chile relleno de carne con queso',
    'cena': '2 x quesadillas'},
    {'desayuno': 'cereal con frutas',
    'comida': 'tallarines con tomate, cordero al cilantro, 1 x tortilla',
    'cena': 'esquites sin grasa, mayonesa, queso fresco, frijoles'}
    
]

special_diets = [
    {'desayuno': 'cereal',
    'comida': 'hamburguesa con queso',
    'cena': 'cereal'},
    {'desayuno': 'ceral con fruta',
    'comida': 'mac & cheese, atún tipo bacalao, 1 rebanada de pan blanco',
    'cena': '1 x hot dog'},
    {'desayuno': 'licuado de platano, pan tostado con mantequilla',
    'comida': '1 x rebanada de pizza de jamón, ensalada',
    'cena': 'cereal con frutas'},
    {'desayuno': 'tlacoyos de requesón y frijoles',
    'comida': 'Torta de Pierna tipo Alex',
    'cena': 'ensalada césar con pollo'},
    {'desayuno': 'licuado de plátano',
    'comida': 'Dip de philadelphia con tocino y jalapeños, babyback ribs al tajín, 1 x tortilla, cebolla asada',
    'cena': 'huevo con frijoles'},
    {'desayuno': 'leche con chocolate, pieza de pan dulce',
    'comida': 'Yakimeshi, rollo de sushi',
    'cena': 'omelette de queso y champiñones, 1 x tortilla de maíz'},
    {'desayuno': '1 x café, 2 x quesadillas, fruta',
    'comida': 'cebolla asada, papa asada, carne asada a la parrilla, 1/4 de salchicha para asar, 1 x tortilla, 1 tazón de frijoles',
    'cena': 'cereal con fruta'}
]

weekdays = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for day in weekdays:
    print("La dieta del " + day + " es:")
    
    if day == "Sábado":
        n = random.randint(0, (len(special_diets)-1))
        dieta = special_diets.pop(n)
    else:
        n = random.randint(0, (len(diets)-1))
        dieta = diets.pop(n)

    print('Desayuno: ' + dieta['desayuno'])
    print('Comida: ' + dieta['comida'])
    print('Cena: ' + dieta['cena'])
    print("")



# In[ ]:





# In[ ]:




