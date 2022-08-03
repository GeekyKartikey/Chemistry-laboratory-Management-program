# ==============CHEMISTRY LABORATORY MANAGEMENT================
# =============================FUNCTIONS============================
# Function For Searching Contents
def SName(z, Z, ZZZ):
    AA = "select * from " + Z + " where " + ZZZ + "=" + "'" + z + "'"
    cursor.execute(AA)
    data = cursor.fetchall()
    for row in data:
        print("\n")
        print("SrNo     Name      Quantity ShelfNo")
        print(row)
        print("\n")
        return


# Function For Adding Content
def Add(L, M, N, O, Y):
    BB = "insert into " + Y + " values" + "(" + L + "," + "'" + M + "'" + "," + N + "," + O + ")"
    cursor.execute(BB)
    mycon.commit()
    return


# Function For Updating Contents
def Req(P, U, X, AAAA, PPPP):
    CC = "update " + X + " set " + AAAA + " = " + U + " where " + PPPP + " = " "'" + P + "'"
    cursor.execute(CC)
    mycon.commit()
    return


# Function For Showing Contents
def ShowTable(Var4):
    print("SrNo Name RollNo TableNo Dues")
    Var5 = "select * from " + Var4
    cursor.execute(Var5)
    data = cursor.fetchall()
    for row in data:
        print(row)
    return


# Function For Searching Contents
def SearchName(Var7, Var11, Var8):
    print("\n")
    print("SrNo Name RollNo TableNo Dues")
    Var9 = "select * from " + Var8 + " where " + Var11 + "=" + "'" + Var7 + "'"
    cursor.execute(Var9)
    data = cursor.fetchall()
    for row in data:
        print(row)
        print("\n")
        return


# Function For Adding Content
def ADNew(Var17, Var18, Var19, Var20, Var21, Var22):
    Var23 = "insert into " + Var22 + " values" + "(" + Var17 + "," + "'" + Var18 + "'" + "," + Var19 + "," + Var20 + "," + Var21 + ")"
    cursor.execute(Var23)
    mycon.commit()
    return


# Function For Updating Content
def UpdateDue(Var27, Var28, Var29, Var31, Var32):
    Var33 = "update " + Var29 + " set " + Var28 + " = " + Var31 + " where " + Var32 + " = " "'" + Var27 + "'"
    cursor.execute(Var33)
    mycon.commit()
    return


# Function For Updating Content
def UpdateTableNo(Var40, Var41, Var6, Var10, var100):
    Var34 = "update " + Var6 + " set " + Var100 + " = " + Var41 + " where " + Var10 + " = " "'" + Var40 + "'"
    cursor.execute(Var34)
    mycon.commit()
    return


# ========================MAIN PROGRAM============================
# _main_

# Connection Establishing
import mysql.connector as sqltor

mycon = sqltor.connect(host='localhost', database='ChemistryLaboratory', user='root', passwd='karateboy07')
if mycon.is_connected():
    print("successful")
if mycon.is_connected() == False:
    print("error")
cursor = mycon.cursor()

# Variables Used
A = "Welcome"
B = A.center(150)
print(B)
C = "To"
D = C.center(150)
print(D)
E = "Chemistry Laboratory Management"
F = E.center(150)
print(F)
I = "Chemicals"
J = "Salts"
K = "Apparatus"
III = "Chemical_Name"
JJJ = "Salt_Name"
KKK = "Apparatus_Name"
KKKK = "Quantity"
JJJJ = "Pieces"
LLLL = "Shelf_No"
Var6 = "students_11"
Var10 = "Name"
Var29 = "Dues"
Var50 = "students_12"
Var100 = "Table_No"

