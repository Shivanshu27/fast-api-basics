# FastAPI
# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. Some key features include:

# Performance: FastAPI is one of the fastest Python web frameworks available, thanks to its use of asynchronous programming with ASGI.
# Type Safety: It leverages Python type hints, providing better code completion and less debugging time.
# Automatic Documentation: FastAPI automatically generates interactive API documentation using Swagger UI and ReDoc.
# Dependency Injection: It has a powerful dependency injection system.
# Django
# Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Some key features include:

# Batteries-Included: Django comes with many built-in features such as an ORM, authentication, and an admin panel.
# Scalability: It is scalable and can handle high-traffic sites.
# Security: Django provides robust security features out-of-the-box, including protection against SQL injection, cross-site scripting, and cross-site request forgery.
# Community and Ecosystem: It has a large community and a vast ecosystem of reusable apps and plugins.
# Flask
# Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. Some key features include:

# Flexibility: Flask provides simplicity and flexibility, allowing developers to choose the components they need.
# Minimalism: It is lightweight and minimalistic, making it easy to start with and understand.
# Extensions: Flask has a rich ecosystem of extensions that can add functionality as needed.
# Learning Curve: It has a gentle learning curve and is suitable for beginners.
# Comparison and Use Cases
# Feature/Criteria	FastAPI	Django	Flask
# Performance	High (Asynchronous)	Moderate (Synchronous)	Moderate (Synchronous)
# Type Safety	Yes (Type Hints)	No	No
# Built-in Features	Minimal, API-focused	Extensive (ORM, Admin, Auth, etc.)	Minimal, Extendable
# Ease of Use	Moderate	Moderate to High	High
# Documentation	Automatic (Swagger, ReDoc)	Manual	Manual
# Community Support	Growing	Large	Large
# Best For	Modern APIs, Async Tasks	Full-fledged web applications	Simple applications, Prototypes
# Dependency Injection	Yes	No	No
# Scalability	High	High	High
# Security	Moderate (Customizable)	High (Built-in)	Moderate (Customizable)
# When to Use Which Framework
# FastAPI: Use FastAPI when you need to build high-performance APIs, especially if you need asynchronous capabilities and type safety. It's ideal for modern, fast, and scalable API development.

# Django: Use Django when you need a full-featured web application with built-in components like ORM, authentication, and an admin panel. It's suitable for large-scale applications that require rapid development and robust security.

# Flask: Use Flask when you need a lightweight and flexible framework for simple web applications or prototypes. It allows you to have more control over the components and architecture of your application.

# Each of these frameworks has its own strengths and is suitable for different use cases. The choice of framework depends on the specific requirements of your project.






# Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. It's designed to run Python web applications and frameworks that support the ASGI (Asynchronous Server Gateway Interface) standard, such as FastAPI.

# Key Features
# Performance: Uvicorn is built to be fast and efficient, leveraging uvloop (a high-performance event loop) and httptools for HTTP parsing.
# Asynchronous: Supports asynchronous programming using asyncio, making it suitable for handling concurrent requests.
# Flexibility: Can be used to serve various ASGI applications, including FastAPI, Starlette, and Django Channels.
# Deployment: Suitable for both development and production environments.


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


#     Pydantic
# Pydantic is a data validation and settings management library for Python, which uses Python type annotations to validate and parse data. It's widely used in FastAPI for request and response validation.

# Key Features
# Type Hints: Leverages Python type hints to define data models.
# Validation: Automatically validates data against the defined models, raising errors for invalid data.
# Parsing: Parses input data to the desired types, providing a clear and consistent API.
# Settings Management: Can be used to manage application settings and configurations.
# Example Usage

from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = Field(default=False)

# Example of using the model
item = Item(name="Sample Item", price=19.99)
print(item.dict())


# In this example:

# An Item model is defined using Pydantic.
# The Item model includes fields with type annotations and default values.
# The model is used to create an item instance and convert it to a dictionary.
# Conclusion
# Uvicorn: A high-performance ASGI server designed to run asynchronous web applications and APIs. It's commonly used with FastAPI to serve applications.
# Pydantic: A powerful library for data validation and settings management, using Python type hints. It's extensively used in FastAPI for defining and validating request and response data models.
# Both Uvicorn and Pydantic play crucial roles in the FastAPI ecosystem, contributing to its performance, reliability, and ease of use.

















# Dependency Injection (DI) is a design pattern used to implement IoC (Inversion of Control), allowing for better modularity and easier testing. It involves providing a component with its dependencies rather than having the component construct them itself.

# Key Concepts of Dependency Injection
# Inversion of Control (IoC): This principle states that the control of object creation and management should be transferred from the object itself to an external entity, often called the IoC container or DI container.

# Dependency: A dependency is any object that another object requires to function. For example, a service class might depend on a repository class to access data.

