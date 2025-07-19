from code_quality_agent import CodeQualityAgent

def print_review_result(result: dict):
    print(result.get("formatted_feedback", "").strip())

if __name__ == "__main__":
    agent = CodeQualityAgent()
    sample_code = """
def greet(name):
    print("Hello " + name)
    print("Bye" + name)
"""
    result = agent.analyze(sample_code)
    print_review_result(result)
