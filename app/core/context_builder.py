from app.config.settings import settings
from app.mcp.search_tool import SearchTool

class ContextBuilder:
    def __init__(self) -> None:
        self.search_tool = SearchTool()

    def build(self, query: str) -> str:
        search_results = self.search_tool.search(
            query,
            settings.PROJECT_ROOT,
        )

        return f"""
Relevant repository matches:

{search_results}
"""