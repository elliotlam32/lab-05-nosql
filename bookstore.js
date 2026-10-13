// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
db.authors.find()
db.books.find()

// Step 6: insert two new books
db.books.insertOne({ title: 'Emma', published_year: 1815, author_ids: [ 'author_001' ]})
db.books.insertOne({ title: 'JimmyEatsSandwich', published_year: 2026, author_ids: [ 'author_004' ]})

// Step 7: add missing authors
db.authors.insertOne({ _id:'author_004', name: 'Jimmy Brown', nationality: 'USA', bio: {short: 'aspiring data science student at the uva school of data science', long: 'JimyJIMYMJIYJJIYJYMYMMMYMMMYYMYMYMY stuff'}})

// Step 8: filter books by a list of authors
db.books.find({ author_ids: { $in: ["author_001", "author_004"] } })