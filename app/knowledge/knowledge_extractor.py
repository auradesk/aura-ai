import re


def extract_fact(message):

    message_lower = message.lower()


    patterns = [

        ("favorite_food", r"my favorite food is (.+)"),
        ("favorite_color", r"my favorite color is (.+)"),
        ("name", r"my name is (.+)"),
        ("age", r"i am (\d+) years old")

    ]


    for fact_type, pattern in patterns:

        match = re.search(pattern, message_lower)

        if match:

            fact_value = match.group(1).strip()

            return fact_type, fact_value


    return None, None
