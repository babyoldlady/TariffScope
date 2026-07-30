from datetime import datetime
import uuid

from sqlalchemy import Boolean, Column, DateTime, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TariffRecord(Base):
    __tablename__ = "tariff_records"

    tariff_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    issuer = Column(String, index=True, nullable=True)
    tariff_no = Column(String, index=True, nullable=True)
    tariff_type = Column(String, index=True, nullable=True)
    product_type = Column(String, index=True, nullable=True)
    origin = Column(String, index=True, nullable=True)
    destination = Column(String, index=True, nullable=True)
    regulator = Column(String, index=True, nullable=True)
    status = Column(String, index=True, nullable=True)
    effective_yes_no = Column(Boolean, default=False)
    effective_date = Column(String, nullable=True)
    filed_date = Column(String, nullable=True)
    rate_text = Column(Text, nullable=True)
    rules_text = Column(Text, nullable=True)
    tariff_index_text = Column(Text, nullable=True)
    company_contact_name = Column(String, nullable=True)
    company_contact_email = Column(String, nullable=True)
    company_contact_phone = Column(String, nullable=True)
    source_url = Column(String, nullable=True)
    source_system = Column(String, nullable=True)
    last_updated_at = Column(DateTime, default=datetime.utcnow)


class Subscription(Base):
    __tablename__ = "subscriptions"

    subscription_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    issuer = Column(String, index=True, nullable=False)
    email = Column(String, nullable=True)
    tariff_type = Column(String, nullable=True)
    product_type = Column(String, nullable=True)
    state = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class TariffVersion(Base):
    __tablename__ = "tariff_versions"

    version_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tariff_id = Column(String, index=True, nullable=False)
    payload_json = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
