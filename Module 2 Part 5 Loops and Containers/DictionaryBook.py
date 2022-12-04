# dictionarybook.py
# author: lucia
# date: 2.12. 2022
'''
city_population = {"New York City": 8_550_405, 
                   "Los Angeles": 3_971_883, 
                   "Toronto": 2_731_571, 
                   "Chicago": 2_720_546, 
                   "Houston": 2_296_224, 
                   "Montreal": 1_704_694, 
                   "Calgary": 1_239_220, 
                   "Vancouver": 631_486, 
                   "Boston": 667_137}

city_population["New York City"]
city_population["Toronto"]
city_population["Toronto"]
city_population["Halifax"] = 390096
city_population

city_population = {}
city_population
city_population['New York City'] = 8550405
city_population['Los Angeles'] = 3971883
city_population

food = {"bacon": "yes", "egg": "yes", "spam": "no" }
food
food = {"bacon" : "yes", "spam" : "yes", "egg" : "yes", "spam" : "no" }
food

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
de_tr = {"rot": "kırmızı", "grün": "yeşil", "blau": "mavi", "gelb": "jel"}
en_es = {"red" : "rojo", "green" : "verde", "blue" : "azul", "yellow":"amarillo"}

dictionaries = {"en_de" : en_de, "de_fr" : de_fr, "de_tr": de_tr, "en_es": en_es}
dictionaries
cn_de = {"红": "rot", "绿" : "grün", "蓝" : "blau", "黄" : "gelb"}
de_ro = {'rot': 'roșu', 'gelb': 'galben', 'blau': 'albastru', 'grün': 'verde'}
de_hex = {"rot" : "#FF0000", "grün" : "#00FF00", "blau" : "0000FF", "gelb":"FFFF00"}
en_pl = {"red" : "czerwony", "green" : "zielony", 
         "blue" : "niebieski", "yellow" : "żółty"}
de_it = {"rot": "rosso", "gelb": "giallo", "blau": "blu", "grün": "verde"}

dictionaries["cn_de"] = cn_de
dictionaries["de_ro"] = de_ro
dictionaries["de_hex"] = de_hex
dictionaries["en_pl"] = en_pl
dictionaries["de_it"] = de_it
dictionaries

dictionaries["en_de"]     # English to German dictionary
dictionaries["de_fr"]     # German to French
print(dictionaries["de_fr"]["blau"])    # equivalent to de_fr['blau']
de_fr['blau']
lang_pair = input("Which dictionary, e.g. 'de_fr', 'en_de': ")
word_to_be_translated = input("Which colour: ")

d = dictionaries[lang_pair]
if word_to_be_translated in d:
    print(word_to_be_translated + " --> " + d[word_to_be_translated])
dictionaries['de_fr'][dictionaries['en_de']['red']]
de_fr
for value in de_fr.values():
    print(value)
for key, value in de_fr.items():
    print(key, value)
fr_de = {}
fr_de['rouge'] = 'rot'
fr_de['vert'] = "grün"
fr_de = {}
for key, value in de_fr.items():
    fr_de[value] = key             # key and value are swapped

fr_de
de_cn = {}
for key, value in cn_de.items():
    de_cn[value] = key
de_cn
'''
'''
en_de = {"Austria":"Vienna", "Switzerland":"Bern", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capital = capitals.pop("Austria")
print(capital)

capital = capitals.pop("Switzerland", "Bern")
print(capital)
capital = capitals.pop("France", "Paris")
print(capital)
capital = capitals.pop("Germany", "München")
print(capital)
'''
'''
capitals = {"Springfield": "Illinois", 
            "Augusta": "Maine", 
            "Boston": "Massachusetts", 
            "Lansing": "Michigan", 
            "Albany": "New York", 
            "Olympia": "Washington", 
            "Toronto": "Ontario"}
(city, state) = capitals.popitem()
(city, state)
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
'''
'''
locations = {"Toronto": "Ontario", "Vancouver": "British Columbia"}
province = "Ottawa"

if province in locations: 
    print(locations[province])
else:
    print(province + " is not in locations")
'''
'''
proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
proj_language["proj1"]
proj_language.get("proj2")
proj_language.get("proj4")
print(proj_language.get("proj4")) 
# setting a default value:
proj_language.get("proj4", "Python")
'''
'''
words = {'house': 'Haus', 'cat': 'Katze'}
w = words.copy()
words["cat"]="chat"
print(w)
print(words)
'''
'''
trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }

trainings2 = trainings.copy()
'''
'''
trainings["course2"]["title"] = "Perl Training Course for Beginners"
print(trainings2)
'''
'''
trainings["course2"] = {"title": "Perl Seminar for Beginners",
                         "location": "Ulm",
                         "trainer": "James D. Morgan"}
print(trainings2["course2"])
'''
'''
knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
knowledge.update(knowledge2)
print(knowledge)
'''
'''
d = {"a":123, "b":34, "c":304, "d":99}
for key in d:
     print(key)
for key in d.keys():
     print(key) 
for value in d.values():
    print(value)
for key in d:
    print(d[key])
'''
'''
%%timeit  d = {"a":123, "b":34, "c":304, "d":99}
for key in d.keys():
    x = d[key]
%%timeit  d = {"a":123, "b":34, "c":304, "d":99}
for value in d.values():
    x = value
'''

