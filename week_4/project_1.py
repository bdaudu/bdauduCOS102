b_name = ['Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola','Kunle', 'George', 'Thomas','Wesley']
b_age = [19,16,18,17,20,19,16,18,17,19]
b_height = [5.7,5.9,5.8,6.1,5.9,5.5,61,5.4,5.8,5.7]
b_score = [74,87,75,68,66,78,87,98,54,60]

g_name = ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Liza', 'Madonna', 'Waje', 'Tola', 'Aisha','Latifa']
g_age = [17,16,17,18,16,18,17,20,19,17]
g_height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
g_score = [80,85,70,60,76,66,87,95,50,49]

print("\t\tBOYS")
print("|Name  |Age  |Height|Score|")
for table in range(10):
    print("|",b_name[table],"|",b_age[table],"|",b_height[table],"|",b_score[table],"|")

print("\n")

print("\t\tGIRLS")
print("|Name   |Age  |Height|Score|")
for table in range(10):
    print("|",g_name[table],"|",g_age[table],"|",g_height[table],"|",g_score[table],"|")

