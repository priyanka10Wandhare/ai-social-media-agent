from agent.planner import decide_topic
from agent.generator import generate
from agent.reviewer import review
from memory.store import save


def main_agent_run(auto_approve=False):
    topic = decide_topic()
    post = generate(topic)

    print("\nGenerated Post:\n")
    print(post)

    if review(post, auto_approve=auto_approve):
        save(post, topic)
        print(f"\nPost stored. Topic saved: {topic}")
    else:
        print("\nPost rejected.")


if __name__ == "__main__":
    main_agent_run(auto_approve=False)
