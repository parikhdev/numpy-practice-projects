#  Wap to Store following Word-Meanings to the following dictionary
# table : "A piece of furniture", "List of facts and figures"
# Cat : "A small Animal"

Word_Meanings = {
    "table": ["A piece of furniture", "List of facts and figures"],
    "Cat": "A small Animal"
}
print(Word_Meanings.items())
print(Word_Meanings.keys())
print(Word_Meanings.values())
print(Word_Meanings["Cat"])
print(Word_Meanings.get("Cat"))
Word_Meanings.update({"Dog" : "A domesticated carnivorous mammal"})
print(Word_Meanings)