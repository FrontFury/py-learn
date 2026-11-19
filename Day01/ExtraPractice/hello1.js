console.log("Hello, World!");


const term = "Variable";
console.log(`Today : ${term}`);

let learned = true;
let definition = false;
console.log(`Learned : ${learned}, Definition : ${definition}`);

if (learned) {
    console.log("Already learned JavaScript.");
}else {
    console.log("Still learning JavaScript.");
}

if(term === "Variable" && !learned) {
    console.log("You need to learn Variable.");
}

const tags = ["Python", "Variable"];
tags.push("api");
console.log(tags.length);
console.log(tags.includes("api"));