# programming a guessing game
### processing a guess


```rust
use std::io;

fn main() {
    println!("Guess the number");
    println!("Plese input your guess");
    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("failed to read ling");

    println!("you guessed: (guess)")

}
```

**Library** is a collection of pre-written code that you can use in your own program. Instead of writing everything from scratch, you borrow useful tools that someone already made.

**`std`** stands for "standard library." This is a library that comes built-in with Rust. You don't need to install anything — it's always available. It contains many useful tools for common tasks.

**`io`** stands for "input/output." It is one module (a smaller section) inside `std`. It gives you tools to receive input from the user (like keyboard typing) and send output to the screen.

**`use`** is a keyword that brings a tool into your code's scope. "Scope" just means "the area where your code can see and use something." Without `use`, your code doesn't know the tool exists.

**`::`** is called the "path separator." It works like a `/` in a file path. It tells Rust: "go inside this, and find that." So `std::io` means "go inside `std`, find `io`."

**`;`** is the "statement terminator." It tells Rust: "this line is finished." Almost every statement in Rust ends with `;`.

---

Now putting it all together:

rust

```rust
use std::io;
```

Reading it left to right:

- `use` → "I want to bring something into scope"
- `std` → "from the standard library"
- `::` → "go inside it"
- `io` → "and get the input/output module"
- `;` → "done, end of statement"

**Scope** is the area in your code where something exists and can be used. If something is "in scope," your code can see it and use it. If it is "out of scope," your code has no idea it exists.

**Prelude** is a small set of tools that Rust automatically brings into scope for every program. You don't need to write `use` for them — they are already available.

```rust
fn main() {
```
this function is the entry point of the program

- `fn` → declares new function
- `()` → indicates there are no parameters
- `{` → starts the body of the function

```rust
	println!("Guess the number!");
	println!("Please input your guess.");
```
This code is printing a prompt stating what the game is and requesting input from the user.

```rust
    let mut guess = String::new();
```
create a _variable_ to store the user input

- `let` = create variable
	example:
	`let apples = 5;`
	This line creates a new variable named `apples` and binds it to the value `5`
	In rust once we give a variable a value, the value wont change(immutable)
- `mut`= make the variable mutable
- `=` = bind something to the variable
- 