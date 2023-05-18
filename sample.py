from almatric import alMatric as am

while True:
    # Functions
    inp = int(input("\n 1.Define New Matrix \n 2.Display Exsisting Matrices \n 3.Add All Matrices \n 4.Sub All Matrices \n"))
    if inp == 1:
        am.putData()
    if inp == 2:
        am.dispData()
    if inp == 3:
        print("\nAddition : {}".format(am.matrixAdd()))
    if inp == 4:
        print("\nSubtraction : {}".format(am.matrixSub()))
