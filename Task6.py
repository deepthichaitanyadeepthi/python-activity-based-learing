# Courier Charge Optimization

weight = float(input("Enter parcel weight in kg: "))
length = float(input("Enter length in cm: "))
breadth = float(input("Enter breadth in cm: "))
height = float(input("Enter height in cm: "))
zone = input("Enter distance zone (local/national): ").lower()
urgency = input("Enter delivery type (normal/express): ").lower()
restricted = input("Is parcel restricted? (yes/no): ").lower()

if (weight <= 0 or length <= 0 or breadth <= 0 or height <= 0
        or zone not in ["local", "national"]
        or urgency not in ["normal", "express"]
        or restricted not in ["yes", "no"]):
    print("Invalid input")

elif restricted == "yes":
    print("Parcel cannot be accepted")

elif weight > 20 or length + breadth + height > 150:
    print("Parcel exceeds allowed limits")

else:
    if zone == "local":
        charge = 50 + weight * 10
    else:
        charge = 100 + weight * 20

    if urgency == "express":
        charge = charge + 100

    print("\n--- Courier Details ---")
    print("Weight:", weight, "kg")
    print("Zone:", zone)
    print("Delivery:", urgency)
    print("Courier Charge: Rs.", charge)

    print("\nEligible service selected successfully")