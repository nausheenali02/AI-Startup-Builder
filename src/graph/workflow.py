from langgraph.graph import StateGraph, START, END
from src.graph.state import StartupBuilderState


def manager_node(state: StartupBuilderState) -> dict:
    return {
        "execution_trace": ["Manager: Analyzed user idea and formed research plan."]
    }


def market_research_node(state: StartupBuilderState) -> dict:
    return {
        "execution_trace": ["Market Agent: Trends and industry size fetched."]
    }


def competitor_node(state: StartupBuilderState) -> dict:
    return {
        "execution_trace": ["Competitor Agent: Benchmarked 3 top rivals."]
    }


def product_node(state: StartupBuilderState) -> dict:
    return {
        "execution_trace": ["Product Agent: Scoped MVP user stories."]
    }


def critic_node(state: StartupBuilderState) -> dict:
    return {
        "execution_trace": ["Critic Agent: Evaluated feasibility and citations."]
    }


def build_test_graph():
    builder = StateGraph(StartupBuilderState)

    builder.add_node("manager", manager_node)
    builder.add_node("market_research", market_research_node)
    builder.add_node("competitor_research", competitor_node)
    builder.add_node("product_scoping", product_node)
    builder.add_node("critic", critic_node)

    # Workflow edges: Manager triggers research in parallel
    builder.add_edge(START, "manager")
    builder.add_edge("manager", "market_research")
    builder.add_edge("manager", "competitor_research")

    # Research merges into product scoping
    builder.add_edge("market_research", "product_scoping")
    builder.add_edge("competitor_research", "product_scoping")

    # Scoping moves to Critic, then ends
    builder.add_edge("product_scoping", "critic")
    builder.add_edge("critic", END)

    return builder.compile()