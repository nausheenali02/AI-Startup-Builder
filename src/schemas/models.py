from typing import List, Optional
from pydantic import BaseModel, Field


class EvidenceSource(BaseModel):
    title: str = Field(description="Title of the source or article")
    url: str = Field(description="URL link to the source")
    snippet: str = Field(description="Relevant factual extract or snippet")
    reliability_score: float = Field(
        default=0.8, description="Estimated reliability between 0.0 and 1.0"
    )
    published_date: Optional[str] = Field(
        default=None, description="Publish date if available"
    )


class ResearchPlan(BaseModel):
    core_problem: str = Field(description="Refined summary of the problem being solved")
    target_hypothesis: str = Field(description="Primary initial target customer segment")
    key_assumptions: List[str] = Field(
        description="Assumptions that require factual validation"
    )
    search_queries: List[str] = Field(
        description="Targeted search queries for evidence gathering"
    )


class CompetitorProfile(BaseModel):
    name: str = Field(description="Company or tool name")
    key_features: List[str] = Field(description="Core feature offerings")
    pricing_model: Optional[str] = Field(
        default=None, description="Known pricing structure"
    )
    weaknesses: List[str] = Field(
        description="Identified user complaints or operational gaps"
    )
    citations: List[str] = Field(
        default_factory=list, description="URLs backing competitor claims"
    )


class MarketAnalysis(BaseModel):
    market_size_narrative: str = Field(
        description="Market opportunity context (TAM/SAM/SOM breakdown)"
    )
    key_trends: List[str] = Field(description="Industry trends driving adoption")
    regulatory_risks: List[str] = Field(
        description="Legal, compliance, or regulatory hurdles"
    )
    citations: List[EvidenceSource] = Field(
        default_factory=list, description="Grounding evidence sources"
    )


class CustomerPersona(BaseModel):
    persona_title: str = Field(
        description="e.g., Independent Restaurant Owner, Kitchen Manager"
    )
    core_pain_points: List[str] = Field(
        description="Specific everyday operational frustrations"
    )
    willingness_to_pay_drivers: List[str] = Field(
        description="What direct value triggers budget spend"
    )
    citations: List[str] = Field(
        default_factory=list, description="Direct quotes or forum/article URLs"
    )


class UserStory(BaseModel):
    role: str = Field(description="As a [role]")
    action: str = Field(description="I want to [action]")
    benefit: str = Field(description="So that [business outcome]")
    acceptance_criteria: List[str] = Field(
        description="Conditions verifying completion"
    )
    priority: str = Field(description="Must Have, Should Have, or Nice to Have")


class ProductScope(BaseModel):
    mvp_description: str = Field(description="High-level definition of the minimum viable product")
    features: List[UserStory] = Field(
        description="Prioritized features mapped into user stories"
    )
    out_of_scope: List[str] = Field(
        description="Explicitly deprioritized features for v1"
    )


class BusinessModel(BaseModel):
    revenue_streams: List[str] = Field(description="Pricing models and revenue streams")
    pricing_hypotheses: List[str] = Field(
        description="Estimated pricing tiers with rationale"
    )
    go_to_market_channels: List[str] = Field(
        description="Primary customer acquisition tactics"
    )
    facts: List[str] = Field(description="Claims directly backed by market evidence")
    assumptions: List[str] = Field(
        description="Hypotheses requiring real-world validation"
    )


class TechArchitecture(BaseModel):
    system_overview: str = Field(description="Architectural pattern summary")
    frontend_stack: str = Field(description="Recommended UI technologies")
    backend_stack: str = Field(description="Recommended APIs, services, and language")
    database_design: str = Field(description="Schema model and primary persistence")
    ai_ml_pipeline: str = Field(
        description="Model choices, orchestration, latency, and context strategy"
    )
    key_apis: List[str] = Field(description="External third-party API dependencies")


class CritiqueFeedback(BaseModel):
    is_approved: bool = Field(
        description="Whether the blueprint meets standards without critical flaws"
    )
    critique_score: int = Field(
        description="Overall blueprint score out of 100"
    )
    unsupported_claims: List[str] = Field(
        default_factory=list, description="Claims lacking citation or market grounding"
    )
    scope_creep_warnings: List[str] = Field(
        default_factory=list, description="Areas where the MVP is oversized"
    )
    recommended_revisions: List[str] = Field(
        default_factory=list, description="Specific feedback points for targeted agents"
    )