from typing import Annotated, List, Optional
from typing_extensions import TypedDict
import operator

from src.schemas.models import (
    ResearchPlan,
    MarketAnalysis,
    CompetitorProfile,
    CustomerPersona,
    ProductScope,
    BusinessModel,
    TechArchitecture,
    CritiqueFeedback,
)


class StartupBuilderState(TypedDict):
    # User Input
    user_idea: str
    target_geography: Optional[str]
    budget_constraint: Optional[str]

    # Orchestrator Deliverable
    research_plan: Optional[ResearchPlan]

    # Parallel Research Deliverables
    market_research: Optional[MarketAnalysis]
    competitors: Optional[List[CompetitorProfile]]
    customer_personas: Optional[List[CustomerPersona]]

    # Downstream Synthesis
    product_scope: Optional[ProductScope]
    business_model: Optional[BusinessModel]
    tech_architecture: Optional[TechArchitecture]

    # Quality Gate & Critique
    critique: Optional[CritiqueFeedback]
    revision_count: int

    # Final Output
    final_blueprint_markdown: Optional[str]

    # Audit Trail: node execution logs appended in sequence
    execution_trace: Annotated[List[str], operator.add]