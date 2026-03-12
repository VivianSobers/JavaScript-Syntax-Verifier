# JavaScript-Syntax-Verifier

Takes JavaScript code as input and verifies whether it is syntactically valid. It reports the exact line and token where a syntax error occurs, or confirms the code is error-free.

---

## Supported Constructs

| Construct | Example |
|---|---|
| Variable declaration | `var x = 5;` `let y;` `const z = "hello";` |
| Array declaration | `var arr = [1, 2, 3];` |
| Function definition | `function foo(a, b) { return a; }` |
| If / else | `if (x > 0) { ... } else { ... }` |
| For loop | `for (var i = 0; i < 10; i = i + 1) { ... }` |
| While loop | `while (x > 0) { ... }` |
| Return statement | `return x;` |
| Assignment | `x = 10;` |

---

## How to Run

### 1. Install dependencies

```bash
pip install ply
```

### 2. Run the verifier

```bash
python main.py
```

### 3. Choose a construct from the menu

```
JavaScript Syntax Verifier (PLY)
1. Variable declaration/instantiation
2. Iterative constructs (for/while)
3. Selective constructs (if/else)
4. Function declaration
5. Array declaration
6. Combination of all the above constructs
7. Exit
```

### 4. Enter your JavaScript code and type `exit` to verify

```
js> var x = 10;
js> if (x > 5) { return x; }
js> exit

--- Verifying Syntax ---
Syntax is valid! No errors detected.
```

## Author

**Vivian Sobers E** — [github.com/VivianSobers](https://github.com/VivianSobers)
