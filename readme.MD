# Сервис Назначения Заказов

Сервис управления заказами, обеспечивающий хранение данных о заказах и взаимодействие с внешними системами. 

Система поддерживает высокую доступность, масштабируемость, надёжность и идемпотентность операций.

### ADR

https://docs.google.com/document/d/1qEkNfho60Py_Mx6pEOZr7hfJvXBQWhewGb_JW94Z9rQ/edit?tab=t.0#heading=h.t5vg7sgbcah8

### Как слать запросы?

```
curl -X POST http://localhost:8000/assign-order/ -H "Content-Type: application/json" -d '{"order_id": "order123", "executer_id": "executer456", "locale": "en-US"}'

curl -X POST http://localhost:8000/acquire-order/ -H "Content-Type: application/json" -d '{"executer_id": "executer456"}'

curl -X POST http://localhost:8000/cancel-order/ -H "Content-Type: application/json" -d '{"order_id": "order123"}'
```