from random import randint, choice, shuffle


ext = ('.mp3', '.wav', '.txt', '.tar', '.zip', '.exe', '.xml', '.json', '.sql', '.py', '.js')
table1 = []
table2 = []

for index in range(1, 700_001):
    delimeter = ','

    if index == 700_000:
        delimeter = ';'

    table1.append(f"('nazvanie{index}', {randint(1,10)}){delimeter}")


for index in range(1, 500_001):
    table2.append(f"('nazvanie{index}{choice(ext)}'),")

shuffle(table2)
table2[-1] = table2[-1].replace(',', ';')

with open('test.sql', 'w') as f:

    f.write('create table short_names (\n')
    f.write('name_ varchar(50),\n')
    f.write('status integer\n')
    f.write(');\n')
    f.write('create table full_names (\n')
    f.write('name_ varchar(50),\n')
    f.write('status integer\n')
    f.write(');\n')
    f.write('truncate short_names;\n')
    f.write('insert into short_names (name_, status)\n')
    f.write('values\n')

    for row in table1:
        f.write(row + '\n')

    f.write('\n\n')
    f.write('truncate full_names;\n')
    f.write('insert into full_names (name_)\n')
    f.write('values\n')

    for row in table2:
        f.write(row + '\n')
