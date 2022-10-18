united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom[1]["capital"])
united_kingdom.append({"name": "Northern Ireland", "population": 1811000, "capital": "Belfast"})
print(united_kingdom[-1])
for country in united_kingdom:
    print(country["name"])

total_pop = 0

for country in united_kingdom:
    total_pop += country["population"]

print(f"There are {total_pop} many people in the uk.")
