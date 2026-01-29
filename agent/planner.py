from memory.store import get_used_topics

TOPIC_POOL = [
    "AI agents for beginners",
    "Human-in-the-loop AI systems",
    "Why automation still needs humans",
    "AI agents vs chatbots",
    "How AI agents use memory",
]

def decide_topic():
    used_topics = get_used_topics()

    for topic in TOPIC_POOL:
        if topic not in used_topics:
            return topic

    return "AI agents: advanced concepts"
