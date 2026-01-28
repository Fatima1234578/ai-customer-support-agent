# app.py - Simple AI Customer Support Agent

# Step 1: Load tickets
issues = []
categories = []
responses = []

with open("tickets.txt", "r") as file:
    for line in file:
        category, issue, response = line.strip().split("|")
        categories.append(category)
        issues.append(issue.lower())
        responses.append(response)

# Step 2: Compare words to find similarity
def similarity(user_issue, old_issue):
    user_words = set(user_issue.lower().split())
    old_words = set(old_issue.split())
    return len(user_words & old_words)  # number of common words

# Step 3: Find the best matching issue
def resolve_issue(user_input):
    best_score = 0
    best_index = 0
    for i in range(len(issues)):
        score = similarity(user_input, issues[i])
        if score > best_score:
            best_score = score
            best_index = i
    return categories[best_index], responses[best_index]

# Step 4: App interface (simple)
def main():
    print("=== AI Customer Support Agent ===")
    while True:
        user_input = input("\nEnter customer issue (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting... Goodbye!")
            break
        category, reply = resolve_issue(user_input)
        print(f"\nCategory: {category}")
        print(f"Response: {reply}")

if __name__ == "__main__":
    main()
