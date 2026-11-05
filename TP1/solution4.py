# Part B — a safe converter
def safe_int(text):
    """Turn text into an int; return None when it is not a number."""
    text = text.strip() 
    if text.lstrip("-").isdigit():        
        return int(text)          
    try:                                    
        return int(float(text))            
    except ValueError:
        return None                       

#Part C
for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample)) 

    a = safe_int(input("Enter first number: "))
b = safe_int(input("Enter second number: "))

if a is None or b is None:
    print("Please enter valid numbers.")
else:
    print("Sum =", a + b)
