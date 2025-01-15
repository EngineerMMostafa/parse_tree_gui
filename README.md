# Parse Tree Visualization Tool

This project is a Python-based GUI application for generating and visualizing parse trees from a user-defined context-free grammar (CFG) and expression. It uses the NLTK library for parsing and Graphviz for visualizing the resulting tree structure.

## Features
- Define a custom grammar in CFG format.
- Input expressions to parse using the defined grammar.
- Generate and visualize parse trees as images.
- Interactive GUI built with Tkinter for ease of use.

---

## Requirements
To run this script, you need to install the following dependencies:

- Python 3.7 or later
- Libraries listed in `requirements.txt`:
  ```plaintext
  nltk==3.9.1
  graphviz==0.20.3
  pillow==11.1.0
  ```

- Graphviz executable installed on your system and added to the PATH. Follow [Graphviz Installation Guide](https://graphviz.gitlab.io/download/) if you don’t have it installed.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:EngineerMMostafa/parse_tree_gui.git
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Graphviz is Installed**:
   - Install Graphviz from [here](https://graphviz.gitlab.io/download/).
   - Make sure the `dot` executable is in your system PATH.

---

## Usage

1. **Run the Application**:
   ```bash
   python parse_tree_gui.py
   ```

2. **Using the GUI**:
   - Enter your CFG grammar in the "Enter Grammar" text area. Example grammar:
     ```
     S -> S S | '(' S ')' | '(' ')'
     ```
   - Enter the expression to parse in the "Enter Expression" field. Example:
     ```
     ( ( ) ) ( )
     ```
   - All entered text must be space separated 
   - Click the "Generate Tree" button.
   - The parse tree will be generated and displayed as an image below the button.

---

## Example Grammar and Expression

### Grammar:
```plaintext
    Expr -> Term | Term '+' Expr | Term '-' Expr
    Term -> Factor | Factor '*' Term | Factor '/' Term
    Factor -> '(' Expr ')' | Num
    Num -> '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0'
```

### Expression:
```plaintext
3 + 5 * ( 2 - 8 )
```

The generated parse tree will visually represent how the expression is derived based on the grammar rules.

---

## License
This project is open-source and available under the MIT License.

---

## Acknowledgments
- **NLTK**: For parsing and grammar tools.
- **Graphviz**: For rendering and visualizing the parse tree.
- **Tkinter**: For building the user-friendly GUI.
