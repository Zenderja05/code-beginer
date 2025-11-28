//alert("นี่คือบทเรียน java script ทั้งหมด ถ้าอยากดูโค้ดให้กด F12 แล้วไปที่ Console หรือ คลิกขวาแล้วเลือก Inspect แล้วไปที่ Console และ ดูในไฟล์ javascript.jsก็ได้");
// document.write("<h1>JAVA SCRIPT</h1>");
// ----------------------------------------------------------------------------------------------------------------------------------
// การสร้างตัวแปร
let name ="Zen";
console.log(name);
// ----------------------------------------------------------------------------------------------------------------------------------
// การแปลงชนิดข้อมูล
let value1 = "5"; // string
let value2 = 10;  // number
// แปลง string เป็น number
console.log(Number(value1) + value2);
// แปลง number เป็น string
console.log(value1 + String(value2));
// ----------------------------------------------------------------------------------------------------------------------------------
// การใช้ array
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); // แสดงผล "Apple"
// ----------------------------------------------------------------------------------------------------------------------------------
// คำสั่งเงื่อนไข if...else
let age = 20;
if (age < 18) {
    console.log("คุณยังไม่บรรลุนิติภาวะ");
} else {
    console.log("คุณบรรลุนิติภาวะแล้ว");
}
// คำสั่งเงื่อนไข switch...case
let day = 3;
switch (day) {
    case 1:
        console.log("วันจันทร์");
        break;
    case 2:
        console.log("วันอังคาร");
        break;
    case 3:
        console.log("วันพุธ");
        break;
    default:
        console.log("วันอื่น ๆ");
}
// ----------------------------------------------------------------------------------------------------------------------------------
// คำสั่ง LOOP
// for LOOP
for (let i = 0; i < 5; i++) {
    console.log("รอบที่ " + (i + 1));
}
// while LOOP
let count = 0;
while (count < 5) {
    console.log("นับ: " + (count + 1));
    count++;
}
// do..while LOOP
let doCount = 0;
do {
    console.log("นับ: " + (doCount + 1));
    doCount++;
} while (doCount < 5);
// ----------------------------------------------------------------------------------------------------------------------------------
// break
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break; // หยุดลูปเมื่อ i เท่ากับ 5
    }
    console.log("i: " + i);
}
// continue
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        continue; // ข้ามรอบที่ i เป็นเลขคู่
    }
    console.log("i: " + i);
}
// ----------------------------------------------------------------------------------------------------------------------------------
// null, undefined และ NaN
let a; // undefined
console.log(a); // แสดงผล undefined
let b = null;
console.log(b); // แสดงผล null
let c = "hello" / 2;
console.log(c); // แสดงผล NaN
// ----------------------------------------------------------------------------------------------------------------------------------
// ฟังก์ชั่น
function greet(name) {
    console.log("สวัสดี, " + name + "!");
}
greet("สมชาย");
// ฟังก์ชั่นแบบมีการรับค่า
function add(x, y) {
    console.log(x + y);
}
add(5, 10);
// ฟังก์ชั่นแบบมีการคืนค่า
function multiply(x, y) {
    return x * y;
}
multiply(5, 10);
// ฟังก์ชั่นแบบรับค่าและคืนค่า
function square(num) {
    return num * num;
}
let result = square(4);
console.log(result); // แสดงผล 16
// ----------------------------------------------------------------------------------------------------------------------------------
// array properties & function
let colors = ["Red", "Green", "Blue"];
// length property
console.log(colors.length); // แสดงผล 3
// push() function
colors.push("Yellow");
console.log(colors); // แสดงผล ["Red", "Green", "Blue", "Yellow"]
// pop() function
colors.pop();
console.log(colors); // แสดงผล ["Red", "Green", "Blue"]
// shift() function
colors.shift();
console.log(colors); // แสดงผล ["Green", "Blue"]
// unshift() function
colors.unshift("Purple");
console.log(colors); // แสดงผล ["Purple", "Green", "Blue"]
// indexOf() function
console.log(colors.indexOf("Green")); // แสดงผล 1
// ----------------------------------------------------------------------------------------------------------------------------------
// เข้าถึงอาเรย์แบบวนลูป
let numbers = [10, 20, 30, 40, 50];
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
// เข้าถึงสมาชิกarrayด้วย forech
numbers.forEach(function(number) {
    console.log(number);
});
// ----------------------------------------------------------------------------------------------------------------------------------
// การแปลงอาเรย์ให้เป็น string
// to string
let fruits2 = ["Mango", "Pineapple", "Grapes"];
console.log(fruits2.toString());
// join
console.log(fruits2.join(" - "));
// ----------------------------------------------------------------------------------------------------------------------------------
// การเพิ่ม ลบ แก้ไข อาเรย์
let veggies = ["Carrot", "Potato", "Cucumber"];
// การเพิ่มสมาชิกอาเรย์
veggies.push("Lettuce");
console.log(veggies);
// การลบสมาชิกอาเรย์
veggies.pop();
console.log(veggies);
// การแก้ไขสมาชิกอาเรย์
veggies[1] = "Tomato";
console.log(veggies);
// ----------------------------------------------------------------------------------------------------------------------------------
// การรวมอาเรย์
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let combinedArray = array1.concat(array2);
console.log(combinedArray); // แสดงผล [1, 2, 3, 4, 5, 6]
// ----------------------------------------------------------------------------------------------------------------------------------
// การเรียงลำดับสมาชิกอาเรย์
// เรียงแบบจากน้อยไปมาก
let unsortedArray = [3, 1, 4, 2, 5];
unsortedArray.sort(function(a, b) {
    return a - b;
});
console.log(unsortedArray); // แสดงผล [1, 2, 3, 4, 5]
// เรียงแบบจากมากไปน้อย
unsortedArray.sort(function(a, b) {
    return b - a;
});
console.log(unsortedArray); // แสดงผล [5, 4, 3, 2, 1]
// ----------------------------------------------------------------------------------------------------------------------------------
// javascript object
let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    greet: function() {
        console.log("Hello, " + this.firstName + " " + this.lastName);
    }
};
console.log(person.firstName); // แสดงผล "John"
person.greet(); // แสดงผล "Hello, John Doe"
// ----------------------------------------------------------------------------------------------------------------------------------
