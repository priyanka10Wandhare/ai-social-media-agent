MEMORY_FILE = "memory/memory.txt"

def save(post, topic):
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"TOPIC: {topic}\n")
        f.write(post + "\n---\n")


def get_used_topics():
    topics = set()

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TOPIC:"):
                    topics.add(line.replace("TOPIC:", "").strip())
    except FileNotFoundError:
        pass

    return topics
