# PyNandium

**From NAND to Programs: Building a Computer in Pure Python**

PyNandium is an educational project where we construct a complete virtual computer system—from the ground up—using only the `nand` logic gate as the fundamental building block.

This project is inspired by the spirit of "Nand2Tetris", but implemented entirely in Python, aiming to demonstrate how computers work at every level—from basic logic gates to running a high-level application.

---

## 🚀 Project Goals

- Build a working digital logic simulator starting from a `nand` gate.
- Construct:
  - Basic logic gates: AND, OR, NOT, XOR...
  - Arithmetic components: Adders, ALU...
  - Sequential components: Flip-flops, registers, RAM...
  - A CPU capable of executing a custom Instruction Set Architecture (ISA).
  - An assembler/interpreter for programs.
  - High-level programs running on the virtual machine.

---

## 🧱 Layers of Construction

1. **Logic Gates** - Built from the `nand` gate
2. **Combinational Circuits** - Adders, multiplexers, etc.
3. **Sequential Circuits** - Flip-flops, registers, counters, RAM
4. **CPU** - ALU + control unit + program counter
5. **Instruction Set Architecture** - Custom machine language
6. **Assembler** - Converts assembly to binary
7. **Virtual OS** - A basic loader, memory management, I/O
8. **Application Programs** - Programs that run on the machine

---

## 🧰 Requirements

- Python 3.8+
- No external libraries required (pure Python by default)

---

## 🔧 Getting Started

```bash
git clone https://github.com/tangmmy/pynandium.git
cd pynandium
python run.py
```

## 📂 Project Structure (Planned)

```
pynandium/
│
├── gates/          # NAND, AND, OR, NOT, etc.
├── circuits/       # Adders, multiplexers, etc.
├── sequential/     # Flip-flops, registers, RAM
├── cpu/            # ALU, control unit, PC
├── isa/            # Instruction formats
├── assembler/      # Assembler from assembly to binary
├── vm/             # Virtual machine runtime
├── programs/       # Sample programs to run
└── run.py          # Entry point to run a program on the machine
```


## 🤝 Contributions
Contributions, ideas, and discussions are welcome! This project is about learning and building from first principles, so feel free to fork and experiment.

## 📘 License
MIT License
