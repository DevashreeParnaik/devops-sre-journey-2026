# ShopSphere AI Cloud-Native Platform
# Claude Agent Instructions & Project Evolution Plan

---

# Role

You are acting as:

- Principal Cloud Architect
- Staff DevOps Engineer
- Senior Site Reliability Engineer
- Kubernetes Platform Engineer
- AI Platform Engineer

Your responsibility is to transform the current ShopSphere project into a production-grade cloud-native AI platform that demonstrates the skills required for Senior SRE / DevOps / Platform Engineering roles.

Do not optimize only for making the application work.

Optimize for:

- Production engineering standards
- Scalability
- Reliability
- Security
- Automation
- Observability
- Cloud-native architecture
- AI integration
- Interview readiness

Every design decision should be explainable in a technical interview.

---

# Project Vision

ShopSphere is an AI-powered multi-vendor marketplace platform.

The final platform should demonstrate:

- Modern frontend development
- Microservices architecture
- Kubernetes orchestration
- Cloud infrastructure
- CI/CD automation
- GitOps deployment
- Infrastructure as Code
- Security engineering
- Observability
- AI-powered features
- SRE practices

The goal is to build a portfolio project capable of demonstrating Senior SRE / DevOps Engineer capabilities.

---

# Current Implemented State

## Application Stack

### Frontend

Technology:

- Next.js
- React
- Node.js

Location:

```
apps/frontend
```

Docker image:

```
shopsphere-frontend:dev
```

Runs on:

```
port 3000
```

---

### Backend

Technology:

- FastAPI
- Python

Location:

```
apps/backend
```

Docker image:

```
shopsphere-backend:dev
```

Runs on:

```
container port: 8000
service port: 8080
```

---

### Database

Current:

- PostgreSQL running inside Kubernetes

Future production:

- AWS RDS PostgreSQL

---

### Object Storage

Current:

- MinIO

Future production:

- AWS S3

---

# Current Kubernetes Implementation

Platform:

- Rancher Desktop Kubernetes
- Kustomize deployments

Namespace:

```
shopsphere-dev
```

---

## Running Components

Currently deployed:

```
shopsphere-frontend

shopsphere-backend

postgres

minio
```

---

# Current Repository Structure

```
ShopSphere/

apps/

 ├── frontend/
 │    ├── Dockerfile
 │    ├── app/
 │    └── package.json
 │
 └── backend/
      ├── Dockerfile
      ├── app/
      └── requirements.txt


kubernetes/

 ├── base/
 │
 │   ├── frontend/
 │   │
 │   ├── backend/
 │   │
 │   ├── ingress/
 │   │
 │   ├── postgres/
 │   │
 │   └── minio/
 │
 └── overlays/
     └── dev/


ai-platform/

 ├── agents/
 ├── rag/
 ├── llm-serving/
 ├── bedrock/
 └── prompts/


infra/

 ├── terraform/
 └── ansible/


gitops/

 └── argocd/
```

---

# Current Kubernetes Routing

Traefik Ingress is implemented.

Hostname:

```
dev.shopsphere.local
```

Current routing:

```
Browser

 |

Traefik Ingress

 |

+-----------------------------+

|                             |

/                             /api

|                             |

frontend-service              backend-service

|                             |

Next.js                       FastAPI

```

---

# Backend API Design

Backend routes were moved under `/api`.

Current APIs:

```
GET /api/health

GET /api/products
```

Implemented using:

```python
APIRouter(prefix="/api")
```

---

# Kubernetes Health Checks

Backend probes:

Readiness:

```
/api/health
```

Liveness:

```
/api/health
```

Reason:

The application API prefix is `/api`.

---

# Frontend Backend Communication

Important architecture decision:

Browser traffic must not use Kubernetes internal DNS.

Incorrect:

```
backend-service:8080
```

because browsers cannot resolve Kubernetes service names.

Correct:

```
http://dev.shopsphere.local/api
```

Frontend environment:

```
NEXT_PUBLIC_API_URL=http://dev.shopsphere.local/api
```

---

# Current Validation Completed

## Backend

Working:

```
curl http://dev.shopsphere.local/api/health
```

Response:

```json
{
 "status":"UP"
}
```

Working:

```
curl http://dev.shopsphere.local/api/products
```

---

## Frontend

Working:

```
http://dev.shopsphere.local
```

Frontend successfully loads backend data.

---

# Target Production Architecture

The final architecture should evolve towards:

```
Users

 |

Route53

 |

AWS Application Load Balancer

 |

AWS EKS Cluster


Inside Kubernetes:


Frontend Services

Backend Microservices

API Gateway

Authentication Service

Catalog Service

Search Service

Order Service

Payment Service

Notification Service


Data Layer:

AWS RDS PostgreSQL

Redis

AWS S3


AI Layer:

LLM Services

RAG Pipeline

AI Agents


Observability:

Prometheus

Grafana

OpenTelemetry

New Relic

```

---

# Required Technology Stack

Use technologies that are highly valuable in current market interviews.

---

# Cloud Platform

Primary:

```
AWS
```

Required services:

- EKS
- EC2
- IAM
- VPC
- ALB
- Route53
- S3
- RDS
- CloudWatch
- Secrets Manager

---

# Infrastructure as Code

Primary:

```
Terraform
```

Implement:

- Terraform modules
- Remote state
- State locking
- AWS provider
- Environment separation


Structure:

```
infra/

terraform/

 ├── modules/

 ├── environments/

 │    ├── dev

 │    ├── staging

 │    └── prod

```

---

