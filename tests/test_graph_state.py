import sys
from pathlib import Path

# Ensure root directory is on the import path
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.graph.workflow import build_test_graph


def test_skeleton_graph():
    graph = build_test_graph()

    initial_state = {
        "user_idea": "AI food waste reduction platform for small restaurants",
        "target_geography": "North America",
        "budget_constraint": "Lean MVP",
        "research_plan": None,
        "market_research": None,
        "competitors": None,
        "customer_personas": None,
        "product_scope": None,
        "business_model": None,
        "tech_architecture": None,
        "critique": None,
        "revision_count": 0,
        "final_blueprint_markdown": None,
        "execution_trace": [],
    }

    result = graph.invoke(initial_state)

    print("\n--- SKELETON EXECUTION TRACE ---")
    for log in result["execution_trace"]:
        print(f" -> {log}")

    assert len(result["execution_trace"]) == 5
    print("\n[OK] StateGraph compiled and resolved parallel routes successfully!")


if __name__ == "__main__":
    test_skeleton_graph()