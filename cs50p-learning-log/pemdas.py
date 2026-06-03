def parse_expression(expr_str):
    # Remove all spaces
    expr_str = expr_str.replace(" ", "")
    
    tokens = []
    current_num = ""
    
    for char in expr_str:
        if char in "+-*/":
            if current_num:
                tokens.append(float(current_num))
                current_num = ""
            tokens.append(char)
        elif char.isdigit() or char == ".":
            current_num += char
        else:
            raise ValueError(f"Invalid character: {char}")
            
    if current_num:
        tokens.append(float(current_num))
        
    return tokens

def compute_operations(tokens, ops_to_do):
    i = 0
    while i < len(tokens):
        if tokens[i] in ops_to_do:
            op = tokens[i]
            left_num = tokens[i - 1]
            right_num = tokens[i + 1]
            
            # Perform calculation
            if op == "*":
                result = left_num * right_num
            elif op == "/":
                if right_num == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = left_num / right_num
            elif op == "+":
                result = left_num + right_num
            elif op == "-":
                result = left_num - right_num
                
            # Replace the 3 items (left, op, right) with the single result
            tokens[i - 1 : i + 2] = [result]
            # Stay at the same index since we shrunk the list
            i -= 1
        i += 1
    return tokens

def calculate(expr_str):
    tokens = parse_expression(expr_str)

    tokens = compute_operations(tokens, ["*", "/"])
    
    tokens = compute_operations(tokens, ["+", "-"])
    
    return tokens[0]

def main():
    print("--- Multi-Number PEMDAS Calculator ---")
    print("Enter any arithmetic expression (e.g., 10 + 5 * 2 - 4 / 2)")
    
    user_input = input("Expression: ")
    try:
        final_answer = calculate(user_input)
        print(f"Result: {final_answer}")
    except ZeroDivisionError:
        print("Error: Math error! Division by zero detected.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Error: Invalid expression formatting.")

if __name__ == "__main__":
    main()
