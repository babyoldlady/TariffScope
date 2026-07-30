# TariffScope

TariffScope is a cloud-native tariff search and monitoring platform for U.S. crude oil and refined products pipelines.

It helps users search tariffs by:
- Issuer
- Tariff Type
- Rates
- Rules and Regulations
- Tariff Index
- Origin
- Destination
- Product Type
- Regulator
- Tariff Number
- Status
- Effective Yes/No
- Company Contact Information

## MVP
- Ingest tariff data from FERC and operator sources
- Store normalized tariff records
- Search tariffs through a REST API
- Display operator index views
- Support basic subscriptions and alerts
- Optionally classify tariff text using TensorFlow/Vertex AI

## Tech Stack
- Python / FastAPI
- PostgreSQL
- Docker
- Cloud Run
- Kubernetes YAML
- TensorFlow
- Vertex AI
- VPC / IAM / Secret Manager
- HTML / JavaScript frontend

## Project Goals
- Reduce manual tariff search time
- Improve tariff monitoring and change awareness
- Demonstrate modern cloud deployment and applied ML

## Local Run
1. Copy `.env.example` to `.env`
2. Run database and app locally
3. Start ingestion and API services

## Deployment
See `docs/deployment_guide.md`
