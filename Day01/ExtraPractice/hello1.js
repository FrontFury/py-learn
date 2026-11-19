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

const note = {term: "Variable", definition: "A variable is a container for storing data values."};
console.log(note.term);


const notes = [
  {
    id: 1,
    term: "arrow function",
    definition: "A shorter syntax for writing function expressions.",
    python_equivalent: "lambda",
    tags: ["javascript", "functions"],
    learned: true,
  },
  {
    id: 2,
    term: "array",
    definition: "An ordered collection of values stored in a single variable.",
    python_equivalent: "list",
    tags: ["javascript", "data-structures"],
    learned: true,
  },
  {
    id: 3,
    term: "object",
    definition: "A collection of key-value pairs.",
    python_equivalent: "dictionary",
    tags: ["javascript", "data-structures"],
    learned: false,
  },
  {
    id: 4,
    term: "template literal",
    definition: "Strings enclosed in backticks allowing embedded expressions.",
    python_equivalent: "f-string",
    tags: ["javascript", "strings"],
    learned: false,
  },
];

for (const note of notes) {
    console.log(note.term);
}

const query = "LI";

for (const note of notes) {
  if (note.term.toLowerCase().includes(query.toLowerCase())) {
    console.log("Found:", note.term);
  }
}

function findTerm(notes, name) {
  for (const note of notes) {
    if (note.term === name) {
      return note;
    }
  }
}

console.log(findTerm(notes, "dict"));
console.log(findTerm(notes, "class"));