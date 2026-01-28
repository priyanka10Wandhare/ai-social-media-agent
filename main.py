from agent.planner import decide_topic
from agent.generator import generate
from agent.reviewer import review
from memory.store import save

if __name__ == "__main__":
    topic = decide_topic()
    post = generate(topic)

    print("\nGenerated Post:\n")
    print(post)

    if review(post):
        save(post)
        print("\nPost approved and stored.")
    else:
        print("\nPost rejected.")
