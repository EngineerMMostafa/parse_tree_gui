import tkinter as tk
from tkinter import ttk, messagebox
from nltk import CFG, ChartParser
from nltk.tree import Tree
from graphviz import Digraph
from itertools import count
from PIL import Image, ImageTk


def generate_parse_tree(grammar_text, expression_text, output_path="parse_tree"):
    """
    Generates a parse tree from the given context-free grammar and expression.

    This function uses the NLTK library to parse the expression according to the
    specified grammar, and visualizes the resulting tree using the Graphviz library.

    Parameters:
        grammar_text (str): A string containing the grammar in CFG format. Each rule should be space-separated.
        expression_text (str): A string containing the expression to parse, with symbols space-separated.
        output_path (str, optional): The file path where the generated tree image will be saved.
                                     Defaults to "parse_tree".

    Returns:
        None: The function saves the generated tree visualization as an image at the specified path.
    """
    try:
        grammar = CFG.fromstring(grammar_text)
        expression = expression_text.split()
        parser = ChartParser(grammar)
        tree = next(parser.parse(expression))

        def tree_to_graphviz(tree: Tree):
            """
            Converts an NLTK Tree object into a Graphviz graph for visualization.

            This function traverses the tree structure, adding nodes and edges to a Graphviz
            directed graph, and returns the graph for rendering.

            Parameters:
                tree (Tree): An NLTK Tree object representing the parse tree.

            Returns:
                Digraph: A Graphviz Digraph object representing the parse tree, ready for rendering.
            """

            def traverse(subtree, parent_id, dot, unique_id_counter):
                node_id = id(subtree)
                dot.node(str(node_id), subtree.label(), shape="ellipse", style="filled", color="lightblue")
                if parent_id is not None:
                    dot.edge(str(parent_id), str(node_id), color="blue")
                for child in subtree:
                    if isinstance(child, Tree):
                        traverse(child, node_id, dot, unique_id_counter)
                    else:
                        unique_leaf_id = f"{id(child)}_{next(unique_id_counter)}"       # unique leaf nodes
                        dot.node(unique_leaf_id, child, shape="box", style="filled", color="lightgreen")
                        dot.edge(str(node_id), unique_leaf_id, color="blue")

            dot = Digraph(format="png", engine="dot")
            unique_id_counter = count()
            traverse(tree, None, dot, unique_id_counter)
            return dot

        # Render and save the tree image
        dot = tree_to_graphviz(tree)
        output_file = dot.render(output_path, format="png", cleanup=True)
        return output_file  # Return the path to the generated image

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate parse tree: {e}")
        return None


def on_generate_tree():
    grammar_text = grammar_text_area.get("1.0", tk.END).strip()
    expression_text = expression_entry.get().strip()

    if not grammar_text or not expression_text:
        messagebox.showwarning("Required Input", "Please provide both grammar and expression.")
        return

    output_file = generate_parse_tree(grammar_text, expression_text)
    if output_file:
        load_tree_image(output_file)


def load_tree_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Resize image to fit in the GUI
        photo = ImageTk.PhotoImage(image)

        tree_image_label.config(image=photo)
        tree_image_label.image = photo
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load tree image: {e}")


# Create the GUI
root = tk.Tk()
root.title("Parse Tree Generator")
root.geometry("600x750")

# Grammar input
grammar_label = ttk.Label(root, text="Enter Grammar (in CFG format):")
grammar_label.pack(pady=5)
grammar_text_area = tk.Text(root, height=10, width=70)
grammar_text_area.pack(pady=5)

# Expression input
expression_label = ttk.Label(root, text="Enter Expression:")
expression_label.pack(pady=5)
expression_entry = ttk.Entry(root, width=50)
expression_entry.pack(pady=5)

# Generate Tree Button
generate_button = ttk.Button(root, text="Generate Tree", command=on_generate_tree)
generate_button.pack(pady=10)

# Tree Image Display
tree_image_label = ttk.Label(root)
tree_image_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
