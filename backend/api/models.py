from sqlalchemy import Column, String, Boolean, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class TariffRecord(Base):
    __tablename__ = "tariff_records"

    tariff_id = Column(String, primary_key=True, index=True)
    issuer = Column(String, index=True)
    tariff_no = Column(String, index=True)
    tariff_type = Column(String, index=True)
    product_type = Column(String, index=True)
    origin = Column(String, index=True)
    destination = Column(String, index=True)
    regulator = Column(String, index=True)
    status = Column(String, index=True)
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
