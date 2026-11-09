import json
import os
from datetime import datetime


class SharedMemory:

    def __init__(self, filename="centro_memory.json"):
        self.filename = filename
        self.data = self.load()

    def load(self):
        if not os.path.exists(self.filename):
            return {"history": []}

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {"history": []}

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                self.data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def add(self, role, message):
        entry = {
            "role": role,
            "message": message,
            "date": datetime.now().isoformat()
        }

        self.data["history"].append(entry)
        self.save()

    def get_history(self):
        return self.data["history"]

    def clear(self):
        self.data = {"history": []}
        self.save()


if __name__ == "__main__":
    memory = SharedMemory()

    memory.add(
        "system",
        "CENTRO IA 1.0 iniciado"
    )

    print("Memoria compartida funcionando")
    print("Registros:", len(memory.get_history()))
