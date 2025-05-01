# 🤖 Coding Assistant for Beginners

A friendly terminal-based coding assistant built with OpenAI's GPT API.  
Perfect for beginners who want to ask programming questions or get line-by-line code explanations.

---

## ✨ Features

- 🧠 Ask basic coding questions and get clear explanations
- 💬 Type `annotate: <your code>` to get line-by-line code analysis
- 🤝 Beginner-friendly responses powered by GPT-3.5
- 🔐 API key managed securely using `.env` file
- ✅ Works entirely in your terminal

---

## 📸 Examples

```bash
You> What is a list in Python?

Assistant>
A list is a built-in data structure that holds an ordered collection of items...

You> annotate: for i in range(3): print(i)

Assistant>
Line 1: `for i in range(3):` - Creates a loop that runs 3 times...
Line 2: `print(i)` - Prints the current value of `i`
