print("Artemis Rover Rock Scanner Starting")
basalt = 0
breccia = highland = regolith = 0
rockList = []
caminho = "D:/codigo-vsCode/programa-python/aprendendo/SpaceRockProject/rocks.txt"

# arquivo = open(caminho, 'w')
# arquivo.writelines(["Reading Rocks\n","basalt\n","breccia\n","highland\n","regolith\n","highland\n","breccia\n","highland\n","regolith\n","regolith\n","basalt\n","highland\n","basalt\n","breccia\n","breccia\n","regolith\n","breccia\n","highland\n","highland\n","breccia\n","basalt\n"])
# arquivo.close()
def countMoonRocks(rockToID):
    global basalt
    global breccia
    global highland
    global regolith

    rockToID = rockToID.lower()
    if("basalt" in rockToID):
        print("basalt encontrado\n")
        basalt += 1
    elif("breccia" in rockToID):
        print("Breccia encontrado!\n")
        breccia += 1
    elif("highland" in rockToID):
        print("highland encontrado!\n")
        highland += 1
    elif("regolith" in rockToID):
        print("Regolith encontrado!\n")
        regolith += 1
    return

arquivo = open(caminho)

linha = arquivo.readline()
print(linha)

rockList = arquivo.readlines()
for rock in rockList:
    countMoonRocks(rock)
arquivo.close()

print(f"total de basalt: {basalt} ")
print(f"total de breccia: {breccia} ")
print(f"total de highland: {highland} ")
print(f"total de regolith: {regolith} ")
print("The max number of one type of rock found was:", max(basalt, breccia, highland,regolith))
print("The minimum number of one type of rock found was:", min(basalt, breccia, highland, regolith))

