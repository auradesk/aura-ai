"""
Aura Healthcare Intelligence Engine
Phase 28
Provides safe, educational healthcare responses
"""


# Basic symptom knowledge base
SYMPTOM_KNOWLEDGE = {

    "chest pain": {
        "info": "Chest pain can have many causes, including muscle strain, acid reflux, anxiety, or heart-related conditions.",
        "action": "Chest pain can sometimes be serious. You should seek medical attention, especially if it is severe, sudden, or accompanied by other symptoms."
    },

    "headache": {
        "info": "Headaches are common and may be caused by stress, dehydration, lack of sleep, or illness.",
        "action": "Rest, hydration, and stress management may help. Seek medical care if headaches are severe or persistent."
    },

    "fever": {
        "info": "Fever is usually a sign that your body is fighting an infection.",
        "action": "Monitor temperature and stay hydrated. Seek medical care if fever is very high or lasts several days."
    },

    "fatigue": {
        "info": "Fatigue can result from lack of sleep, stress, illness, or nutritional deficiencies.",
        "action": "Rest and proper nutrition may help. Seek medical advice if fatigue persists."
    }

}


# Safety disclaimer
DISCLAIMER = (
    "\n\n⚠️ This information is for educational purposes only "
    "and is not medical advice. Please consult a licensed "
    "healthcare professional for diagnosis or treatment."
)


def analyze_symptoms(message: str):
    """
    Analyze message and return healthcare-safe response
    """

    message_lower = message.lower()

    for symptom, data in SYMPTOM_KNOWLEDGE.items():

        if symptom in message_lower:

            return (
                f"Aura Healthcare Intelligence:\n\n"
                f"Detected symptom: {symptom}\n\n"
                f"Information:\n{data['info']}\n\n"
                f"Recommended action:\n{data['action']}"
                f"{DISCLAIMER}"
            )

    # Default healthcare response
    return (
        "Aura Healthcare Intelligence:\n\n"
        "I understand your concern. Could you provide more details "
        "about your symptoms, such as duration, severity, and "
        "any additional symptoms?"
        f"{DISCLAIMER}"
    )
