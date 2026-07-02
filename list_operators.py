justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)

justice_league.sort()
print("Sorted List:", justice_league)
print("Leader:", justice_league[0])