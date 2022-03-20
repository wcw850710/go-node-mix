name = "frank:l8"

if "l8" in name:
  print("yes")

if name.index("l8"):
  print("yes2")

if name.count("l8") > 0:
  print("yes3")

if name.startswith("ff"):
  print("yes4")

print(name.upper())
print(name.lower())
print("frank l8".split())
print(",".join(["frank", "l8"]))