# loop used
while True:
    print("=======MAIN MENU========")
    print("1. Accesories management ")
    print("2. Data Mangenent")
    ch = int(input("Enter your choice(1-2):"))
    if ch == 1:
        print("\n")
        print("1. Chemicals")
        print("2. Salts")
        print("3. Apparatus")
        he = int(input("Enter your choice(1-3):"))
        if he == 1:
            print("\n")
            print("1. Search by name")
            print("2. Update database")
            fe = int(input("Enter your choice(1-2):"))
            if fe == 1:
                print("\n")
                a = input("Enter  name:")
                SName(a, I, III)
            elif fe == 2:
                print("\n")
                print("1. Add a chemical")
                print("2. Update Quantity")
                print("3. Update Shelf No")
                le = int(input("Enter your choice(1-3):"))
                if le == 1:
                    print("\n")
                    b = input("Enter S.No:")
                    c = input("Enter Chemical name:")
                    d = input("Enter Quantity:")
                    e = input("Enter shelf No:")
                    Add(b, c, d, e, I)
                elif le == 2:
                    print("\n")
                    f = input("Enter chemical name:")
                    g = input("Enter quantity in Ltrs:")
                    Req(f, g, I, KKKK, III)

                elif le == 3:
                    print("\n")
                    pp = input("Enter Chemical Name:")
                    qq = input("Enter Shelf No:")
                    Req(pp, qq, I, LLLL, III)
                else:
                    print("Invalid Entry!!!")

            else:
                print("Invalid Entry!!!")
        elif he == 2:
            print("\n")
            print("1. Search by name")
            print("2. Update database")
            ke = int(input("Enter your choice(1-2):"))
            if ke == 1:
                print("\n")
                h = input("Enter  name:")
                SName(h, J, JJJ)
            elif ke == 2:
                print("\n")
                print("1. Add a Salt")
                print("2. Update Quantity")
                print("3. Update Shelf No")
                te = int(input("Enter your choice(1-3):"))
                if te == 1:
                    print("\n")
                    i = input("Enter S.No:")
                    j = input("Enter Salt name:")
                    l = input("Enter Quantity:")
                    m = input("Enter shelf No :")
                    Add(i, j, l, m, J)
                elif te == 2:
                    print("\n")
                    n = input("Enter Salt Name:")
                    o = input("Enter Quantity:")
                    Req(n, o, J, KKKK, JJJ)
                elif te == 3:
                    print("\n")
                    pp = input("Enter Salt Name:")
                    qq = input("Enter Shelf No:")
                    Req(pp, qq, J, LLLL, JJJ)
                else:
                    print("Invalid Entry!!!")
            else:
                print("Invalid Entry!!!")

        elif he == 3:
            print("\n")
            print("1. Search by name")
            print("2. Update database")
            re = int(input("Enter your choice(1-2):"))
            if re == 1:
                print("\n")
                p = input("Enter  name:")
                SName(p, K, KKK)
            elif re == 2:
                print("\n")
                print("1. Add Apparatus")
                print("2. Update Pieces")
                print("3. Update Shelf No")
                we = int(input("Enter your choice(1-3):"))
                if we == 1:
                    print("\n")
                    q = input("Enter S.No:")
                    r = input("Enter Apparatus name:")
                    s = input("Enter Pieces:")
                    t = input("Enter shelf No :")
                    Add(q, r, s, t, K)
                elif we == 2:
                    print("\n")
                    u = input("Enter Apparatus Name:")
                    v = input("Enter Pieces:")
                    Req(u, v, K, JJJJ, KKK)
                elif we == 3:
                    print("\n")
                    pp = input("Enter Apparatus Name:")
                    qq = input("Enter Shelf No:")
                    Req(pp, qq, K, LLLL, KKK)
                else:
                    print("Invalid Entry!!!")
            else:
                print("Invalid Entry!!!")

        else:
            print("Invalid Entry!!!")
    elif ch == 2:
        print("\n")
        print("Choose Class:")
        print("1.) 11th")
        print("2.) 12th")
        Var1 = int(input("Enter your choice(1/2):"))
        if Var1 == 1:
            print("\n")
            print("Choose one option:")
            print("1) Show Table")
            print("2) Search by Name")
            print("3) Update Database")
            Var2 = int(input("Enter your choice(1/2/3):"))
            if Var2 == 1:
                print("\n")
                ShowTable(Var6)
            elif Var2 == 2:
                print("\n")
                Var3 = input("Enter Name:")
                SearchName(Var3, Var10, Var6)
            elif Var2 == 3:
                print("\n")
                print("Choose one option:")
                print("1) Add New Student")
                print("2) Update Dues")
                print("3) Update Table No")
                Var3 = int(input("Enter your choice(1/2/3):"))
                if Var3 == 1:
                    ShowTable(Var6)
                    print("\n")
                    Var12 = input("Enter S.No:")
                    Var13 = input("Enter Name:")
                    Var14 = input("Enter Roll No:")
                    Var15 = input("Enter Table No :")
                    Var16 = input("Enter Dues :")
                    ADNew(Var12, Var13, Var14, Var15, Var16, Var6)
                elif Var3 == 2:
                    print("\n")
                    Var24 = input("Enter Name:")
                    Var30 = input("Enter New Dues:")
                    UpdateDue(Var24, Var29, Var6, Var30, Var10)
                elif Var3 == 3:
                    print("\n")
                    Var40 = input("Enter Name:")
                    Var41 = input("Enter New Table No:")
                    UpdateTableNo(Var40, Var41, Var6, Var10, Var100)
                else:
                    print("\n")
                    print("Invalid Entry!!!")
            else:
                print("\n")
                print("Invalid Entry!!!")
        if Var1 == 2:
            print("\n")
            print("Choose one option:")
            print("1) Show Table")
            print("2) Search by Name")
            print("3) Update Database")
            Var2 = int(input("Enter your choice(1/2/3):"))
            if Var2 == 1:
                print("\n")
                ShowTable(Var50)
            elif Var2 == 2:
                print("\n")
                Var3 = input("Enter Name:")
                SearchName(Var3, Var10, Var50)
            elif Var2 == 3:
                print("\n")
                print("Choose one option:")
                print("1) Add New Student")
                print("2) Update Dues")
                print("3) Update Table No")
                Var3 = int(input("Enter your choice(1/2/3):"))
                if Var3 == 1:
                    ShowTable(Var50)
                    print("\n")
                    Var12 = input("Enter S.No:")
                    Var13 = input("Enter Name:")
                    Var14 = input("Enter Roll No:")
                    Var15 = input("Enter Table No :")
                    Var16 = input("Enter Dues :")
                    ADNew(Var12, Var13, Var14, Var15, Var16, Var50)
                elif Var3 == 2:
                    print("\n")
                    Var24 = input("Enter Name:")
                    Var30 = input("Enter New Dues:")
                    UpdateDue(Var24, Var29, Var50, Var30, Var10)
                elif Var3 == 3:
                    print("\n")
                    Var40 = input("Enter Name:")
                    Var41 = input("Enter New Table No:")
                    UpdateTableNo(Var40, Var41, Var50, Var10, Var100)
                else:
                    print("\n")
                    print("Invalid Entry!!!")
            else:
                print("\n")
                print("Invalid Entry!!!")
        else:
            print("\n")
            print("Invalid Entry!!!")
    else:
        print("Invalid Entry!!!")
    print("\n")
    V = input("Do you want to continue (Y/N):")
    if V == "Y":
        continue
    elif V == "N":
        print("THANK YOU")
        break
    else:
        print("\n")
        print("Invalid Entry!!....program ends...")
        break
# PROGRAM ENDS.....THANK YOU
