def review(post, auto_approve=False):
    if auto_approve:
        print("✅ Auto-approved (scheduled run).")
        return True

    decision = input("\nApprove this post? (yes/no): ")
    return decision.lower() == "yes"
