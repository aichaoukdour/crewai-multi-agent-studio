from typing import Dict, Any
from pydantic import BaseModel

# 🧠 Define the memory for the Flow
# The state model, or memory, is like a shared notebook that all agents can read and write to.
# It persists data throughout the entire workflow execution.

class ContentState(BaseModel):
  """
  State model that tracks information throughout the content creation workflow.
  """
  url: str = ""
  content_type: str = ""  
  final_content: str = ""  
  error: str = ""
  metadata: Dict[str, Any] = {}
