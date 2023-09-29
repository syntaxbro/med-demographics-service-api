from dataclasses import dataclass
from ..configuration.config import TEST_PATIENT_ID
import re


@dataclass
class Update:
    nhs_number: str
    operation: str = 'replace'
    path: str = 'gender'
    _record: dict = None
    _value: str = None
    _etag: str = None

    @property
    def patches(self) -> dict:
        patch = {
            "op": f"{self.operation}",
            "path": f"/{self.path}",
            "value": f"{self.value}"
        }
        return {"patches": [patch]}

    @property
    def record(self):
        return self._record

    @property
    def value(self):
        return self._value

    @property
    def record_version(self):
        return re.findall(r'\d+', self.etag)[0]

    @property
    def etag(self):
        return self._etag

    @record.setter
    def record(self, value: dict) -> None:
        self._record = value

    def add_gender_value(self, value: str) -> None:
        self.patches[0].update({"value": value})

    @value.setter
    def value(self, v: str) -> None:
        self._value = v

    @etag.setter
    def etag(self, value: str) -> None:
        self._etag = value


DEFAULT = Update(nhs_number=TEST_PATIENT_ID)
