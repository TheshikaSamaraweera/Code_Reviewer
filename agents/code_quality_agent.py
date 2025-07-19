import re
from llm_client import LLMClient  # Make sure llm_client.py exists and works properly

class CodeQualityAgent:
    """
    This class interfaces with a language model to evaluate the quality of Python code.
    """

    def __init__(self, model_name="gemini-2.0-flash"):
        """
        Initialize the agent with the specified LLM model.
        """
        self.llm = LLMClient(model_name)

    def format_prompt(self, code: str) -> str:
        """
        Construct a detailed prompt asking the LLM to evaluate the code.

        Args:
            code (str): The source code to analyze.

        Returns:
            str: A formatted prompt for the LLM.
        """
        return f"""
You are a senior software engineer AI assistant. 
Analyze the following Python code and provide a code review in the following format:

1. 📋 Issues: List specific problems or anti-patterns found.
2. 🔥 Severity: Mark each issue as LOW, MEDIUM, or HIGH.
3. 💡 Suggestions: Improvements or refactoring ideas for each issue.
4. ✅ Summary: A brief overall quality assessment.
5. ⭐ Rating: A score between 1 (poor) to 10 (excellent).

Code to review:
{code}

Respond in a structured format.
"""

    def parse_response(self, response: str) -> dict:
        """
        Parse the LLM response into a structured dictionary.

        Args:
            response (str): The raw text response from the LLM.

        Returns:
            dict: Parsed results including a formatted feedback string.
        """
        sections = {
            'issues': r'1\. 📋 Issues:(.*?)2\. 🔥 Severity:',
            'severity': r'2\. 🔥 Severity:(.*?)3\. 💡 Suggestions:',
            'suggestions': r'3\. 💡 Suggestions:(.*?)4\. ✅ Summary:',
            'summary': r'4\. ✅ Summary:(.*?)5\. ⭐ Rating:',
            'rating': r'5\. ⭐ Rating:(.*)',
        }

        result = {}
        for key, pattern in sections.items():
            match = re.search(pattern, response, re.DOTALL)
            result[key] = match.group(1).strip() if match else "Not found"

        # Add the full raw response as formatted feedback for easy printing
        result["formatted_feedback"] = response.strip()

        return result

    def analyze(self, code: str) -> dict:
        """
        Send code to the LLM and return the analysis result.

        Args:
            code (str): The Python code to analyze.

        Returns:
            dict: Parsed analysis results including formatted feedback.
        """
        prompt = self.format_prompt(code)
        response = self.llm.send_prompt(prompt)

        print("\n🧾 Raw LLM Response:\n", response)  # Useful for debugging

        return self.parse_response(response)
