def save(post):
    with open("memory/memory.txt", "a", encoding="utf-8") as f:
        f.write(post + "\n---\n")
