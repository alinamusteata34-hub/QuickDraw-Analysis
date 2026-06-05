import matplotlib.pyplot as plt

# Sample Quick Draw category counts
drawing_counts = {
    "Cat": 123202,
    "Dog": 152159,
    "Car": 98331,
    "Cloud": 117587
}

categories = list(drawing_counts.keys())
counts = list(drawing_counts.values())

plt.figure(figsize=(8, 5))
plt.bar(categories, counts)

plt.title("Quick Draw Dataset Categories")
plt.xlabel("Category")
plt.ylabel("Number of Drawings")

plt.savefig("quickdraw_chart.png")
plt.show()

print("Chart saved as quickdraw_chart.png")