# Injection: The process of providing a dependency to a dependent object. There are several ways to inject dependencies:

# Constructor Injection: Dependencies are provided through a class constructor.
# Setter Injection: Dependencies are provided via setter methods.
# Interface Injection: Dependencies are provided through an interface that the class implements.
# Benefits of Dependency Injection
# Decoupling: DI helps to decouple the code, making it easier to change and maintain.
# Testability: By injecting mock dependencies, it becomes easier to write unit tests.
# Flexibility: DI allows for easy swapping of implementations without changing the dependent code.
# Maintainability: Code becomes cleaner and easier to understand, as the dependencies are clearly defined and managed externally.


class Repository:
    def get_data(self):
        return "Data from repository"

class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    def fetch_data(self):
        return self.repository.get_data()

# Dependency Injection
repository = Repository()
service = Service(repository)
print(service.fetch_data())



from fastapi import FastAPI, Depends

app = FastAPI()

def get_repository():
    return Repository()

@app.get("/data")
def read_data(repository: Repository = Depends(get_repository)):
    return {"data": repository.get_data()}








# FastAPI Interview Questions for Senior Software Engineer

# 1. **What are the key features of FastAPI and how do they benefit API development?**
#    - Expected Points: Performance, asynchronous capabilities, data validation with Pydantic, automatic generation of OpenAPI documentation, dependency injection.

# 2. **Can you explain how dependency injection works in FastAPI and provide an example?**
#    - Expected Points: Explanation of dependency injection, use of `Depends`, example of injecting a service or repository into a route.

# 3. **How does FastAPI handle request validation and serialization?**
#    - Expected Points: Use of Pydantic models, automatic validation, serialization of request bodies, query parameters, and path parameters.

# 4. **Describe how to implement authentication and authorization in a FastAPI application.**
#    - Expected Points: JWT tokens, OAuth2, use of dependencies for security, FastAPI's security utilities.

# 5. **What are the differences between ASGI and WSGI, and why is FastAPI built on ASGI?**
# ASGI (Asynchronous Server Gateway Interface) and WSGI (Web Server Gateway Interface) are both interfaces between web servers and web applications.
# 
# **WSGI**:
# - Synchronous: Designed for synchronous applications.
# - Blocking: Each request is handled one at a time, blocking the server until the request is completed.
# - Limited: Not suitable for handling long-lived connections like WebSockets.
# 
# **ASGI**:
# - Asynchronous: Designed for asynchronous applications.
# - Non-blocking: Can handle multiple requests concurrently without blocking.
# - Versatile: Supports long-lived connections like WebSockets and HTTP/2.
# 
# **Why FastAPI is built on ASGI**:
# - Performance: ASGI allows FastAPI to handle many requests concurrently, improving performance.
# - Asynchronous Support: Enables the use of async/await syntax for non-blocking I/O operations.
# - Modern Features: Supports WebSockets, HTTP/2, and other modern web features.

# 6. **How can you manage and scale a FastAPI application in a production environment?**
#    - Expected Points: Use of ASGI servers like Uvicorn or Daphne, deployment strategies (Docker, Kubernetes), load balancing, monitoring, and logging.

# 7. **Can you explain how middleware works in FastAPI and give an example of custom middleware?**
# Middleware in FastAPI is a function that runs before and after each request. It can be used for tasks like logging, authentication, and modifying requests or responses.
# 
# Example of custom middleware:
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Code to run before the request
        response = await call_next(request)
        # Code to run after the request
        response.headers["X-Custom-Header"] = "Custom Value"
        return response

app.add_middleware(CustomMiddleware)

# 8. **How does FastAPI support WebSocket connections and what are some use cases for WebSockets?**
#    - Expected Points: Definition of WebSockets, FastAPI's support for WebSockets, use cases like real-time updates, chat applications, live notifications.

# 9. **What strategies would you use to ensure the security of a FastAPI application?**
#    - Expected Points: Input validation, authentication and authorization, HTTPS, CORS, rate limiting, security headers, dependency injection for security.

# 10. **How would you handle background tasks and scheduled jobs in a FastAPI application?**
# FastAPI provides `BackgroundTasks` for handling background tasks. For more complex scheduling, you can use tools like Celery or APScheduler.
# 
# Example using `BackgroundTasks`:
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")

@app.post("/log")
async def log_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"message": "Log entry created"}

# Example using Celery for background tasks:
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def background_task(message: str):
    write_log(message)

@app.post("/celery-log")
async def log_message_with_celery(message: str):
    background_task.delay(message)
    return {"message": "Log entry created with Celery"}

# Example using APScheduler for scheduled jobs:
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(write_log, "interval", seconds=60, args=["Scheduled log entry"])
scheduler.start()
