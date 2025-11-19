from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType
class Initial(Operator):
    """Redact the string - empty value."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: an empty value."""
        return ""

    def validate(self, params: Dict = None) -> None:
        """Redact does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
    def anonymize(self, text: str) -> str:
        # Remove leading/trailing/multiple spaces
        words = text.strip().split()
        initials = [word[0].upper() + "." for word in words]
        return " ".join(initials)
