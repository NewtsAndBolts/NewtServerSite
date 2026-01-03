from math import ceil
from os import listdir
from os.path import isfile, join
modPath = "C:\\Users\\benai\\curseforge\\minecraft\\Instances\\All of Fabric 5 - AOF5 - 1.18.2\\mods"
onlyFiles = listdir(modPath)
columnSize = ceil(len(onlyFiles) / 3)
nextTable = 0
print(columnSize)

with open("modNamesHTML.txt", "w") as file:
    i = 0
    for fileName in onlyFiles:
        if (i == nextTable):
            nextTable += columnSize
            print("NEW TABLE")
            if (i != 0):
                file.write("    </ul>\n</div>\n")
            file.write("<div class=\"list-item col\">\n")
            file.write("    <ul class=\"list-unstyled\">\n")
        print()
        file.write("        <li><img class=\"sidebar-icon\" src=\"./css/icons/caret-right-fill.svg\"> " + fileName.replace("-", " ").replace("_", "").replace(".jar", "").replace("1.12.2", "").replace("  ", " ").title() + "</li>\n")
        i += 1
    file.write("    </ul>\n</div>\n")