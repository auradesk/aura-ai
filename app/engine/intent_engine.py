# app/engine/intent_engine.py

class IntentEngine:

    def detect_intent(self, message: str) -> str:

        msg = message.lower()

        # Identity intent
        if any(x in msg for x in [
            "my name",
            "who am i",
            "what is my name",
            "do you know me"
        ]):
            return "identity"

        # Memory save intent
        if any(x in msg for x in [
            "remember",
            "save this",
            "store this",
            "my favorite"
        ]):
            return "memory_store"

        # Memory recall intent
        if any(x in msg for x in [
            "what do you remember",
            "recall",
            "what do i like",
            "what do i love"
        ]):
            return "memory_recall"

        # Knowledge intent
        if any(x in msg for x in [
            "what is",
            "explain",
            "define",
            "tell me about"
        ]):
            return "knowledge"

        # Greeting intent
        if any(x in msg for x in [
            "hello",
            "hi",
            "hey"
        ]):
            return "greeting"

        # Default intent
        return "general"


intent_engine = IntentEngine()
