"""
TradingAgents - A multi-agent framework for AI-driven trading analysis.

This package provides a collection of specialized AI agents that collaborate
to analyze financial markets, process news, and generate trading signals.

Fork of TauricResearch/TradingAgents with enterprise enhancements.
"""

__version__ = "0.1.0"
__author__ = "TradingAgents Contributors"
__license__ = "Apache-2.0"

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

__all__ = [
    "TradingAgentsGraph",
    "DEFAULT_CONFIG",
    "__version__",
]
