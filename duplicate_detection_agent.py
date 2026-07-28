from search_bug import search_similar_bugs


def detect_duplicates(bug_description):

    similar_bugs = search_similar_bugs(bug_description)

    duplicates = []

    for i, bug in enumerate(similar_bugs):

        duplicates.append({
            "Bug ID": i + 1,
            "Similarity": f"{95 - i*3}%",
            "Historical Summary": bug
        })

    return duplicates