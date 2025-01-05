# Order Assignment Service

A service for order management that provides data storage for orders and interaction with external systems.

The system ensures high availability, scalability, reliability, and idempotent operations.

### ADR

[Link to ADR Document](https://docs.google.com/document/d/1qEkNfho60Py_Mx6pEOZr7hfJvXBQWhewGb_JW94Z9rQ/edit?tab=t.0#heading=h.t5vg7sgbcah8)

### Testing Report

[Link to Testing Report](https://docs.google.com/document/d/17D4DBvhsImV1VAVdIxyg2qNOMZAOoQz03aoStYgdBlo/edit?usp=sharing)

### How to Send Requests?

```
curl -X POST http://localhost:8000/assign-order/ -H "Content-Type: application/json" -d '{"order_id": "order123", "executer_id": "executer456", "locale": "en-US"}'

curl -X POST http://localhost:8000/acquire-order/ -H "Content-Type: application/json" -d '{"executer_id": "executer456"}'

curl -X POST http://localhost:8000/cancel-order/ -H "Content-Type: application/json" -d '{"order_id": "order123"}'
```
