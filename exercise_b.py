
users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

print(users["Jonathan"]["twitter"])
print(users["Erik"]["home_town"])
print(users["Erik"]["lottery_numbers"])
print(users["Avril"]["pets"][0]["species"])
print(min(users["Erik"]["lottery_numbers"]))
avril_lotto_even = []
for num in users["Avril"]["lottery_numbers"]:
    if num % 2 == 0:
        avril_lotto_even.append(num)
print(avril_lotto_even)
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])
users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})
print(users["Erik"]["pets"])
users.update({"Jamie": {"twitter": "jamiemcglone", "lottery_numbers": [1, 2, 3, 4, 5, 6], "home_town": "Bonnyrigg", "pets": [{"name": "Ellie", "species": "cat"}]}})
print(users["Jamie"])

