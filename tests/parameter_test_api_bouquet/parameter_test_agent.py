from src.backend_code.utility.constants import menu1

test_data_1 = [(menu1, ["Rose", "Lily", "Tulip", "Daisy", "Orchid"])]

test_data_2 = [
    ("ABCDE", menu1, [], "ABCDE", []),
    ("SGFGGT", menu1, ["S", "G", "F", "T"], "", []),
    ("ABBBBBDEV", menu1, ["V"], "ABBBBBDE", []),
    ("", menu1, [], "", []),
    ("AAAAAAACXDEAQ", menu1, ["X", "Q"], "AAAAACDE", ["A"]),
    ("AAAAAAABBBBBBBBSSSSXXXDDDDDDDDDDQQQZXX", menu1, ["S", "X", "Q", "Z"], "AAAAABBBBBDDDDD", ["A", "B", "D"])
]
