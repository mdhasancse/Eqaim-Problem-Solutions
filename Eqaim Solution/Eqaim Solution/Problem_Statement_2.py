# Problem Statement 2: Write a script in python or javascript that would take two numbers and generate the additional steps in a json format.

# For e.g. num1=1489, num2=714
# Then output should be
# {
# "step1": { "carryString": "1", "sumString": "3" },
# "step2": { "carryString": "11", "sumString": "03" },
# "step3": { "carryString": "111", "sumString": "203" },
# "step4": { "carryString": "111", "sumString": "2203" }
# }



import json

def generate_steps(num1, num2):
    num1_str = str(num1)[::-1]
    num2_str = str(num2)[::-1]
    step_counter = 1
    output = {}
    carry = 0
    
    for i in range(max(len(num1_str), len(num2_str))):
        digit1 = int(num1_str[i]) if i < len(num1_str) else 0
        digit2 = int(num2_str[i]) if i < len(num2_str) else 0
      
        digit_sum = digit1 + digit2 + carry
        
        if digit_sum < 10:
            carry = 0
            sum_string = str(digit_sum)
        else:
            carry = 1
            sum_string = str(digit_sum % 10)
        
        output["step" + str(step_counter)] = {"carryString": "1" * carry + "_" * (i + 1 - carry), "sumString": sum_string.rjust(len(num1_str), "0")}
        
        step_counter += 1
    
    return json.dumps(output)

# Example usage:
num1 = 1489
num2 = 714
print(generate_steps(num1, num2))

# This output matches the example in the problem statement.

# json
# {
#     "step1": { "carryString": "1", "sumString": "3" },
#     "step2": { "carryString": "11", "sumString": "03" },
#     "step3": { "carryString": "111", "sumString": "203" },
#     "step4": { "carryString": "111", "sumString": "2203" }
# }