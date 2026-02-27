from datetime import datetime, timezone
from sqlalchemy import Column, DateTime


class TimestampMixin:
    """adds timezone-aware timestamps and touch helper."""
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    discarded_at = Column(DateTime(timezone=True), nullable=True)

    def touch(self):
        """
            Manually update the updated_at timestamp. Useful for marking a record as updated without changing any other fields.
        """
        self.updated_at = datetime.now(timezone.utc)
