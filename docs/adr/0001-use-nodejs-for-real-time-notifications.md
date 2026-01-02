# ADR 0001: Use Node.js for Real-Time Notifications

## Status
Accepted

## Context 
The application requires a real-time notification system to deliver instant updates to users (e.g., status changes, alerts, or messages). These notifications require long-lived WebSocket connections and must support a large number of concurrent clients.

The existing backend is implemented as a Django monolith, which is well-suited for data-driven CRUD operations and business logic. However, handling large-scale, long-lived WebSocket connections efficiently in Django can introduce additional complexity and resource overhead.

## Decision

A separate Node.js microservice will be introduced to handle real-time notifications using WebSockets. The Django monolith will remain responsible for core application logic, data persistence, and REST APIs. Communication between Django and the Node.js service will occur via HTTP or message-based events.

## Alternatives Considered

1. **Implement WebSockets using Django Channels**
 - Pros: Single codebase, no additional service to maintain
 - Cons: Increased complexity, higher resource usage per connection, and less optimal performance for high-concurrency real-time communication

2. **Use Node.js for the entire backend**
   - Pros: Unified runtime for all services
   - Cons: Loss of Django’s mature ORM, admin interface, and rapid development advantages for data-centric features

## Consequences

  - **Positive**
    - Improved performance and scalability for real-time features
    - Clear separation of concerns between core business logic and real-time communication
    - Ability to scale the notification service independently

  - **Negative**
    - Increased architectural complexity due to an additional service
    - Need for inter-service communication and monitoring


