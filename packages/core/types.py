from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class Policy:
    name: str
    func: callable

@dataclass
class Anomaly:
    name: str
    description: str

PolicyList = List[Policy]
AnomalyList = List[Anomaly]
Data = Dict[str, Any]