def dfa_transition(state, symbol):
    transitions = {
        0: {'<': 1},
        1: {'h': 2, 'H': 2, 't': 8, 'T': 8, 'b': 14, 'B': 14, 'p': 18, 'P': 18, '/': 22},
        2: {'t': 3, 'T': 3, '1': 7},
        3: {'m': 4, 'M': 4},
        4: {'l': 5, 'L': 5},
        5: {'>': 6},
        6: {},  # Accept state for <html>
        7: {'>': 6},  # Accept state for <h1>
        8: {'i': 9, 'I': 9},
        9: {'t': 10, 'T': 10},
        10: {'l': 11, 'L': 11},
        11: {'e': 12, 'E': 12},
        12: {'>': 13},
        13: {},  # Accept state for <title>
        14: {'o': 15, 'O': 15},
        15: {'d': 16, 'D': 16},
        16: {'y': 17, 'Y': 17},
        17: {'>': 6},
        18: {'>': 6},
        22: {'h': 23, 'H': 23},
        23: {'t': 24, 'T': 24, '1': 7},
        24: {'m': 25, 'M': 25},
        25: {'l': 26, 'L': 26},
        26: {'>': 6},
    }
    return transitions.get(state, {}).get(symbol, None)

def dfa_accepts(input_string): # melihat apakah dfa tersebut accept atau tidak
    state = 0
    for symbol in input_string:
        state = dfa_transition(state, symbol)
        if state is None:
            return False
    return state == 6

def main():
    recognized_tags = ["<html>", "<head>", "<title>", "<body>", "<h1>", "<p>", "</html>", "</head>", "</title>", "</body>", "</h1>", "</p>"]
    user_input = input("Masukkan tag HTML: ").strip() # meminta input

    if any(dfa_accepts(user_input) and user_input.lower() == tag.lower() for tag in recognized_tags): # Kondisi dfa_accept & input user ada di recognized tags (walaupun ada perbedaan besar kecil huruf)
        print(f"Tag '{user_input}' : Accepted")
    else:
        print(f"Tag '{user_input}' : Rejected")

if __name__ == "__main__":
    main()