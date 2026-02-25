def select_relevant_memories(memories, current_message, max_memories=3):
    """
    Select only memories relevant to current message using keyword matching
    """

    medical_keywords = {
        "pain", "chest", "heart", "breathing",
        "symptom", "sick", "hurt", "pressure",
        "doctor", "hospital", "health"
    }

    message_words = set(current_message.lower().split())

    relevant = []

    for memory in memories:

        memory_words = set(memory.user_message.lower().split())

        # Find overlap
        overlap = message_words.intersection(memory_words)

        # Only include if overlap contains meaningful keywords
        if overlap.intersection(medical_keywords):
            relevant.append(memory)

    # Return limited number
    return relevant[:max_memories]
