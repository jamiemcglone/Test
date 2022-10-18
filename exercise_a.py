stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
stops.append("Edinburgh Waverley")
stops.insert(0, "Glasgow Queen St")
stops.insert(3, "Polmont")
print(f"Linlithgow is at index {stops.index('Linlithgow')} in the list.")
stops.remove("Livingston")
stops.remove(stops[2])
print(f"There are {len(stops)} stops in the list.")
stops.sort()
stops.reverse()
for stop in stops:
    print(stop)