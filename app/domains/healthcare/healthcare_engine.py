class HealthcareEngine:

    def __init__(self):

        self.symptom_database = {

            "chest pain": {
                "info": "Chest pain can have many causes, including muscle strain, acid reflux, anxiety, or heart-related conditions.",
                "action": "Chest pain can sometimes be serious. Seek immediate medical attention, especially if severe, sudden, or accompanied by shortness of breath, sweating, or nausea."
            },

            "headache": {
                "info": "Headaches are common and can be caused by stress, dehydration, lack of sleep, or illness.",
                "action": "Rest, hydrate, and seek medical attention if severe or persistent."
            },

            "fever": {
                "info": "Fever is often a sign of infection or illness.",
                "action": "Monitor temperature, rest, and stay hydrated. Seek medical care if fever is very high or persistent."
            },

            "cough": {
                "info": "Cough can result from infection, irritation, or respiratory conditions.",
                "action": "Monitor symptoms and seek medical care if cough is severe or persistent."
            }

        }


    def process(self, message: str) -> str:

        message_lower = message.lower()

        for symptom, data in self.symptom_database.items():

            if symptom in message_lower:

                return (
                    "Aura Healthcare Intelligence:\n\n"
                    f"Detected symptom: {symptom}\n\n"
                    f"Information:\n{data['info']}\n\n"
                    f"Recommended action:\n{data['action']}\n\n"
                    "This information is for educational purposes only and is not medical advice."
                )

        return (
            "Aura Healthcare Intelligence:\n\n"
            "No specific symptom detected.\n\n"
            "Please consult a licensed healthcare professional for medical advice."
        )
