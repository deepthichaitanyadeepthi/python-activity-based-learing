# Hospital Ward Occupancy Monitoring

wards = ["General", "ICU", "Private"]
capacity = [50, 20, 30]

occupancy = []

for i in range(3):
    print("\nEnter bed occupancy for", wards[i], "ward")
    days = []
    for j in range(3):
        beds = int(input("Enter beds occupied on day " + str(j + 1) + ": "))
        days.append(beds)
    occupancy.append(days)

peak = 0
peak_ward = ""
peak_day = 0

for i in range(3):
    print("\nWard:", wards[i])

    for j in range(3):
        beds = occupancy[i][j]

        if beds < 0:
            print("Invalid occupancy")
            continue

        percentage = (beds / capacity[i]) * 100
        print("Day", j + 1, "- Utilization:", round(percentage, 2), "%")

        if beds > capacity[i]:
            print("Capacity violation!")

        if beds > peak:
            peak = beds
            peak_ward = wards[i]
            peak_day = j + 1

print("\nPeak Demand")
print("Ward:", peak_ward)
print("Day:", peak_day)
print("Occupied Beds:", peak)