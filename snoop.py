# Hammer and Sons
# Christoph Kletzer

hours = 8

# Street Snoop 🕵🏻‍♂️

if hours <= 2:
  cost_street = hours * 100.00 + 200
elif hours <= 6:
  cost_street = hours * 80.00 + 200
elif hours <= 10:
  cost_street = hours * 60.00 + 200
else:
  cost_street = hours * 55 + 200

print("Street Snoop $", cost_street)
      
# Street Snoop Premimum 🕵🏻‍♂️💨

cost_street_premium = 1250.00

print("Street Snoop Premium $", cost_street_premium)

# Digital Deep Snoop 🕵🏻‍♂️🖥

if hours <= 2:
  cost_digital = hours * 300.00
elif hours <= 6:
  cost_digital = hours * 240.00
elif hours <= 10:
  cost_digital = hours * 180.00
else:
  cost_digital = hours * 165.00

print("Digital Deep Snoop: $", cost_digital)
