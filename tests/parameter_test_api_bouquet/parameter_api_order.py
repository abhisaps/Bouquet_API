from src.backend_code.utility.constants import menu1

test_data_1 = [
    ("ABC", menu1, ["A", "B", "C"], {"A": 1, "B": 1, "C": 1}),
    ("ABCDE", menu1, ["A", "B", "C", "D", "E"], {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1},),
    ("AAABBCE", menu1, ["A", "B", "C", "E"], {"A": 3, "B": 2, "C": 1, "E": 1}),
    ("", menu1, [], {}),
    ("QWERSD", menu1, ["Q", "W", "E", "R", "S", "D"], {"Q": 1, "W": 1, "E": 1, "R": 1, "S": 1, "D": 1}),
    ("", "", [], {}),
]

test_data_2 = [
        (["A", "B", "C"], {"A": 1, "B": 1, "C": 1}, menu1, [], "ABC", []),
        (["A", "B", "C", "D", "E"], {"A": 5, "B": 2, "C": 1, "D": 3, "E": 1}, menu1, [], "AAAAABBCDDDE", []),
        ([], {}, menu1, [], "", []),
        (["C", "Z", "N", "Q", "E"], {"C": 1, "Z": 1, "N": 1, "Q": 1, "E": 1}, menu1, ["Z", "N", "Q"], "CE", []),
        (["X", "W", "P", "U"], {"X": 4, "W": 2, "P": 1, "U": 1}, menu1, ["X", "W", "P", "U"], "", []),
        (["X", "W", "A", "B", "E", "C"], {"X": 4, "W": 2, "A": 7, "B": 1, "E": 10, "C": 4}, menu1, ["X", "W"], "AAAAABEEEEECCCC", ["A", "E"]),
]
