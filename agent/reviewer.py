def review(post):
    decision = input("\nApprove this post? (yes/no): ")
    return decision.lower() == "yes"
