RULES = [
    ({"interest_ai", "strong_math", "programming"}, "AI/ML Engineer"),
    ({"interest_data", "strong_math", "analytical"}, "Data Analyst"),
    ({"programming", "problem_solving", "interest_software"}, "Software Developer"),
    ({"networking", "security_interest", "problem_solving"}, "Cybersecurity Analyst")
]


def forward_chaining(facts):
    inferred = set(facts)
    recommendations = set()

    changed = True
    while changed:
        changed = False
        for conditions, career in RULES:
            if conditions.issubset(inferred) and career not in recommendations:
                recommendations.add(career)
                inferred.add("career:" + career)
                changed = True

    return recommendations


def backward_chaining(goal, facts):
    for conditions, career in RULES:
        if career == goal:
            return conditions.issubset(set(facts))
    return False


def csp_filter(careers, preferred):
    return [career for career in careers if career in preferred]


def main():
    print("AI Student Career Recommendation System")
    print("Enter facts separated by commas.")
    print("Examples: interest_ai, strong_math, programming")

    facts = {item.strip().lower() for item in input("Student facts: ").split(",")}

    inferred = forward_chaining(facts)
    valid = csp_filter(sorted(inferred), inferred)

    if not valid:
        print("No exact match. Build more skills or add profile facts.")
    else:
        print("\nRecommended careers:")
        for career in valid:
            print("-", career)
            print("  Goal verified:", backward_chaining(career, facts))


if __name__ == "__main__":
    main()
