## making a project with cargo
1. open terminal
2. go to the file that u want to make the project in
3. command : cargo new projectname

inside project their will be
- cargo.toml - acts like an assistant
- src
	- main.rs

**cargo new will automatically git init and make .git and .gitignore inside the project**

**cargo.toml**
An instruction sheet for Cargo. It has two sections.
[package] — Defines "what this project is." Name, version, and Rust edition. Cargo reads this to determine how to compile.
[dependencies] — "List any external libraries (crates) here." Currently empty. Used starting in Chapter 2.

**SRC**
all the files related to the code must be inside src
others can be on the top directory like README.md file

| command       | function                                                       |
| ------------- | -------------------------------------------------------------- |
| `cargo new`   | create a project                                               |
| `cargo init`  | make the file into a project                                   |
| `cargo build` | build a project                                                |
| `cargo run`   | build and run a project in one step                            |
| `cargo check` | build a project without producing a binary to check for errors |
- Instead of saving the result of the build in the same directory as our code, Cargo stores it in the _target/debug_ directory.
- compile = source cord to machine language(binary 0100010101)
- build = turning human readable code to computer processing file(binary file)
- Cargo puts the binary in a directory named _debug_

**when you open on vscode open the full project file**

### Building for release
`cargo build --release`
- This command will create an executable in _target/release_ instead of _target/debug_.
- The optimizations make your Rust code run faster, but turning them on lengthens the time it takes for your program to compile.