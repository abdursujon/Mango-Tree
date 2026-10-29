from typing import List 
from dataclasses import asdict, dataclass, field 

@dataclass
class MangoTree:
    id: int = field(default=None, compare=False)
    task: str = None
    expected_completion_time: str = None

    @classmethod
    def from_dict(cls, d):
        return MangoTree(**d)
    def to_dict(self):
        return asdict
     
    