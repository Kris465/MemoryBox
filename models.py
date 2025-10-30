from dataclasses import dataclass
from typing import List, Optional


@dataclass
class DocumentChunk:
    text: str
    source: str
    page: Optional[int] = None
    metadata: dict = None


@dataclass
class SearchResult:
    chunks: List[DocumentChunk]
    query: str
    total_found: int


@dataclass
class GenerationRequest:
    assignment: str
    topic: str
    context: str
    style: str = "academic"
