import os
files = os.listdir("D:\\100DaysofPython\\Day75\\files")
filepath = "D:\\100DaysofPython\\Day75\\files"
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
    os.rename(f"{filepath}/{file}", f"{filepath}/{i}.png")
    i = i + 1