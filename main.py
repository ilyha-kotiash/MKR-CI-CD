import csv

def read_population_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                country, area, population = row[0], int(row[1]), int(row[2])
                data.append({"country": country, "area": area, "population": population})
    return data

def sort_by_area(data):
    return sorted(data, key=lambda x: x["area"], reverse=True)

def sort_by_population(data):
    return sorted(data, key=lambda x: x["population"], reverse=True)

if __name__ == "__main__":
    filename = "data/population.txt"
    countries = read_population_data(filename)

    print("Відсортовані за площею:")
    for country in sort_by_area(countries):
        print(country)

    print("\nВідсортовані за населенням:")
    for country in sort_by_population(countries):
        print(country)
