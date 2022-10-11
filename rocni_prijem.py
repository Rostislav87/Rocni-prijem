# Program, který vypočte roční příjem a průměrnou měsíční příjem.

year = {"january": 0, "february": 0, "march": 0, "april": 0, "may": 0,
        "june": 0, "july": 0, "august": 0, "september": 0, "october": 0,
         "november": 0, "december": 0}

# Mzda za každý měsíc
print("Zadej výplatu za každý měsíc.")
year["january"] = input("Leden: ")
year["february"] = input("Únor: ")
year["march"] = input("Březen: ")
year["april"] = input("Duben: ")
year["may"] = input("Květen: ")
year["june"] = input("Červen: ")
year["july"] = input("Červenec: ")
year["august"] = input("Srpen: ")
year["september"] = input("Září: ")
year["october"] = input("Říjen ")       
year["november"] = input("Listopad: ")
year["december"] = input("Prosinec: ")

# Součet všech mezd = roční příjem
summary = 0
for months in year.values():
        summary += int(months)

print("Tvůj roční příjem je:", summary, "Kč.")

# Výpočet průměrné měsíční mzdy
average = summary / len(year)

print("Tvoje průměrná měsíční mzda je:", round(average, 2), "Kč.")





