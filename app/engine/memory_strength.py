import math


class MemoryStrengthCalculator:

    def calculate_strength(self, memory):

        importance = memory.importance or 0.5
        confidence = memory.confidence or 0.5
        recall_count = memory.recall_count or 0

        strength = importance * confidence * math.log(recall_count + 1)

        return strength


memory_strength = MemoryStrengthCalculator()