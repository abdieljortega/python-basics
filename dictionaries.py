def run():
  myDictionary = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
  }

  # print(myDictionary['llave1'])
  # print(myDictionary['llave2'])
  # print(myDictionary['llave3'])

  populationCountries = {
    'argentina': 44938712,
    'brazil': 210147125,
    'colombia': 50372424
  }

  # print(populationCountries['argentina'])
  # print(populationCountries['brazil'])
  # print(populationCountries['colombia'])

  # for country in populationCountries.keys():
  #   print(country)

  # for country in populationCountries.values():
  # print(country)

  for country, population in populationCountries.items():
    print(country + ' tiene ' + str(population) + ' habitantes')

if __name__ == "__main__":
    run()