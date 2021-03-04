code_input = "4 LBLBLBRRRAAA"
print(int(code_input.split(" ")[0]) + sum([{"R": 1, "L": -1, "A": -4, "B": 4}[move] for move in code_input.split(" ")[1]]))