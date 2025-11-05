def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    char_counts = {}

    for c in text:
        if not c.isspace():
            c = c.lower()
            if c not in char_counts:
                char_counts[c] = 1
            else:
                char_counts[c] += 1

    return char_counts

def sorted_character_counts(counts_dict):
    counts_list = []

    for c in counts_dict:
        counts_list.append({"char": c, "num": counts_dict[c]})

    counts_list.sort(key=lambda k: k["num"], reverse=True)
    return counts_list

        
