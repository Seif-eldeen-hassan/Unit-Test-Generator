import ast

def get_functions_from_code(source_code: str):
    try:
        code_tree = ast.parse(source_code)
        functions = [node for node in code_tree.body if isinstance(node, ast.FunctionDef)]
        return functions
    except SyntaxError:
        return []

def clean_function(function_node: ast.FunctionDef):
    new_body = []
    for node in function_node.body:
        is_standalone_string = (
            isinstance(node, ast.Expr) and 
            isinstance(node.value, (ast.Str, ast.Constant, ast.JoinedStr))
        )
        if not is_standalone_string:
            new_body.append(node)
            
    function_node.body = new_body
    return ast.unparse(function_node)