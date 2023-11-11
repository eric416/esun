import sqlite3
con=sqlite3.connect('bank.db')

cur=con.cursor()
cur.execute("SELECT * FROM Product;")
for row in cur.fetchall():
    print('Product No: '+str(row[0])+' Name: '+row[1]+' Price: '+str(row[2])+' Fee Rate: '+str(row[3]))

print("1. 新增喜好金融商品")
print("2. 查詢喜好金融商品清單")
print("3. 刪除喜好金融商品資訊")

ID="A123"
while(True):
    num=input("輸入服務代碼 (1, 2, 3)")

    if num=='1':
        pno=input("input Product No: ")
        count=input("input order count: ")
        Account=cur.execute("SELECT Account FROM User WHERE User_ID='A123';")
        Fee=cur.execute("SELECT Fee_Rate FROM Product WHERE No="+pno+";").fetchone()[0]
        Price=cur.execute("SELECT Price FROM Product WHERE No="+pno+";").fetchone()[0]
        TotalFee=0
        TotalAmount=TotalFee+Price*int(count)

        cur.execute("INSERT INTO Like_List VALUES("+pno+','+count+','+Account+','+TotalFee+','+TotalAmount+');')
        con.commit


