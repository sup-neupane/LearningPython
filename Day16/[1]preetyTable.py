from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon",["Gengar","Gardevoir","Venusaur"])
table.add_column("Pokemon",["Ghost","Fairy","Grass"])

table.align = "l"


print(table)