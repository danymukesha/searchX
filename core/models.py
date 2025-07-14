from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class SequenceType(str, Enum):
    DNA = "DNA"
    RNA = "RNA"
    PROTEIN = "Protein"

class Sequence(BaseModel):
    id: str = Field(..., description="Unique identifier")
    seq: str = Field(..., min_length=10, description="Biological sequence")
    type: SequenceType
    organism: str
    annotations: Dict[str, List[tuple]] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ClinicalVariant(BaseModel):
    chrom: str
    pos: int
    ref: str
    alt: str
    significance: Optional[str] = None  # ACMG classification
    evidence: List[Dict] = Field(default_factory=list)
