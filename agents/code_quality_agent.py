# code_quality_agent.py

from llm_client import LLMClient  # You’ll create this file next

class CodeQualityAgent:
    def __init__(self, model_name="gemini-2.0-flash"):
        self.llm = LLMClient(model_name)

    def format_prompt(self, code: str) -> str:
        """
        Constructs a detailed prompt asking the LLM to evaluate the code.
        """
        prompt = f"""
You are a senior software engineer AI assistant. 
Analyze the following Python code and provide a code review with the following format:

1. 📋 Issues: List specific problems or anti-patterns found.
2. 🔥 Severity: Mark each issue as LOW, MEDIUM, or HIGH.
3. 💡 Suggestions: Improvements or refactoring ideas for each issue.
4. ✅ Summary: A brief overall quality assessment.
5. ⭐ Rating: A score between 1 (poor) to 10 (excellent).

Code to review: {code}



Respond in a structured format.
"""
        return prompt

    def parse_response(self, response: str) -> dict:
        """
        Temporary placeholder: just returns the raw response inside a dict.
        """
        return {"raw_response": response}

    def analyze(self, code: str) -> dict:
        """
        Complete analysis pipeline: prompt හදා → LLM ට යව → response parse → return.
        """
        prompt = self.format_prompt(code)
        response = self.llm.send_prompt(prompt)
        result = self.parse_response(response)
        return result
