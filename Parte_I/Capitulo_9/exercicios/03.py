import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],["Titanic", "The Revenant", "Inception"],["Training Day", "Man on Fire", "Flight"]]
with open("exe 03.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(movies[0])
    w.writerow(movies[1])