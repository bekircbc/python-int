import csv

with open("students.csv", "w", newline="") as f:

# "a" for appending; "w" for new schreiben..
  writer = csv.writer(f, delimiter=";")
  
  writer.writerow(["Zeile2 : Spalte 1", "Spalte 2", "Spalte 3"])
  writer.writerow(["Spalte 1", "Spalte 2", "Spalte 3"])
  