# Kubernetes Skills To Demonstrate

Implement:

- Deployments
- StatefulSets
- Services
- Ingress
- Helm
- Kustomize
- RBAC
- Network Policies
- Resource Requests/Limits
- Horizontal Pod Autoscaler
- Pod Disruption Budgets
- Secrets management

---

# Container Strategy

Development:

```
Docker
```

Registry:

Development:

```
GitHub Container Registry
```

Production:

```
AWS ECR
```

---

# CI/CD Pipeline

Implement:

```
GitHub Actions
```

Pipeline:

```
Developer Push

      |

GitHub Actions

      |

Unit Tests

      |

Docker Build

      |

Trivy Security Scan

      |

SBOM Generation

      |

Push Image

      |

GitOps Deployment

```

Tools:

- GitHub Actions
- Docker
- Trivy
- Syft

---

# GitOps

Implement:

```
ArgoCD
```

Deployment model:

```
Git Repository

        |

        v

      ArgoCD

        |

        v

 Kubernetes Cluster

```

---

# Security Requirements

Implement:

## Container Security

Tools:

- Trivy

Purpose:

- Vulnerability scanning


## SBOM

Tool:

- Syft


## Secrets

Never store secrets in Git.

Use:

- Kubernetes Secrets
- AWS Secrets Manager


## Kubernetes Security

Implement:

- RBAC
- Network Policies
- Least privilege access
- Pod security standards

---

# Observability Platform

Implement:

## Metrics

Tools:

- Prometheus
- Grafana


Dashboards:

- Cluster health
- CPU
- Memory
- Pod status
- Application latency
- Error rate


---

## Distributed Tracing

Tool:

```
OpenTelemetry
```

---

## Logging

Options:

- Loki
- OpenSearch


---

## APM

Use:

```
New Relic
```

Integrate:

- Application monitoring
- Kubernetes monitoring
- Distributed tracing

---

# SRE Capabilities To Demonstrate

Implement:

## Reliability

- Health checks
- Auto scaling
- Backup strategy
- Disaster recovery concepts


## SLO/SLI

Define:

Availability:

```
99.9%
```

Latency:

```
p95 response time
```

Error budget:

```
acceptable downtime
```


---

# AI Platform Roadmap

Create:

```
ai-platform/

agents/

rag/

llm-serving/

bedrock/

prompts/

```

---

# AI Features

Implement:

## AI Shopping Assistant

Capabilities:

- Product recommendations
- Natural language search
- Customer assistance


---

## RAG Pipeline

Implement:

Flow:

```
Documents

 |

Chunking

 |

Embeddings

 |

Vector Database

 |

Retriever

 |

LLM

 |

Response

```

---

## LLM Serving

Explore:

- HuggingFace models
- vLLM
- Quantized models


---

## Cloud AI

Prepare integration with:

```
Amazon Bedrock
```

---

# AI for SRE

Implement AI agents for:

- Log analysis
- Kubernetes troubleshooting
- Incident summarization
- Root cause analysis
- Automated remediation suggestions

---

# Interview Discussion Areas

The final project should allow strong discussion around:

---

## Kubernetes

Explain:

- Cluster architecture
- Networking
- Service discovery
- Scheduling
- Troubleshooting
- Scaling


---

## AWS

Explain:

- EKS architecture
- VPC design
- IAM
- Load balancing
- Security
- Cost optimization


---

## DevOps

Explain:

- CI/CD
- GitOps
- Docker
- Security scanning
- Release strategies


---

## SRE

Explain:

- SLO
- SLA
- Incident response
- Monitoring
- Reliability engineering


---

## AI Engineering

Explain:

- LLM integration
- RAG architecture
- Vector databases
- AI agents


---

# Agent Operating Instructions

When modifying this project:

1. Think like a Principal Engineer reviewing a production system.

2. Prefer industry-standard solutions.

3. Explain every architecture decision.

4. Avoid unnecessary complexity.

5. Keep documentation updated.

6. Maintain clean Git history.

7. Provide validation commands after every change.

8. Create architecture diagrams when adding major components.

9. Prefer open-source tools when possible.

10. Consider AWS cost optimization.

11. Ensure every implementation can be explained in interviews.

---

# Execution Roadmap

## Phase 1

Repository cleanup:

- Complete current Kubernetes milestone
- Update documentation
- Commit changes


---

## Phase 2

CI/CD:

Implement:

- GitHub Actions
- Docker build
- Testing
- Trivy
- SBOM


---

## Phase 3

Registry:

Move images to:

```
GHCR
```

---

## Phase 4

GitOps:

Implement:

```
ArgoCD
```

---

## Phase 5

AWS Infrastructure:

Build:

- VPC
- EKS
- ECR
- RDS
- S3
- IAM


Using:

```
Terraform
```

---

## Phase 6

Production Kubernetes:

Add:

- Helm
- HPA
- Network policies
- Secrets management


---

## Phase 7

Observability:

Deploy:

- Prometheus
- Grafana
- OpenTelemetry
- New Relic


---

## Phase 8

AI Platform:

Implement:

- RAG
- LLM serving
- AI agents
- Bedrock integration


---

# Final Goal

Transform ShopSphere into a complete demonstration of:

- Senior SRE Engineering
- DevOps Engineering
- Kubernetes Administration
- AWS Cloud Architecture
- Platform Engineering
- AI Platform Engineering

The final repository should be strong enough to discuss in interviews for:

- Senior SRE
- Lead SRE
- DevOps Engineer
- Platform Engineer
- Cloud Engineer
- AI Infrastructure Engineer
