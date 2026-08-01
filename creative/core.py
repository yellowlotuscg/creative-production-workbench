from dataclasses import dataclass, field
@dataclass
class Concept:
 title:str
 brief:str
 constraints:list[str]
 alt_text:str=""
 provenance:str=""
 status:str="draft"
 events:list[str]=field(default_factory=list)
def approve(concept):
 if not concept.alt_text or not concept.provenance: raise ValueError("accessibility and provenance are required")
 concept.status="approved"; concept.events.append("approved"); return concept
