# agent_manager.py

from code_quality_agent import CodeQualityAgent

class AgentManager:
    def __init__(self):
        self.agents = {
            "quality": CodeQualityAgent(),
            # You can add more agents like performance, testing later.
        }

    def run_review_cycle(self, code: str, max_iterations: int = 2):
        """
        Run recursive plan → act → reflect loop using the Code Quality Agent.
        """
        current_code = code
        history = []

        for i in range(max_iterations):
            print(f"\n🔁 Iteration {i + 1}")
            analysis = self.agents["quality"].analyze(current_code)

            # Print the nicely formatted feedback from the agent
            print(analysis.get("formatted_feedback", "No feedback available."))

            history.append(analysis)

            # For now, just run one iteration for simplicity
            break

        return history
