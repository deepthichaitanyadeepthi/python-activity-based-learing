# Smart Parking Fee Management

vehicle = input("Enter vehicle type (bike/car): ").lower()
entry = int(input("Enter entry time (0-23): "))
exit = int(input("Enter exit time (0-23): "))

if vehicle not in ["bike", "car"] or entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid input")

else:
    if exit < entry:
        hours = (24 - entry) + exit
        overnight = True
    else:
        hours = exit - entry
        overnight = False

    if hours == 0:
        hours = 1

    if vehicle == "bike":
        rate = 10
    else:
        rate = 20

    fee = hours * rate

    # Daily parking limit
    if fee > 200:
        fee = 200

    # Overnight penalty
    if overnight:
        fee = fee + 50

    print("\n--- Parking Bill ---")
    print("Vehicle:", vehicle)
    print("Parking Hours:", hours)
    print("Overnight Parking:", overnight)
    print("Parking Fee: Rs.", fee)