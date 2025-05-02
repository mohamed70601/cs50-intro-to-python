results = [
    "Mario",
    "Luigi",
    "Princess",
    "Yoshi",
    "Koopa Troopa",
    "Toad",
    "Bowser",
    "Donkey Kong Jr.",
]

# results.append("Princess")
# results.extend(["Bowser", "Donkey Kong Jr."])

results.remove("Bowser")
results.insert(6, "Bowser")
results.reverse()

for i in range(len(results)):
    print(results[i])
