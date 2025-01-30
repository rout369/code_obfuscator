import ast
import base64
import random
import string


def analyze_code(code):
    """
    Analyzes the code and returns a summary of the constructs present.
    """
    tree = ast.parse(code)
    analysis = {
        "functions": [],
        "classes": [],
        "variables": [],
        "imports": [],
        "has_oop": False,
    }

    # Traverse the AST to find all relevant constructs
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            analysis["functions"].append(node.name)
        elif isinstance(node, ast.ClassDef):
            analysis["classes"].append(node.name)
            analysis["has_oop"] = True  # If any class is found, it is OOP
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    analysis["variables"].append(target.id)
        elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            analysis["imports"].append(node.names[0].name)

    return analysis



def random_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def encode_strings(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.Str):
            encoded = base64.b64encode(node.s.encode()).decode()
            # Generate random obfuscated names
            obf_module_name = random_name()
            obf_func_name = random_name()
            # Dynamically import and use obfuscated names
            node.s = '__import__("{}").{}("{}")'.format(obf_module_name, obf_func_name, encoded)
    return ast.unparse(tree)


# obfuscator/flattener.py

def remove_whitespace(code):
    """
    Removes unnecessary whitespace and newlines from the code to make it less readable.
    """
    # Remove leading and trailing whitespace from each line and join them
    code = ''.join(line.strip() for line in code.splitlines())
    return code


# obfuscator/flattener.py

def flatten_code(code):
    """
    Flattens the code by combining multiple lines into fewer lines, ensuring proper syntax.
    """
    # Split the code into statements and filter out empty ones
    statements = [line.strip() for line in code.splitlines() if line.strip()]
    
    # Join the statements into a single line with proper separation
    # We need to use semicolons to separate the statements
    return '; '.join(statements)



class VariableRenamer(ast.NodeTransformer):
    def __init__(self):
        self.mapping = {}

    def random_name(self):
        return ''.join(random.choices(string.ascii_letters, k=8))

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):  # Rename variables being defined
            if node.id not in self.mapping:
                self.mapping[node.id] = self.random_name()
            node.id = self.mapping[node.id]
        elif isinstance(node.ctx, ast.Load):  # Use mapped names for variables
            if node.id in self.mapping:
                node.id = self.mapping[node.id]
        return node

def rename_variables(code):
    tree = ast.parse(code)
    renamer = VariableRenamer()
    transformed_tree = renamer.visit(tree)
    return ast.unparse(transformed_tree)
