# -*- coding: utf-8 -*-

"""
    Python file which contains an error type

"""
import json
from dataclasses import dataclass


@dataclass
class NetError:
    error_code: int
    reason: str
    entity_id: str

    def __str__(self):
        data: dict = {
            "error_code": self.error_code,
            "reason": self.reason,
            "entity_id": self.entity_id,
        }

        return json.dumps(data)
