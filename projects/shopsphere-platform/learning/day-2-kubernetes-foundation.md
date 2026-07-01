# Day 2 - Kubernetes Foundation Notes

## Project
ShopSphere Marketplace

---

## 1. Kubernetes Context

kubectl connects to a specific cluster.

Check:

kubectl config get-contexts

Switch:

kubectl config use-context rancher-desktop

Important:
Always check context before applying YAML.

---

## 2. Namespace

Namespace separates workloads inside a cluster.

Created:

shopsphere-dev

Structure:

Cluster
 |
 └── shopsphere-dev
        |
        └── applications

---

## 3. Deployment vs StatefulSet

Deployment:
- For stateless apps
- Pods can be replaced anytime

Examples:
- frontend
- api-gateway
- services


StatefulSet:
- For databases/stateful apps
- Stable pod names
- Stable storage

Example:

postgres-0

---

## 4. Storage in Kubernetes

Pods are temporary.

Database needs persistent storage.

Flow:

PostgreSQL
    |
    v
Pod
    |
    v
PVC
    |
    v
PV
    |
    v
StorageClass


PVC = storage request

PV = actual storage

StorageClass = creates storage automatically

---

## 5. PostgreSQL Deployment

Created:

StatefulSet:
postgres

Pod:
postgres-0

Service:
postgres-service

Storage:
postgres-data-postgres-0


Flow:

App
 |
 v
postgres-service
 |
 v
postgres-0
 |
 v
PVC

---

## 6. Service

Pods get new IPs after restart.

Service provides stable DNS.

Example:

postgres-service

Applications connect using service name.

---

## 7. ConfigMap

Stores normal configuration.

Example:

POSTGRES_PORT=5432


---

## 8. Secret

Stores sensitive values.

Example:

username
password
database name


---

## 9. Kustomize

Used to organize Kubernetes YAML.

Apply:

kubectl apply -k kubernetes/base


---

## Commands Learned

kubectl get nodes

kubectl get ns

kubectl get pods -n shopsphere-dev

kubectl get pvc -n shopsphere-dev

kubectl get all -n shopsphere-dev

kubectl exec -it postgres-0 -n shopsphere-dev -- bash


---

## Day 2 Completed

✅ Namespace  
✅ StatefulSet  
✅ PostgreSQL  
✅ PVC/PV storage  
✅ Service discovery  
✅ Kustomize basics  


Next:
- Test PostgreSQL persistence
- Deploy MinIO
- Start microservices