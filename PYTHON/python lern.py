print("""
    1.python เบื้องต้น
    2.การเขียนคอมเมนท์หรือการใส่หมายเหตุ
    3.ข้อมูลแต่ละประเภท
    4.ตัวแปร
    5.การรับค่าจากผู้ใช้
    6.การดำเนินการทางคณิตศาสตร์
    7.ตัวดำเนินการกำหนดค่า
    8.ตัวดำเนินการเปรียบเทียบ
    9.ตัวดำเนินการทางตรรกะ
    10.คำสั่งเงื่อนไข if, elif, else
    11.คำสั่งเงื่อนไข match-case
    12.คำสั่งวนซ้ำ
    13.เจาะลึก string
    14.list
    15.tuple
    16.set
    17.dictionary
    18.pattern matching
    19.ฟังก์ชัน
    20.ขอบเขตตัวแปร
    21.try...except
    22.module
    23.import
""")
lern=input("เลือกเนื้อหาที่คุณต้องการ:")
match lern :
    case "1" | "python เบื้องต้น" | "1.python เบื้องต้น" :
        print("""
        python เบื้องต้น
            การสร้างไฟล์ python คือใช้นามสกุล .py
            การแสดงผลข้อมูลใช้คำสั่ง print(ข้อความ)
            เราไม่สามารถนำ strมาคำนวนกีบint ได้เพราะตัวอักขระกับตัวเลขคำนวนด้วยกันไม่ได้ จะทำได้แค่ str,intเท่านั้น
        """)
    case "2" | "การเขียนคอมเมนท์หรือใส่หมายเหตุ" | "2.การเขียนคอมเมนท์หรือใส่หมายเหตุ":
        print("""
        การเขียนคอมเมนท์หรือใส่หมายเหตุ
              ใช้เครื่องหมาย #ต่อด้วยข้อความ
              พอรันก็จะไม่เห็นข้อความที่คอมเมนท์ไว้
              """)
    case "3" | "ข้อมูลแต่ละประเภท" | "3.ข้อมูลแต่ละประเภท":
        print("""
        ข้อมูลแต่ละประเภท
              จำนวนเต็ม(int หรือ integers)
              จำนวนทศนิยม(floats หรือ floating point)
              จำนวนเชิงซ้อน(coplex)
              จำนวนตรรกะศาสตร์(boolหรือboolean)เป็นข้อมูลที่มีค่าได้เพียง 2 ค่าคือ 1.True(จริง)2.False(เท็จ)
              ข้อมูลอักขระ(stringsหรือstr)ข้อความครอบด้วย"..." เช่น "ควยไรสัด"
              ข้อมูลแบบไม่ระบุค่า(์NoneType)มีค่าเดียวคือ None
              """)
    case "4" | "ตัวแปร" | "4.ตัวแปร" :
        print("""
        ตัวแปร
              ตัวแปรคือการตั้งชื่อให้กับข้อมูลต่างๆเพื่อให้ง่ายต่อการเรียกใช้
              การตั้งชื่อตัวแปรต้องไม่ขึ้นต้นด้วยตัวเลขและห้ามมีช่องว่าง
              ยกตัวอย่างเช่น a=10 b=20 c="งงไมสัด
              การเรียกใช้ตัวแปรก็แค่พิมพ์ชื่อตัวแปรนั้นๆเช่น print(a)
        การเช็คค่าตัวแปร
              ใช้คำสั่ง print(type(ชื่อตัวแปร))
              """)
    case "5" | "การรับค่าจากผู้ใช้" |"5.การรับค่าจากผู้ใช้" :
        print("""
        การรับค่าจากผู้ใช้
              ใช้คำสั่ง input
              ยกตัวอย่างเช่น name=input("ป้อนชื่อของคุณ:")
              """)
    case "6" | "การดำเนินการทางคณิตศาสตร์" | "6.การดำเนินการทางคณิตศาสตร์" :
        print("""
        การดำเนินการทางคณิตศาสตร์
              เครื่องหมายบวก(+)ใช้กับการบวกเลขและการต่อข้อความเข้าด้วยกัน
              เครื่องหมายลบ(-)ใช้กับการลบเลข
              เครื่องหมายคูณ(*)ใช้กับการคูณเลขและการทำซ้ำข้อความ
              เครื่องหมายคูณ(/)ใช้กับการหารเลข
              เครื่องหมายหารเอาเศษ(%)ใช้กับการหารเลขแล้วเอาเศษ
              เครื่องหมายยกกำลัง(**)ใช้กับการยกกำลังเลข
              เครื่องหมายหารปัดเศษ(//)ใช้กับการหารเลขแล้วปัดเศษทิ้ง(ไม่มีจุดทศนิยม)
              เครื่องหมายวงเล็บ()ใช้กับการจัดลำดับความสำคัญของการคำนวณ
              """)
    case "7" | "ตัวดำเนินการกำหนดค่า" | "7.ตัวดำเนินการกำหนดค่า" :
        print("""
        ตัวดำเนินการกำหนดค่า
              เครื่องหมายเท่ากับ(=)ใช้กับการกำหนดค่าตัวแปร
              เครื่องหมายบวกเท่ากับ(+=)ใช้กับการเพิ่มค่าตัวแปร
              เครื่องหมายลบเท่ากับ(-=)ใช้กับการลดค่าตัวแปร
              เครื่องหมายคูณเท่ากับ(*=)ใช้กับการคูณค่าตัวแปร
              เครื่องหมายหารเท่ากับ(/=)ใช้กับการหารค่าตัวแปร
              เครื่องหมายหารเอาเศษเท่ากับ(%=)ใช้กับการหารเอาเศษค่าตัวแปร
              เครื่องหมายยกกำลังเท่ากับ(**=)ใช้กับการยกกำลังค่าตัวแปร
              เครื่องหมายหารปัดเศษเท่ากับ(//=)ใช้กับหารปัดเศษค่าตัวแปร
              """)
    case "8" | "ตัวดำเนินการเปรียบเทียบ" | "8.ตัวดำเนินการเปรียบเทียบ":
        print("""
        ตัวดำเนินการเปรียบเทียบ
              ผลลัพธ์ของการเปรียบเทียบจะมีค่าเป็น true(จริง) หรือ false(เท็จ)
              เครื่องหมาย == ใช้เปรียบเทียบค่าของตัวแปรว่ามีค่าเท่ากันหรือไม่
              เครื่องหมาย != ใช้เปรียบเทียบค่าของตัวแปรว่ามีค่าไม่เท่ากับหรือไม่
              เครื่องหมาย > ใช้เปรียบเทียบค่าของตัวแปรว่ามีค่ามากกว่าหรือไม่
              เครื่องหมาย < ใช้เปรียบเทียบค่าของตัวแปรว่ามีค่าน้อยกว่าหรือไม่
              เครื่องหมาย >= ใช้เปรียบเทียบค่าของตัวแปรว่ามีค่ามากกว่าหรือเท่ากับหรือไม่
              เครื่องหมาย <= ใช้เปรียบเทียบค่าของตัวแปรว่ามีค่าน้อยกว่าหรือเท่ากับหรือไม่
              """)
    case "9" | "ตัวดำเนินการทางตรรกะ" | "9.ตัวดำเนินการทางตรรกะ":
        print("""
        ตัวดำเนินการทางตรรกะ
              ผลลัพธ์ของการดำเนินการทาตรรกศาสตร์จะมีค่าเป็น true หรือ false
              จะมีคำสั่งอยู่ 3 อย่างคือ
                1.and
                2.or
                3.not
              """)
        logic=input("เลือกดูตัวอย่างที่ต้องการ:")
        match input:
            case "1" | "and" | "1.and":
                print("""
                and
                    คำสั่ง and ใช้กับการเปรียบเทียบหลายๆค่าโดยจะต้องเป็นจริงทั้งหมดจึงจะได้ผลลัพธ์เป็น true
                    user=str(input("ใส่ชื่อ:"))
                    password=int(input("ใส่รหัส:"))
                    print(user=="admin" and password==1234)
                """)
                user=str(input("ใส่ชื่อ:"))
                password=int(input("ใส่รหัส:"))
                print(user=="admin" and password==1234)
            case "2" | "or" | "2.or":
                print("""
                or
                    คำสั่ง or ใช้กับการเปรียบเทียบหลายๆค่าโดยจะต้องเป็นจริงอย่างน้อย 1 ค่าจึงจะได้ผลลัพธ์เป็น true 
                    user=str(input("ใส่ชื่อ:"))
                    password=int(input("ใส่รหัส:"))
                    print(user=="admin" and password==1234) 
                """)
                user=str(input("ใส่ชื่อ:"))
                password=int(input("ใส่รหัส:"))
                print(user=="admin" and password==1234)
            case "3" | "not" | "3.not":
                print("""
                not
                    คำสั่ง not ใช้กับการเปลี่ยนค่าจาก true เป็น false หรือจาก false เป็น ture
                    user=str(input("ใส่ชื่อ:"))
                    print(not user=="admin")
                """)
                user=str(input("ใส่ชื่อ:"))
                print(not user=="admin")
    case "10" | "คำสั่งเงื่อนไข if, elif, else" | "10.คำสั่งเงื่อนไข if, elif, else":
        print("""
        if statement
              คือการสร้างเงื่อนไขในการใช้คำสั่ง if
              1.if
              2.if-else
              3.if-elif-else
              4.kw pass
              5.การนำคำสั่งเงื่อนไขมาใช้ร่วมกับตัวดำเนินการเปรียบเทียบ
              6.การนำคำสั่งเงื่อนไขมาใช้ร่วมกับตัวดำเนินการทางตรรกะศาสตร์
              7.nested if
              """)
        statement=input("เลือกดูตัวอย่างที่ต้องการ:")
        match statement:
            case "1" | "if" | "1.if":
                print("""
                score=int(input("ใส่ตัวเลข:"))
                if score>=50:
                    print("สอบผ่าน")
                      """)
                score=int(input("ใส่คะแนนขอลงคุณ:"))
                if score>=50:
                      print("สอบผ่าน")
            case "2" | "if-else" | "2.if-else":
                print("""
                score=int(input("ใส่ตัวเลข:"))
                if score>=50:
                    print("สอบผ่าน")
                else:
                    print("สอบไม่ผ่าน")
                      """)
                score=int(input("ใส่ตัวเลข:"))
                if score>=50:
                    print("สอบผ่าน")
                else:
                    print("สอบไม่ผ่าน")
            case "3" | "if-elif-else" | "3.if-elif-else":
                print("""
                score=int(input("ใส่ตัวเลข:"))
                if score>=50:
                    print("สอบผ่าน")
                elif score<1:
                    print("ยังไม่สอบ")
                else:
                    print("สอบไม่ผ่าน")
                      """)
                score=int(input("ใส่ตัวเลข:"))
                if score>=50:
                    print("สอบผ่าน")
                elif score<1:
                    print("ยังไม่สอบ")
                else:
                    print("สอบไม่ผ่าน")
            case "4" | "kw pass" | "4.kw pass":
                print("""
                pass
                      คือคำสั่งที่ทำให้โปรแกรมของคำสั่งเงื่อนไขรันได้แม้จะไม่มีผลลัพธ์ของเงื่อนไข
                      score=int(input("ใส่ตัวเลข:"))
                      if score>=50:
                        pass
                      """)
                score=int(input("ใส่ตัวเลข:"))
                if score>=50:
                    pass
            case "5" | "การนำคำสั่งเงื่อนไขมาใช้ร่วมกับตัวดำเนินการเปรียบเทียบ" | "5.การนำคำสั่งเงื่อนไขมาใช้ร่วมกับตัวดำเนินการเปรียบเทียบร์":
                print("""
                score=int(input("ใส่คะแนน:"))
                if score<=100:
                    print("เกรด A")
                elif score<=79:
                    print("เกรด B")
                elif score<=69:
                    print("เกรด C")
                elif score>1:
                    print("เกรด F")
                else:
                    print("เกรด N")
                      """)
                score=int(input("ใส่คะแนน:"))
                if score<=100:
                    print("เกรด A")
                elif score<=79:
                    print("เกรด B")
                elif score<=69:
                    print("เกรด C")
                elif score<50:
                    print("เกรด F")
                else:
                    print("เกรด N")
            case "6" | "การนำคำสั่งเงื่อนไขมาใช้ร่วมกับตัวดำเนินการทางตรรกะศาสตร์" | "6.การนำคำสั่งเงื่อนไขมาใช้ร่วมกับตัวดำเนินการทางตรรกะศาสตร์":
                print("""
                score=int(input("ใส่คะแนน:"))
                if score>=80 and score<=100:
                    print("เกรด A")
                elif score>=60 and score<=79:
                    print("เกรด B")
                elif score>=50 and score<=69:
                    print("เกรด C")
                elif score>0 and score<50:
                    print("เกรด F")
                else:
                    print("เกรด N")
                      """)
                score=int(input("ใส่คะแนน:"))
                if score>=80 and score<=100:
                    print("เกรด A")
                elif score>=60 and score<=79:
                    print("เกรด B")
                elif score>=50 and score<=69:
                    print("เกรด C")
                elif score>0 and score<50:
                    print("เกรด F")
                else:
                    print("เกรด N")
            case "7" | "nested if" | "7.nested if":
                print("""
                nested if คือการนำคำสั่งเงื่อนไขมาใช้ซ้อนกันภายในคำสั่งเงื่อนไขอีกทีหนึ่ง
                name=str(input("ป้อนชื่อของคุณ:"))
                password=int(input("ป้อนรหัสของคุณ:"))
                if name=="member" and password==1234:
                    print("เข้าสู่ระบบ")
                    survice=str(input("คุณต้องการใช้บริการอะไร:"))
                    if survice=="ดูหนัง":
                        print("เลือกภาพยนตร์ที่ต้องการดู")
                    else:
                        print("บริการยังไม่พร้อมใช้งาน")
                else:
                    print("ชื่อหรือรหัสของคุณไม่ถูกต้อง")
                      """)
                name=str(input("ป้อนชื่อของคุณ:"))
                password=int(input("ป้อนรหัสของคุณ:"))
                if name=="member" and password==1234:
                    print("เข้าสู่ระบบ")
                    survice=str(input("คุณต้องการใช้บริการอะไร:"))
                    if survice=="ดูหนัง":
                        print("เลือกภาพยนตร์ที่ต้องการดู")
                    else:
                        print("บริการยังไม่พร้อมใช้งาน")
                else:
                    print("ชื่อหรือรหัสของคุณไม่ถูกต้อง")
    case "11" | "คำสั่งเงื่อนไข match-case" | "11.คำสั่งเงื่อนไข match-case":
        print("""
        คำสั่งเงื่อนไข match-case
            match statement , case คือคำสั่งเงื่อนไขคล้ายกับ if แต่จะใช้กับการเปรียบเทียบค่าตัวแปรเพียงตัวเดียว
            survice=str(input("คุณต้องการใช้บริการอะไร:"))
            match survice:
                case "ดูหนัง":
                    print("เลือกภาพยนตร์ที่ต้องการดู")
                case "ฟังเพลง":
                    print("เลือกเพลงที่ต้องการฟัง")
              """)
        survice=str(input("คุณต้องการใช้บริการอะไร:"))
        match survice:
                case "ดูหนัง":
                    print("เลือกภาพยนตร์ที่ต้องการดู")
                case "ฟังเพลง":
                    print("เลือกเพลงที่ต้องการฟัง")
    case "12" | "คำสั่งวนซ้ำ" | "12.คำสั่งวนซ้ำ":
        print("""
        คำสั่งวนซ้ำ
            คำสั่งทำซ้ำมี 2 ประเภท คือ
            1.for loop
            2.while loop
            3.kw break
            4.kw continue
              """)
        loop=input("เลือกเนื้อหาที่ต้องการ:")
        match loop:
            case "1" | "for loop" | "1.for loop":
                print("""
                for loop คือคำสั่งทำซ้ำโดยกำหนดจำนวนครั้งที่แน่นอน
                for i in range(2):
                    print("รอบที่",i+1)
                      """)
                for i in range(2):
                    print("รอบที่",i+1)
            case "2" | "while loop" | "2.while loop":
                print("""
                while loop คือคำสั่งทำซ้ำโดยไม่กำหนดจำนวนครั้งที่แน่นอน
                    while counter<2:
                        counter+=1
                        print("รอบที่",counter)
                      """)
                while counter<2:
                    counter+=1
                    print("รอบที่",counter)
            case "3" | "kw break" | "3.kw break":
                print("""
                break คือคำสั่งที่ใช้หยุดการทำซ้ำทันทีเมื่อเจอคำสั่งนี้
                    for i in range(10):
                        if i==5:
                            break
                        print("รอบท่",i)
                      """)
                for i in range(10):
                        if i==5:
                            break
                        print("รอบท่",i)
            case "4" | "kw continue" | "4.kw continue":
                print("""
                continue คือคำสั่งที่ใช้ข้ามการทำซ้ำในรอบนั้นๆเมื่อเจอคำสั่งนี้แล้วไปทำซ้ำรอบถัดไป
                    for i in range(10):
                        if i==5:
                            continue
                        print("รอบท่",i)
                      """)
                for i in range(10):
                    if i==5:
                        continue
                    print("รอบท่",i)
    case "13" | "เจาะลึก string" | "13.เจาะลึก string":
        print("""
        เจาะลึก string
            string คือข้อมูลอักขระที่ครอบด้วย"..."หรือ'...'
            string สามารถใช้เครื่องหมาย + ในการต่อข้อความเข้าด้วยกันได้
            string สามารถใช้เครื่องหมาย * ในการทำซ้ำข้อความได้
            string สามารถใช้เครื่องหมาย [] ในการเข้าถึงตำแหน่งของข้อความได้โดยเริ่มจาก 0
            string สามารถใช้เครื่องหมาย [m:n] ในการเข้าถึงช่วงของข้อความได้โดยเริ่มจาก m ถึง n-1
            string สามารถใช้คำสั่ง str() ในการแปลงค่าตัวแปรเป็นข้อความได้
            string สามารถใช้คำสั่ง .lower() ในการแปลงข้อความให้เป็นตัวพิมพ์เล็กได้
            string สามารถใช้คำสั่ง .upper() ในการแปลงข้อความให้เป็นตัวพิมพ์ใหญ่ได้
            string สามารถใช้คำสั่ง .strip() ในการตัดช่องว่างหน้าหรือหลังข้อความได้
            string สามารถใช้คำสั่ง .replace("ข้อความเก่า","ข้อความใหม่") ในการแทนที่ข้อความได้
            string สามารถใช้คำสั่ง .split("ตัวคั่น") ในการแยกข้อความออกเป็น list ได้
            string สามารถใช้คำสั่ง .join(list) ในการรวม list เป็นข้อความได้
            string สามารถใช้คำสั่ง f"..." ในการแทรกค่าตัวแปรลงในข้อความได้
            string สามารถใช้คำสั่ง .format() ในการแทรกค่าตัวแปรลงในข้อความได้
            text="hello world"
            print(text)
            print(text*2)
            print(text[0])
            print(text[0:5])
            print(len(text))
            print(str(1234))
            print(text.lower())
            print(text.upper())
            print("   hello   ".strip())
            print(text.replace("world","python"))
            print(text.split(" "))
            print("-".join(text))
            name="john"
            age=20
            print(f"สวัสดีครับผมชื่อ{name} อายุ{age}ปี")
            print("สวัสดีครับผมชื่อ{} อายุ{}ปี".format(name,age))
        """)
        text="hello world"
        print('-text="hello world"')
        print(text)
        print("-print(text)")
        print(text*2)
        print("-print(text*2)")
        print(text[0])
        print("-print(text[0])")
        print(text[0:5])
        print("-print(text[0:5])")
        print(len(text))
        print("-print(len(text))")
        print(str(1234))
        print("-print(str(1234))")
        print(text.lower())
        print("-print(text.lower())")
        print(text.upper())
        print("-print(text.upper())")
        print("   hello   ".strip())
        print('-print("   hello   ".strip())')
        print(text.replace("world","python"))
        print('-print(text.replace("world","python"))')
        print(text.split(" "))
        print("-print(text.split(" "))")
        print("-".join(text))
        print('-print("-".join(text))')
        name="john"
        print('-name="john"')
        age=20
        print("-age=20")
        print(f"สวัสดีครับผมชื่อ{name} อายุ{age}ปี")
        print('-print(f"สวัสดีครับผมชื่อ{name} อายุ{age}ปี")')
        print("สวัสดีครับผมชื่อ{} อายุ{}ปี".format(name,age))
        print('-print("สวัสดีครับผมชื่อ{} อายุ{}ปี".format(name,age))')
    case "14" | "list" | "14.list":
        print("""
        list
            list คือข้อมูลที่เก็บข้อมูลหลายๆค่าไว้ในตัวแปรเดียวโดยใช้เครื่องหมาย [ ] ครอบข้อมูลและคั่นด้วย ,
            list สามารถใช้เครื่องหมาย + ในการต่อ list เข้าด้วยกันได้
            list สามารถใช้เครื่องหมาย * ในการทำซ้ำ list ได้
            list สามารถใช้เครื่องหมาย [] ในการเข้าถึงตำแหน่งของข้อมูลใน list ได้โดยเริ่มจาก 0
            list สามารถใช้เครื่องหมาย [m:n] ในการเข้าถึงช่วงของข้อมูลใน list ได้โดยเริ่มจาก m ถึง n-1
            list สามารถใช้คำสั่ง len() ในการนับจำนวนข้อมูลใน list ได้
            list สามารถใช้คำสั่ง list() ในการแปลงค่าตัวแปรเป็น list ได้
            list สามารถใช้คำสั่ง .append() ในการเพิ่มข้อมูลลงใน list ได้
            list สามารถใช้คำสั่ง .insert(ตำแหน่ง,ข้อมูล) ในการแทรกข้อมูลลงใน list ได้
            list สามารถใช้คำสั่ง .remove(ข้อมูล) ในการลบข้อมูลออกจาก list ได้
            list สามารถใช้คำสั่ง .pop(ตำแหน่ง) ในการลบข้อมูลออกจาก list โดยระบุตำแหน่งได้
            list สามารถใช้คำสั่ง .sort() ในการเรียงข้อมูลใน list ได้    #ตอนนี้ใช้ไม่เป็น
            list สามารถใช้คำสั่ง .reverse() ในการเรียงข้อมูลใน list แบบย้อนกลับได้
            list สามารถใช้คำสั่ง .index(ข้อมูล) ในการหาตำแหน่งของข้อมูลใน list ได้
            list สามารถใช้คำสั่ง .count(ข้อมูล) ในการนับจำนวนข้อมูลใน list ได้
            list สามารถใช้คำสั่ง .clear() ในการลบข้อมูลทั้งหมดใน list ได้
            list สามารถใช้คำสั่ง .copy() ในการคัดลอก list ได้
            mylist=[10,20,30,"hello","world"]
            print(mylist)
            print(mylist*2)
            print(mylist[0])
            print(mylist[0:3])
            print(len(mylist))
            print(list("12345"))
            mylist.append(40)
            print(mylist)
            mylist.insert(1,15)
            print(mylist)
            mylist.remove(20)
            print(mylist)
            mylist.pop(2)
            print(mylist)
            mylist2=mylist.copy()
            mylist.reverse()
            print(mylist)
            print(mylist.index(10))
            print(mylist.count(10))
            mylist2=mylist.copy()
            print(mylist2)
            mylist.clear()
            print(mylist)
              """)
        mylist=[10,20,30,"hello","world"]
        print('-mylist=[10,20,30,"hello","world"]')
        print(mylist)
        print('-print(mylist)')
        print(mylist*2)
        print('-print(mylist*2)')
        print(mylist[0])
        print('-print(mylist[0])')
        print(mylist[0:3])
        print('-print(mylist[0:3])')
        print(len(mylist))
        print('-print(len(mylist))')
        print(list("12345"))
        print('-print(list("12345"))')
        mylist.append(40)
        print('-mylist.append(40)')
        print(mylist)
        print('-print(myli')
        mylist.insert(1,15)
        print('-mylist.insert(1,15)')
        print(mylist)
        print('-print(mylist)')
        mylist.remove(20)
        print('-mylist.remove(20)')
        print(mylist)
        print('-print(mylist)')
        mylist.pop(2)
        print('-mylist.pop(2)')
        print(mylist)
        print('-print(mylist)')
        mylist2=mylist.copy()
        print('-mylist2=mylist.copy()')
        mylist.reverse()
        print('-mylist.reverse()')
        print(mylist)
        print('-print(mylist)')
        print(mylist.index(10))
        print('-print(mylist.index(10))')
        print(mylist.count(10))
        print('-print(mylist.count(10))')
        mylist2=mylist.copy()
        print('-mylist2=mylist.copy()')
        print(mylist2)
        print('-print(mylist2)')
        mylist.clear()
        print('-mylist.clear()')
        print(mylist)
        print('-print(mylist)')
    case "15" | "tuple" | "15.tuple":
        print("""
        tuple
            tuple คือข้อมูลที่เก็บข้อมูลหลายๆค่าไว้ในตัวแปรเดียวโดยใช้เครื่องหมาย ( ) ครอบข้อมูลและคั่นด้วย ,')
            tuple มีลักษณะคล้ายกับ list แต่ไม่สามารถแก้ไข เพิ่ม หรือลบข้อมูลได้')
            tuple สามารถใช้เครื่องหมาย + ในการต่อ tuple เข้าด้วยกันได้')
            tuple สามารถใช้เครื่องหมาย * ในการทำซ้ำ tuple ได้')
            tuple สามารถใช้เครื่องหมาย [] ในการเข้าถึงตำแหน่งของข้อมูลใน tuple ได้โดยเริ่มจาก 0')
            tuple สามารถใช้เครื่องหมาย [m:n] ในการเข้าถึงช่วงของข้อมูลใน tuple ได้โดยเริ่มจาก m ถึง n-1')
            tuple สามารถใช้คำสั่ง len() ในการนับจำนวนข้อมูลใน tuple ได้')
            tuple สามารถใช้คำสั่ง tuple() ในการแปลงค่าตัวแปรเป็น tuple ได้')
            tuple สามารถใช้คำสั่ง .index(ข้อมูล) ในการหาตำแหน่งของข้อมูลใน tuple ได้')
            tuple สามารถใช้คำสั่ง .count(ข้อมูล) ในการนับจำนวนข้อมูลใน tuple ได้')
            mytuple=(10,20,30,"hello","world")
            print(mytuple)
            print(mytuple*2)
            print(mytuple[0])
            print(mytuple[0:3])
            print(len(mytuple))
            print(tuple("12345"))
            print(mytuple.index(10))
            print(mytuple.count(10))
              """)
        mytuple=(10,20,30,"hello","world")
        print('-mytuple=(10,20,30,"hello","world")')
        print(mytuple)
        print('-print(mytuple)')
        print(mytuple*2)
        print('-print(mytuple*2)')
        print(mytuple[0])
        print('-print(mytuple[0])')
        print(mytuple[0:3])
        print('-print(mytuple[0:3])')
        print(len(mytuple))
        print('-print(len(mytuple))')
        print(tuple("12345"))
        print('-print(tuple("12345"))')
        print(mytuple.index(10))
        print('-print(mytuple.index(10))')
        print(mytuple.count(10))
        print('-print(mytuple.count(10))')
    case "16" | "set" | "16.set":
        print("""
        set
            set คือข้อมูลที่เก็บข้อมูลหลายๆค่าไว้ในตัวแปรเดียวโดยใช้เครื่องหมาย { } ครอบข้อมูลและคั่นด้วย ,
            set มีลักษณะคล้ายกับ list แต่ข้อมูลใน set จะไม่ซ้ำกันและไม่มีลำดับ
            set สามารถใช้เครื่องหมาย + ในการต่อ set เข้าด้วยกันได้
            set สามารถใช้เครื่องหมาย * ในการทำซ้ำ set ได้
            set ไม่สามารถใช้เครื่องหมาย [] ในการเข้าถึงตำแหน่งของข้อมูลใน set ได้เพราะไม่มีลำดับ
            set ไม่สามารถใช้เครื่องหมาย [m:n] ในการเข้าถึงช่วงของข้อมูลใน set ได้เพราะไม่มีลำดับ
            set สามารถใช้คำสั่ง len() ในการนับจำนวนข้อมูลใน set ได้
            set สามารถใช้คำสั่ง set() ในการแปลงค่าตัวแปรเป็น set ได้
            set สามารถใช้คำสั่ง .add(ข้อมูล) ในการเพิ่มข้อมูลลงใน set ได้
            set สามารถใช้คำสั่ง .remove(ข้อมูล) ในการลบข้อมูลออกจาก set ได้
            set สามารถใช้คำสั่ง .pop() ในการลบข้อมูลออกจาก set แบบสุ่มได้
            set สามารถใช้คำสั่ง .clear() ในการลบข้อมูลทั้งหมดใน set ได้
            set สามารถใช้คำสั่ง .copy() ในการคัดลอก set ได้
            set สามารถใช้คำสั่ง .union(set) ในการรวม set ได้
            set สามารถใช้คำสั่ง .intersection(set) ในการหาข้อมูลที่เหมือนกันใน set ได้
            set สามารถใช้คำสั่ง .difference(set) ในการหาข้อมูลที่ไม่เหมือนกันใน set ได้
            set สามารถใช้คำสั่ง .issubset(set) ในการตรวจสอบว่า set หนึ่งเป็นส่วนย่อยของอีก set หนึ่งหรือไม่
            set สามารถใช้คำสั่ง .issuperset(set) ในการตรวจสอบว่า set หนึ่งมีข้อมูลครอบคลุมอีก set หนึ่งหรือไม่
            myset={10,20,30,"hello","world",10}
            print(myset)
            print(len(myset))
            print(set("12345"))
            myset.add(40)
            print(myset)
            myset.remove(20)
            print(myset)
            myset.pop()
            print(myset)
            myset2=myset.copy()
            print(myset2)
            myset.clear()
            print(myset)
            setA={1,2,3,4}
            setB={3,4,5,6}
            print(setA.union(setB))
            print(setA.intersection(setB))
            print(setA.difference(setB))
            print(setA.issubset(setB))
            print(setA.issuperset(setB))
              """)
        myset={10,20,30,"hello","world",10}
        print('-myset={10,20,30,"hello","world",10}')
        print(myset)
        print('-print(myset)')
        print(len(myset))
        print('-print(len(myset))')
        print(set("12345"))
        print('-print(set("12345"))')
        myset.add(40)
        print('-myset.add(40)')
        print(myset)
        print('-print(myset)')
        myset.remove(20)
        print('-myset.remove(20)')
        print(myset)
        print('-print(myset)')
        myset.pop()
        print('-myset.pop()')
        print(myset)
        print('-print(myset)')
        myset2=myset.copy()
        print('-myset2=myset.copy()')
        print(myset2)
        print('-print(myset2)')
        myset.clear()
        print('-myset.clear()')
        print(myset)
        print('-print(myset)')
        setA={1,2,3,4}
        print('-setA={1,2,3,4}')
        setB={3,4,5,6}
        print('-setB={3,4,5,6}')
        print(setA.union(setB))
        print('-print(setA.union(setB))')
        print(setA.intersection(setB))
        print('-print(setA.intersection(setB))')
        print(setA.difference(setB))
        print('-print(setA.difference(setB))')
        print(setA.issubset(setB))
        print('-print(setA.issubset(setB))')
        print(setA.issuperset(setB))
        print('-print(setA.issuperset(setB))')
    case "17" | "dictionary" | "17.dictionary":
        print("""
        dictionary
            dictionary คือข้อมูลที่เก็บข้อมูลหลายๆค่าไว้ในตัวแปรเดียวโดยใช้เครื่องหมาย { } ครอบข้อมูลและคั่นด้วย ,
            dictionary มีลักษณะคล้ายกับ set แต่ข้อมูลใน dictionary จะเก็บเป็นคู่ของ key(กุญแจ) กับ value(ค่า)
            key คือชื่อหรือตัวระบุของข้อมูลแต่ละค่าใน dictionary โดยต้องไม่ซ้ำกัน
            value คือค่าของข้อมูลแต่ละค่าใน dictionary โดยสามารถซ้ำกันได้
            dictionary สามารถใช้เครื่องหมาย + ในการต่อ dictionary เข้าด้วยกันได้
            dictionary ไม่สามารถใช้เครื่องหมาย * ในการทำซ้ำ dictionary ได้
            dictionary ไม่สามารถใช้เครื่องหมาย [] ในการเข้าถึงตำแหน่งของข้อมูลใน dictionary ได้เพราะไม่มีลำดับ
            dictionary สามารถใช้เครื่องหมาย [key] ในการเข้าถึงค่าของข้อมูลใน dictionary ได้โดยระบุ key
            dictionary ไม่สามารถใช้เครื่องหมาย [m:n] ในการเข้าถึงช่วงของข้อมูลใน dictionary ได้เพราะไม่มีลำดับ
            dictionary สามารถใช้คำสั่ง len() ในการนับจำนวนข้อมูลใน dictionary ได้
            dictionary สามารถใช้คำสั่ง dict() ในการแปลงค่าตัวแปรเป็น dictionary ได้
            dictionary สามารถใช้คำสั่ง .get(key) ในการเข้าถึงค่าของข้อมูลใน dictionary ได้โดยระบุ key
            dictionary สามารถใช้คำสั่ง .keys() ในการเข้าถึง key ทั้งหมดใน dictionary ได้
            dictionary สามารถใช้คำสั่ง .values() ในการเข้าถึง value ทั้งหมดใน dictionary ได้
            dictionary สามารถใช้คำสั่ง .items() ในการเข้าถึงคู่ของ key กับ value ทั้งหมดใน dictionary ได้
            dictionary สามารถใช้คำสั่ง .update({key:value}) ในการเพิ่มหรือแก้ไขข้อมูลใน dictionary ได้
            dictionary สามารถใช้คำสั่ง .pop(key) ในการลบข้อมูลออกจาก dictionary โดยระบุ key ได้
            dictionary สามารถใช้คำสั่ง .clear() ในการลบข้อมูลทั้งหมดใน dictionary ได้
            dictionary สามารถใช้คำสั่ง .copy() ในการคัดลอก dictionary ได้
            mydict={
                "name":"john",
                "age":20,
                "city":"new york"
                }
            print(mydict)
            print(mydict["name"])
            print(len(mydict))
            print(dict(name="john",age=20,city="new york"))
            print(mydict.get("age"))
            print(mydict.keys())
            print(mydict.values())
            print(mydict.items())
            mydict.update({"age":21})
            print(mydict)
            mydict.pop("city")
            print(mydict)
            mydict2=mydict.copy()
            print(mydict2)
            mydict.clear()
            print(mydict)
        """)
        mydict={
                "name":"john",
                "age":20,
                "city":"new york"
                }
        print('-mydict={ "name":"john", "age":20, "city":"new york" }')
        print(mydict)
        print('-print(mydict)')
        print(mydict["name"])
        print('-print(mydict["name"])')
        print(len(mydict))
        print('-print(len(mydict))')
        print(dict(name="john",age=20,city="new york"))
        print('-print(dict(name="john",age=20,city="new york"))')
        print(mydict.get("age"))
        print('-print(mydict.get("age"))')
        print(mydict.keys())
        print('-print(mydict.keys())')
        print(mydict.values())
        print('-print(mydict.values())')
        print(mydict.items())
        print('-print(mydict.items())')
        mydict.update({"age":21})
        print('-mydict.update({"age":21})')
        print(mydict)
        print('-print(mydict)')
        mydict.pop("city")
        print('-mydict.pop("city")')
        print(mydict)
        print('-print(mydict)')
        mydict2=mydict.copy()
        print('-mydict2=mydict.copy()')
        print(mydict2)
        print('-print(mydict2)')
        mydict.clear()
        print('-mydict.clear()')
        print(mydict)
        print('-print(mydict)')
    case "18" | "pattern matching" | "18.pattern matching":
        print("""
        pattern matching
            pattern matching คือการตรวจสอบรูปแบบของข้อมูลในตัวแปรว่าตรงกับรูปแบบที่กำหนดหรือไม่
            pattern matching สามารถใช้กับข้อมูลประเภท string, list, tuple, set, dictionary ได้
            pattern matching ใช้คำสั่ง match...case
            pattern matching มีอยู่ 7 รูปแบบ คือ
            1.ค่าคงที่ เช่น ตัวเลข อักขระ ข้อความ
            2.ตัวแปร เช่น a,b,c
            3.ลิสต์ เช่น [1,2,3] หรือ [a,b,c]
            4.ทูเพิล เช่น (1,2) หรือ (a,b)
            5.ดิกชันนารี เช่น {"name":"john","age":20} หรือ {"name":a,"age":b}
            6.การจับคู่แบบมีเงื่อนไข เช่น case x if x>0:
            7.การจับคู่แบบไม่ระบุค่า เช่น case _:
            text="hello"
            match text:
                case "hello":
                    print("สวัสดีครับ")
                case "hi":
                    print("หวัดดี")
                case _:
                    print("ไม่รู้จักคำนี้")
            number=10
            match number:
                case x if x>0:
                    print("จำนวนบวก")
                case x if x<0:
                    print("จำนวนลบ")
                case 0:
                    print("ศูนย์")
                case _:
                    print("ไม่ใช่ตัวเลข")
            mylist=[1,2,3]
            match mylist:
                case [1,2,3]:
                    print("ลิสต์ตรงกับ [1,2,3]")
                case [a,b,c]:
                    print(f"ลิสต์มีค่า {a},{b},{c}")
                case _:
                    print("ไม่ตรงกับลิสต์ใดๆ")
            mytuple=(1,2)
            match mytuple:
                case (1,2):
                    print("ทูเพิลตรงกับ (1,2)")
                case (a,b):
                    print(f"ทูเพิลมีค่า {a},{b}")
                case _:
                    print("ไม่ตรงกับทูเพิลใดๆ")
            mydict={"name":"john","age":20}
            match mydict:
                case {"name":"john","age":20}:
                    print("ดิกชันนารีตรงกับ {'name':'john','age':20}")
                case {"name":a,"age":b}:
                    print(f"ดิกชันนารีมีค่า name={a},age={b}")
                case _:
                    print("ไม่ตรงกับดิกชันนารีใดๆ")
              """)
        text="hello"
        match text:
                case "hello":
                    print("สวัสดีครับ")
                case "hi":
                    print("หวัดดี")
                case _:
                    print("ไม่รู้จักคำนี้")
        number=10
        match number:
                case x if x>0:
                    print("จำนวนบวก")
                case x if x<0:
                    print("จำนวนลบ")
                case 0:
                    print("ศูนย์")
                case _:
                    print("ไม่ใช่ตัวเลข")
        mylist=[1,2,3]
        match mylist:
                case [1,2,3]:
                    print("ลิสต์ตรงกับ [1,2,3]")
                case [a,b,c]:
                    print(f"ลิสต์มีค่า {a},{b},{c}")
                case _:
                    print("ไม่ตรงกับลิสต์ใดๆ")
        mytuple=(1,2)
        match mytuple:
                case (1,2):
                    print("ทูเพิลตรงกับ (1,2)")
                case (a,b):
                    print(f"ทูเพิลมีค่า {a},{b}")
                case _:
                    print("ไม่ตรงกับทูเพิลใดๆ")
        mydict={"name":"john","age":20}
        match mydict:
                case {"name":"john","age":20}:
                    print("ดิกชันนารีตรงกับ {'name':'john','age':20}")
                case {"name":a,"age":b}:
                    print(f"ดิกชันนารีมีค่า name={a},age={b}")
                case _:
                    print("ไม่ตรงกับดิกชันนารีใดๆ")
    case "19" | "ฟังก์ชัน" | "19.ฟังก์ชัน":       
        print("""
        ฟังก์ชัน
            ฟังก์ชันคือกลุ่มคำสั่งที่ถูกจัดกลุ่มไว้ด้วยกันเพื่อให้สามารถเรียกใช้ซ้ำได้')
            ฟังก์ชันใช้คำสั่ง def ชื่อฟังก์ชัน(พารามิเตอร์):')
            พารามิเตอร์คือค่าที่ส่งเข้าไปในฟังก์ชันเพื่อให้ฟังก์ชันทำงานตามค่าที่ส่งมา')
            ฟังก์ชันสามารถมีพารามิเตอร์ได้หลายตัวโดยคั่นด้วย ,')
            ฟังก์ชันสามารถมีพารามิเตอร์แบบกำหนดค่าเริ่มต้นได้โดยใช้ =')
            ฟังก์ชันสามารถมีพารามิเตอร์แบบไม่กำหนดค่าเริ่มต้นได้โดยไม่ใช้ =')
            ฟังก์ชันสามารถมีพารามิเตอร์แบบกำหนดค่าเริ่มต้นและไม่กำหนดค่าเริ่มต้นได้โดยให้พารามิเตอร์แบบไม่กำหนดค่าเริ่มต้นอยู่ข้างหน้า')
            ฟังก์ชันสามารถคืนค่าผลลัพธ์ได้โดยใช้คำสั่ง return')
            ฟังก์ชันสามารถเรียกใช้ฟังก์ชันภายในฟังก์ชันได้')
            ฟังก์ชันสามารถเรียกใช้ฟังก์ชันซ้ำได้โดยไม่จำกัดจำนวนครั้ง')
            ฟังก์ชั่นตัวเดียวกันสามารถมีพารามิเตอร์ต่างกันได้โดยใช้ * นำหน้าพร้อมบอกตำแหน่ง')

            def greet(name="guest"):
                print(f"สวัสดีครับ{name}")
            greet()
            def number(a,b):
                a+b
                return print("ผลลัพธ์:",a+b)#return คือนำคำสั่งไปทำงานนอกฟังก์ชัน
            number(10,20)
            def num():
                num=int(input("ป้อนตัวเลข:"))
                for i in range(1,13):
                    print(f"{num}x{i}={num*i}")
            num()
            def employee(*employee):
                print(f"ชื่อ{employee[0]} แผนก {employee[1]} เงินเดือน {employee[2]} บาท")
            employee("john","it",20000)
            employee("mary","hr",25000)
              """)
        def greet(name="guest"):
                print(f"สวัสดีครับ{name}")
        greet()
        def number(a,b):
                a+b
                return print("ผลลัพธ์:",a+b)#return คือนำคำสั่งไปทำงานนอกฟังก์ชัน
        number(10,20)
        def num():
                num=int(input("ป้อนตัวเลข:"))
                for i in range(1,13):
                    print(f"{num}x{i}={num*i}")
        num()
        def employee(*employee):
                print(f"ชื่อ{employee[0]} แผนก {employee[1]} เงินเดือน {employee[2]} บาท")
        employee("john","it",20000)
        employee("mary","hr",25000)
    case "20" | "ขอบเขตตัวแปร" | "20.ขอบเขตตัวแปร":
        print("""
        ขอบเขตตัวแปร
            local variable ตัวแปรที่ทำงานเฉพาะฟังก์ชั่นนั้นๆ')
            globle variable ตัวแปรที่ทำงานนอกฟังก์ชั่นแล้วทำงานได้ทุกฟังก์ชั่นที่สร้าง')

            def local():#local variable
                saly=1000
                print(saly)

            saly=10000#globle variable
            def bank(value):
                global saly
                mony = saly + value
                print(mony)
            bank(1000) 
              """)
        def local():#local variable
                saly=1000
                print(saly)

        saly=10000#globle variable
        def bank(value):
                global saly
                mony = saly + value
                print(mony)
        bank(1000)
    case "21" | "try...except" | "21.try...except":
        print("""
        try...except
            คำสั่งนี้คือการแสดงปัญหาที่เกิดขึ้นแต่ยังรันโปรแกรมต่อได้อยู่
            def exception():
                try:
                    number=int(input("ใส่ตัวเลข:"))
                    print("ตัวเเลขของท่านคือ:",number)
                except:#สามารถระบุข้อผิดพลาดได้
                    print('นี่ไม่ใช่ตัวเลข')
                finally:
                    print("end programe")
                exception()
        kw finally,raise
        finally คือคำสั่งดำเนินการของ exception ไม่ว่าจะมีปัญหาหรือไม่มีก็จะรันตำสั่งนี้ด้วย
        raise คือคำสั่งเพิ่มเติมของ exception หรือเพิ่มเติมข้อผิดพลาดเข้าไป 
              """)
        def exception():
                try:
                    number=int(input("ใส่ตัวเลข:"))
                    print("ตัวเเลขของท่านคือ:",number)
                except:#สามารถระบุข้อผิดพลาดได้
                    print('นี่ไม่ใช่ตัวเลข')
                finally:
                    print("end programe")
        exception()
    case "22" | "module" | "22.module":
        print("""
        module
            module คือไฟล์ที่เก็บฟังก์ชัน ตัวแปร หรือคลาสไว้ในไฟล์เดียวกันเพื่อให้สามารถเรียกใช้ซ้ำได้
            การสร้าง module ให้สร้างไฟล์ .py ขึ้นมาแล้วเขียนฟังก์ชัน ตัวแปร หรือคลาสลงไป
            การเรียกใช้ module ให้ใช้คำสั่ง import ชื่อไฟล์ หรือ from ชื่อไฟล์ import ชื่อฟังก์ชัน/ตัวแปร/คลาส
            การเรียกใช้ module สามารถใช้คำสั่ง as เพื่อเปลี่ยนชื่อ moduleได้
              """)
    case "23" | "import" | "23.import":
        print("""
        import
            import คือคำสั่งที่ใช้เรียกใช้ module ที่สร้างขึ้นมา
            import ชื่อไฟล์
            from ชื่อไฟล์ import ชื่อฟังก์ชัน/ตัวแปร/คลาส
            import ชื่อไฟล์ as ชื่อใหม่
            from ชื่อไฟล์ import * (คือการเรียกใช้ฟังก์ชัน ตัวแปร หรือคลาสทั้งหมดใน module)
              """)