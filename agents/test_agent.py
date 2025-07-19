# test_agent.py

from code_quality_agent import CodeQualityAgent

if __name__ == "__main__":
    agent = CodeQualityAgent()
    code = """
def greet(name):
    print("Hello " + name)
    print("Bye" + name)
"""
    result = agent.analyze(code)
    print(result)
