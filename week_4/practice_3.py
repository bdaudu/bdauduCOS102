print("Welcome to the COUPE DE ESCRIVA FOOTBALL PICKS \n")

captain = {"Madiba:":"Chubby Obiora - Okafor","Blue-Jays:": "Christopher Umeh", 
           "Cirok:" : "Alexander" , "TSG Walkers:" : "Ikechukwu"}

goalkeepers = {'Madiba':'Chubby Obiora - Okafor','Blue-Jays:': 'oladimeji Abaniwondea/Jeffrey Awagu', 
           'Cirok:' : 'Timileyin Pearse/Izuako Jeremy' , 'TSG Walkers:' : 'Ayomide Ojituku'}

for pick in captain:
    print(pick, captain[pick])

print("\n")

for pick in goalkeepers:
    print(pick, goalkeepers[pick])