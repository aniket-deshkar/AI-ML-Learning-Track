from __future__ import annotations

try:
    from .engine import DocumentProcessingEngine
except ImportError:
    # Support LangGraph file-based loading: ./doc_pipeline/graph.py:agent
    from doc_pipeline.engine import DocumentProcessingEngine


def create_graph():
    """Factory for LangGraph CLI / Agent Server."""
    return DocumentProcessingEngine().graph


agent = create_graph()
