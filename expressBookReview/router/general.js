const express = require('express');
let books = require("./booksdb.js");
let isValid = require("./auth_users.js").isValid;
let users = require("./auth_users.js").users;
const public_users = express.Router();
const axios = require('axios');

public_users.post("/register", (req,res) => {
  const username = req.body.username;
  const password = req.body.password;

  if (username && password) {
    if (!isValid(username)) { 
      users.push({"username":username,"password":password});
      return res.status(200).json({message: "User successfully registred. Now you can login"});
    } else {
      return res.status(404).json({message: "User already exists!"});    
    }
  } 
  return res.status(404).json({message: "Unable to register user."});
});

// Get the book list available in the shop using async/await and Axios
public_users.get('/', async function (req, res) {
  try {
    // Simulating an async operation as required for the assignment using Promises
    const getBooks = () => {
        return new Promise((resolve) => {
            setTimeout(() => resolve(books), 500);
        });
    };
    const booksList = await getBooks();
    res.status(200).send(JSON.stringify(booksList, null, 4));
  } catch (error) {
    res.status(500).send("Error fetching books");
  }
});

// Get book details based on ISBN using Promises
public_users.get('/isbn/:isbn', function (req, res) {
  const isbn = req.params.isbn;
  
  const getBookByIsbn = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (books[isbn]) {
            resolve(books[isbn]);
        } else {
            reject("Book not found");
        }
    }, 500);
  });

  getBookByIsbn.then((book) => {
      res.status(200).send(book);
  }).catch((error) => {
      res.status(404).send(error);
  });
});
  
// Get book details based on author using async/await
public_users.get('/author/:author', async function (req, res) {
  const author = req.params.author;
  
  try {
      const getBooksByAuthor = () => {
          return new Promise((resolve, reject) => {
              setTimeout(() => {
                  let booksByAuthor = [];
                  for (let key in books) {
                      if (books[key].author === author) {
                          booksByAuthor.push(books[key]);
                      }
                  }
                  if (booksByAuthor.length > 0) {
                      resolve(booksByAuthor);
                  } else {
                      reject("Author not found");
                  }
              }, 500);
          });
      };
      
      const result = await getBooksByAuthor();
      res.status(200).send(result);
  } catch (error) {
      res.status(404).send(error);
  }
});

// Get all books based on title using Promises
public_users.get('/title/:title', function (req, res) {
  const title = req.params.title;
  
  const getBooksByTitle = new Promise((resolve, reject) => {
      setTimeout(() => {
          let booksByTitle = [];
          for (let key in books) {
              if (books[key].title === title) {
                  booksByTitle.push(books[key]);
              }
          }
          if (booksByTitle.length > 0) {
              resolve(booksByTitle);
          } else {
              reject("Title not found");
          }
      }, 500);
  });

  getBooksByTitle.then((result) => {
      res.status(200).send(result);
  }).catch((error) => {
      res.status(404).send(error);
  });
});

// Get book review
public_users.get('/review/:isbn', function (req, res) {
  const isbn = req.params.isbn;
  if (books[isbn]) {
      res.status(200).send(books[isbn].reviews);
  } else {
      res.status(404).send("Book not found");
  }
});

module.exports.general = public_users;
