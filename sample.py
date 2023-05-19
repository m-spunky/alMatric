from almatric import alMatric 

am = alMatric()


while True:
    # Functions
    inp = int(input("\n 1.Define New Matrix \n 2.Display Exsisting Matrices \n 3.Add All Matrices \n 4.Sub All Matrices \n 5.Multiply 2 Matrices \n"))
    if inp == 1:
        am.putData()
    if inp == 2:
        am.dispData()
    if inp == 3:
        print("\nAddition : {}".format(am.matrixAdd()))
    if inp == 4:
        print("\nSubtraction : {}".format(am.matrixSub()))
    if inp == 5:
        print("\nMultiplication : {}".format(am.getData_mul()))