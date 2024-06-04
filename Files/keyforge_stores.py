
# Quick script written to fix formating from file and convert to CSV
from country_list import countries_for_language

class keyforgeStores:
    def __init__(self):
        self.stores = []

    def setStoresFromFile(self):
        f = open('file/keyforge_stores.txt', 'r')
        lines = f.readlines()
        countries = countries_for_language('en')

        # Example: Name - State Country
        # Example 2: Name - Country
        for line in lines:
            line = line.strip()
            if ("-" in line):
                arr_line = line.split("- ")
                store_name = arr_line[0].rstrip()
                state = ""
                country = arr_line[1].rstrip()

                for country_lookup in countries:
                    # filter out countries that are also contained in states
                    if country_lookup[1] in country and country_lookup[1] not in ['Jersey', 'India', 'Georgia']:
                        state = country.replace(country_lookup[1], "").rstrip()
                        country = country_lookup[1]

                obj = {
                    "name": store_name,
                    "state": state,
                    "country": country
                }
                self.stores.append(obj)
        f.close()


    def getStores(self):
        return self.stores

    def saveStoresToFile(self):
        f = open('file/keyforge_stores_updated.csv', 'w+')
        for store in self.stores:
            f.write(f'{store["name"]},{store["state"]},{store["country"]}\n')
        f.close()

    def sortByCountry(self):
        self.stores.sort(key=lambda store: store["country"])


store = keyforgeStores()
store.setStoresFromFile()
store.sortByCountry()
print(store.getStores())
store.saveStoresToFile()





