# fkcboi
Interpreter of the esoteric language Brainfuck written in an even more esoteric language: boi-lang.

## Why did you do this?

I'm an absolute madman.

## How does it work?

[Boi-lang](https://github.com/KernelDeimos/boi-lang) is extremely limited so things had to be done carefully.

- There are no arrays or pointers, so the entire memory space had to be stored in a single variable
- Luckily, boi-lang variables are arbitrary precision big-ints, meaning they can have infinite length.
- Therefore, each 8 bit character is encoded int a three digit decimal number and appended to the memory block.

For example, the numbers `123`, `555`, and `789` would be stored as a single number: `123555789`

- You can extract each of these numbers with math. For example:

~~~
123555789 / 1000 = 123555
123555    * 1000 = 123555000
123555789 - 123555000 = 789   <-- The number we want
~~~

- Similarily, the Brainfuck program must be stored as a number, because boi-lang cannot parse through strings. See below.

## How can I run it?

1. Get the [Boi-lang](https://github.com/KernelDeimos/boi-lang) intepreter.
2. Convert the Brainfuck code to boi-lang:

- A Python script, `convert_to_boi.py` takes care of that. Simply run it, paste in your BF code (single line), and it will give you several lines out output that should be placed in the bottom of the `fckboi.boi` file.

3. Run the program with `boi-lang fckboi.boi`

## Caveats

- Boi-lang numbers are unsigned. Only use positive numbers please.
- Boi-lang places an annoying newline after every print. Learn to read words vertically.
- Boi-lang uses bigints internally but you can only assign varibles with 64 bit ints. That's why the code is split over many lines when you convert it.

## r u ok

Do you mean emotionally or physically?
