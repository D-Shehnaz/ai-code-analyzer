from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Finding:
    type: str
    severity: str
    message: str
    line: Optional[int] = None
    source: str = "static"


@dataclass
class AnalysisResult:
    language: str
    severity_score: int
    critical_bugs: List[Finding]
    warnings: List[Finding]
    fixed_code: str