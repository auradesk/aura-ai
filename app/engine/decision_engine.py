class DecisionEngine:
    def __init__(self, memory_engine, learning_engine):
        self.memory_engine = memory_engine
        self.learning_engine = learning_engine

    def make_decision(self, input_data):
        goal = input_data["goal"]
        options = input_data.get("options", [])

        scored_options = {}
        # Score options using memory + learning engine
        for option in options:
            # Basic scoring logic; can use past memory
            past_score = self.memory_engine.summary()["memory_entries"]
            scored_options[option] = min(1.0, 0.5 + 0.05 * past_score)

        # Choose highest scored option
        decision = max(scored_options, key=lambda k: scored_options[k])

        # Store in memory
        self.memory_engine.store(goal, decision, scored_options)

        return {
            "goal": goal,
            "decision": decision,
            "scored_options": scored_options
        }