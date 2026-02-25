class VectorEngine:

    def embed(self, text: str):

        vector = [

            float(ord(char)) / 1000

            for char in text[:128]

        ]

        return vector


vector_engine = VectorEngine()
