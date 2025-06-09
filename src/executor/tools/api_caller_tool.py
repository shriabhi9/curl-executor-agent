import requests
from crewai.tools import BaseTool
from crewai.project import tool

@tool
class ApiCallerTool(BaseTool):
    name:str = "ApiCallerTool"
    description:str = "Executes an API request based on structured input and returns the response."

    def _run(self, request_data: dict) -> str:
        method = request_data.get("method", "GET").upper()
        url = request_data.get("url")
        headers = request_data.get("headers", {})
        data = request_data.get("data")

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=data if isinstance(data, dict) else None
            )
            return response.text
        except Exception as e:
            return f"API call failed: {str(e)}"
