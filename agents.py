class Agent:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def describe(self):
        return {
            "name": self.name,
            "specialty": self.specialty
        }


class AgentManager:
    def __init__(self):
        self.agents = [
            Agent("Researcher", "Investigación"),
            Agent("Programmer", "Programación"),
            Agent("Analyst", "Análisis"),
            Agent("Reviewer", "Verificación")
        ]

    def list_agents(self):
        return [
            agent.describe()
            for agent in self.agents
        ]


if __name__ == "__main__":
    manager = AgentManager()

    for agent in manager.list_agents():
        print(agent["name"], "-", agent["specialty"])
