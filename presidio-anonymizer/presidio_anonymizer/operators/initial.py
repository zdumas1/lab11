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
    def anonymize(self, value: str) -> str:
        if not value:
            return ""

        prefix = ""
        first_alnum_index = None

        for i, ch in enumerate(value):
            if ch.isalnum():
                first_alnum_index = i
                break
            else:
                prefix += ch

        if prefix.strip() != "":
        # Only return prefix + first alnum
            first = value[first_alnum_index].upper() if first_alnum_index is not None else ""
            return prefix + first + "."

        # MODE 2: no symbolic prefix → return initials of all words
        words = value.split()
        initials = [w[0].upper() + "." for w in words if w]
        return " ".join(initials)
