# app/reasoning/goal_planner.py

class GoalPlanner:
    """
    Breaks a goal into sequential actionable steps.
    """

    def __init__(self):
        pass

    def plan(self, goal: str):
        """
        Returns a list of steps for a given goal.
        For now, uses simple keyword-based decomposition.
        """
        steps = []

        goal_lower = goal.lower()

        if "meeting" in goal_lower:
            steps.append("Check calendar availability")
            steps.append("Send meeting invitation")
            steps.append("Confirm meeting")

        elif "summarize" in goal_lower:
            steps.append("Retrieve relevant memories")
            steps.append("Extract key points")
            steps.append("Generate summary")

        elif "email" in goal_lower or "message" in goal_lower:
            steps.append("Draft message content")
            steps.append("Send message")
            steps.append("Log sent message in memory")

        else:
            steps.append("Analyze goal")
            steps.append("Break goal into micro-steps")
            steps.append("Execute micro-steps")

        return steps