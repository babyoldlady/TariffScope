from datetime import datetime, timezone
import uuid

from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TariffRecord(Base):
    __tablename__ = "tariff_records"

    tariff_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    issuer: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    tariff_no: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    tariff_type: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    product_type: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    origin: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    destination: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    regulator: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    status: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    effective_yes_no: Mapped[bool] = mapped_column(Boolean, default=False)
    effective_date: Mapped[str | None] = mapped_column(String, nullable=True)
    filed_date: Mapped[str | None] = mapped_column(String, nullable=True)
    rate_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    rules_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    tariff_index_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    company_contact_name: Mapped[str | None] = mapped_column(String, nullable=True)
    company_contact_email: Mapped[str | None] = mapped_column(String, nullable=True)
    company_contact_phone: Mapped[str | None] = mapped_column(String, nullable=True)
    source_url: Mapped[str | None] = mapped_column(String, nullable=True)
    source_system: Mapped[str | None] = mapped_column(String, nullable=True)
    last_updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
    )


class Subscription(Base):
    __tablename__ = "subscriptions"

    subscription_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    issuer: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)
    tariff_type: Mapped[str | None] = mapped_column(String, nullable=True)
    product_type: Mapped[str | None] = mapped_column(String, nullable=True)
    state: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
    )


class TariffVersion(Base):
    __tablename__ = "tariff_versions"

    version_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tariff_id: Mapped[str] = mapped_column(String, index=True)
    payload_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
    )
