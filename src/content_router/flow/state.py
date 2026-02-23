from typing import Dict, Any
from pydantic import BaseModel

class ContentState(BaseModel):
    """
    State model that tracks information throughout the content creation workflow.
    """
    url: str = ""
    content_type: str = ""  
    final_content: str = ""  
    error: str = ""
    metadata: Dict[str, Any] = {}
