---
layout: slides
title: Datasets for Logic Problem Solvers
date: 2025-01-23 02:30
author: Dr. Khalil Chebil
categories: education
comments: true
permalink: /dockerslides
tags:
  - Problem solvers
  - Logic
---

<section data-markdown>
    <textarea data-template>

    <div align="center">
    <br/>

    ## Docker Workshop: From Basics to Deployment  
    *A Hands-on Guide for Developers*  

    <img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" alt="Docker Logo" width="25%" height="25%">       

    </div>
---
## Presentation Overview
A practical introduction to Docker using a real-world **Object Detection Application** built with **Streamlit**, **YOLO**, and **OpenCV** for camera-based AI inference.

---

## Table of Contents
1. [What is Docker?](#what-is-docker)
2. [Why Use Docker?](#why-use-docker)
3. [Our Example Application](#our-example-application)
4. [Docker Basics](#docker-basics)
5. [Containerizing Our Todo App](#containerizing-our-todo-app)
6. [Database Container](#database-container)
7. [Docker Compose](#docker-compose)
8. [Hands-on Commands](#hands-on-commands)
9. [Best Practices](#best-practices)
10. [Next Steps](#next-steps)

---

## What is Docker?

Docker is a platform that uses **containerization** to package applications and their dependencies into lightweight, portable containers.

### Key Concepts:
- **Container**: A running instance of an image
- **Image**: A blueprint for creating containers
- **Dockerfile**: Instructions to build an image
- **Registry**: Storage for Docker images (like Docker Hub)

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Application   │    │   Application   │    │   Application   │
│   Dependencies  │    │   Dependencies  │    │   Dependencies  │
│      OS         │    │   Container     │    │   Container     │
│   Hardware      │    │    Runtime      │    │    Runtime      │
└─────────────────┘    │   Host OS       │    │   Host OS       │
   Traditional VM      │   Hardware      │    │   Hardware      │
                       └─────────────────┘    └─────────────────┘
                          Docker Container       Docker Container
```

---

## Why Use Docker?

### Problems Docker Solves:
- ❌ "It works on my machine" syndrome
- ❌ Complex environment setup
- ❌ Dependency conflicts
- ❌ Inconsistent deployments

### Benefits:
- ✅ **Portability**: Run anywhere Docker is installed
- ✅ **Consistency**: Same environment across development, testing, and production
- ✅ **Isolation**: Applications don't interfere with each other
- ✅ **Scalability**: Easy to scale up or down
- ✅ **Efficiency**: Lightweight compared to VMs

---

## Our Example Application

We'll containerize an **AI-Powered Object Detection Application** with:

### Frontend: Streamlit Web App
- Modern web-based interface
- Real-time camera access
- Interactive object detection
- Image upload capabilities

### AI Engine: YOLO + OpenCV
- YOLOv8 object detection model
- Real-time image processing
- 80+ object class detection
- Confidence scoring

### Python Ecosystem
- Streamlit for web interface
- OpenCV for image processing
- PyTorch for AI inference
- NumPy for numerical operations

### Application Architecture:
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Web Browser   │────▶│   Streamlit     │────▶│   YOLO Model    │
│   (Interface)   │     │   (Web App)     │     │   (AI Engine)   │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                │                         │
                                ▼                         ▼
                        ┌─────────────────┐     ┌─────────────────┐
                        │   Camera/       │     │   Object        │
                        │   Image Input   │     │   Detection     │
                        └─────────────────┘     └─────────────────┘
```

---

## Docker Basics

### Essential Docker Commands:

#### Image Management:
```bash
# Build an image
docker build -t my-app .

# List images
docker images

# Pull an image from registry
docker pull postgres:13

# Remove an image
docker rmi my-app
```

#### Container Management:
```bash
# Run a container
docker run -d --name my-container my-app

# List running containers
docker ps

# List all containers
docker ps -a

# Stop a container
docker stop my-container

# Remove a container
docker rm my-container

# View logs
docker logs my-container

# Execute commands in running container
docker exec -it my-container bash
```

---

## Understanding the Python Application Code

Before we containerize our application, let's examine the Streamlit object detection application structure and understand how each component works.

### Project Structure
```
app/
├── streamlit_app.py   # Main Streamlit application
├── requirements.txt   # Python dependencies
models/                # YOLO model storage
outputs/               # Detection results storage
```

### 1. streamlit_app.py - Main Application

This is our main Streamlit application with object detection capabilities:

```python
import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import tempfile
import os

@st.cache_resource
def load_model():
    """Load the YOLO model once and cache it"""
    try:
        model = YOLO('yolov8n.pt')  # Nano version for speed
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def detect_objects(image, model):
    """Perform object detection on an image"""
    if model is None:
        return None
    
    try:
        results = model(image)
        return results[0]  # Get first result
    except Exception as e:
        st.error(f"Error during detection: {e}")
        return None

# Streamlit UI setup
st.title("🔍 Object Detection with YOLO")
st.write("Upload an image or use your camera to detect objects!")
```

**Key Features:**
- Streamlit web framework for interactive UI
- YOLO model integration for object detection
- Camera and image upload capabilities
- Caching for optimal performance
- Error handling for robust operation

### 2. Object Detection Logic

The core detection functionality processes images and identifies objects:

```python
def process_image_detection(uploaded_file, model):
    """Process uploaded image for object detection"""
    if uploaded_file is not None:
        # Load and display the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Perform detection
        with st.spinner("Detecting objects..."):
            results = detect_objects(image, model)
            
        if results is not None:
            # Display results
            annotated_image = results.plot()
            st.image(annotated_image, caption="Detection Results", use_column_width=True)
            
            # Show detection details
            if len(results.boxes) > 0:
                st.subheader("Detected Objects:")
                for i, box in enumerate(results.boxes):
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    class_name = model.names[class_id]
                    
                    st.write(f"**{class_name}** - Confidence: {confidence:.2%}")
            else:
                st.write("No objects detected in the image.")
```

**Key Features:**
- **Environment-based Configuration**: Reads database settings from environment variables
- **Connection Management**: Handles PostgreSQL connections using JDBC
- **CRUD Operations**: Create, Read, Update, Delete functionality
- **Error Handling**: Proper exception handling for database operations
- **Docker-Ready**: Automatically adapts to containerized environment

**Important Database Methods:**

1. **getAllTodos()**: Retrieves all todos from database
2. **addTodo()**: Inserts new todo with prepared statements
3. **updateTodo()**: Updates existing todo safely
4. **deleteTodo()**: Removes todo by ID
5. **toggleTodoComplete()**: Changes completion status

### 3. TodoApp.java - The GUI Application

This is the main Swing application providing the user interface:

```java
package com.todoapp;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.List;

public class TodoApp extends JFrame {
    private TodoDAO todoDAO;
    private DefaultListModel<Todo> listModel;
    private JList<Todo> todoList;
    private JTextField titleField;
    private JTextArea descriptionArea;
    
    public TodoApp() {
        todoDAO = new TodoDAO();
        initializeGUI();
        loadTodos();
    }
    
    private void initializeGUI() {
        setTitle("Docker Todo App - Java Swing + PostgreSQL");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        
        // Create UI components
        JPanel leftPanel = createListPanel();
        JPanel rightPanel = createFormPanel();
        
        add(leftPanel, BorderLayout.WEST);
        add(rightPanel, BorderLayout.CENTER);
    }
    
    // Event handlers
    private void addTodo(ActionEvent e) { /* Implementation */ }
    private void updateTodo(ActionEvent e) { /* Implementation */ }
    private void deleteTodo(ActionEvent e) { /* Implementation */ }
}
```

**Streamlit Components:**

1. **Main Interface**: 
   - `st.title()` and `st.write()` for headers and descriptions
   - `st.file_uploader()` for image upload
   - `st.camera_input()` for live camera capture

2. **Display Elements**:
   - `st.image()` for showing original and annotated images
   - `st.columns()` for layout organization
   - `st.expander()` for collapsible sections

3. **Interactive Features**:
   - Real-time processing with `st.spinner()`
   - Session state management
   - Automatic UI updates on user interaction

**Key AI/ML Patterns:**

- **Model Loading**: `@st.cache_resource` for efficient model caching
- **Computer Vision Pipeline**: Image preprocessing → YOLO inference → Result visualization
- **Real-time Processing**: Streamlit's reactive framework for instant feedback
- **Error Handling**: Graceful degradation for model loading and inference failures

### Code Architecture Benefits

**Separation of Concerns:**
- `streamlit_app.py`: Main application logic and UI
- Model loading: Cached AI model management
- Image processing: Computer vision pipeline

**Performance Optimization:**
- `@st.cache_resource` for model caching
- Efficient image processing with OpenCV/PIL
- Lightweight YOLO nano model for speed

**Error Handling:**
- Model loading failures
- Image processing errors
- Camera access issues
- Graceful user feedback

**Docker Integration Points:**
- Python package management with requirements.txt
- OpenCV system dependencies
- Port exposure for web access
- Non-root user security

This streamlined architecture makes the AI application perfect for containerized deployment and scaling!

---

## Containerizing Our Streamlit Object Detection App

### Step 1: Create the Dockerfile

```dockerfile
# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgstreamer1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Create non-root user for security
RUN useradd -m -u 1001 appuser && chown -R appuser:appuser /app
USER appuser

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Step 2: Build the Image

```bash
# Build the Docker image
docker build -t streamlit-detector:1.0 .

# Verify the image was created
docker images | grep streamlit-detector
```

---

## Running the Streamlit Application

### Step 1: Run the Application Container

```bash
# Run the Streamlit app container
docker run -d \
  --name streamlit-detector \
  -p 8501:8501 \
  streamlit-detector:1.0
```

### Understanding Docker Networking and Ports

**Port Mapping:**
The `-p 8501:8501` flag maps the container's internal port to the host:
- First `8501`: Host port (accessible from your browser)
- Second `8501`: Container port (where Streamlit runs)

**Alternative Port Configurations:**
```bash
# Map to different host port
docker run -p 3000:8501 streamlit-detector:1.0

# Map to all interfaces
docker run -p 0.0.0.0:8501:8501 streamlit-detector:1.0

# Let Docker choose the host port
docker run -P streamlit-detector:1.0
```

### Step 2: Access the Application

Once the container is running, you can access the application at:
- **Local**: http://localhost:8501
- **Network**: http://YOUR_IP:8501

### Useful Docker Commands for Our App

```bash
# Check container status
docker ps

# View application logs
docker logs streamlit-detector

# Stop the container
docker stop streamlit-detector

# Remove the container
docker rm streamlit-detector

# Enter the container for debugging
docker exec -it streamlit-detector /bin/bash
  -e DB_USER=todouser \
  -e DB_PASSWORD=todopass \
  todo-app:1.0
```

---

## From Docker to Docker Compose

As applications grow complex with multiple containers, managing them with individual `docker run` commands becomes difficult. Docker Compose solves this by defining multi-container applications in a single YAML file.

### Migration Process: Manual Commands → Docker Compose

**Step 1: Analyze Current Docker Commands**

Our current manual setup:
```bash
# Database container
docker run -d \
  --name postgres-db \
  -e POSTGRES_DB=todoapp \
  -e POSTGRES_USER=todouser \
  -e POSTGRES_PASSWORD=todopass \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:13

# Application container
docker run -d \
  --name todo-app-container \
  --link postgres-db:database \
  -e DB_HOST=database \
  -e DB_PORT=5432 \
  -e DB_NAME=todoapp \
  -e DB_USER=todouser \
  -e DB_PASSWORD=todopass \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -e DISPLAY=$DISPLAY \
  todo-app:1.0
```

**Problems with Manual Commands:**
- 🔴 **Order Dependencies**: Must start database before app
- 🔴 **Network Management**: Manual linking is deprecated
- 🔴 **Environment Variables**: Repeated configuration
- 🔴 **Volume Management**: Manual volume creation
- 🔴 **Scaling**: Difficult to scale services
- 🔴 **Maintenance**: Hard to update and restart services

**Step 2: Convert to Docker Compose**

Each `docker run` command becomes a service in `docker-compose.yml`:

| Docker Command Element | Docker Compose Equivalent |
|------------------------|---------------------------|
| `--name postgres-db` | `services: database:` |
| `-e POSTGRES_DB=todoapp` | `environment: POSTGRES_DB: todoapp` |
| `-p 5432:5432` | `ports: - "5432:5432"` |
| `-v postgres_data:/path` | `volumes: - postgres_data:/path` |
| `--link postgres-db:database` | `networks:` + `depends_on:` |
| `postgres:13` | `image: postgres:13` |

**Step 3: Migration Benefits**

✅ **Simplified Management**
```bash
# Instead of multiple docker run commands
docker-compose up -d

# Instead of stopping each container
docker-compose down
```

✅ **Automatic Networking**
```yaml
# Containers can communicate by service name
services:
  database:    # hostname: database
  app:         # hostname: app
```

✅ **Dependency Management**
```yaml
app:
  depends_on:
    - database  # Ensures database starts first
```

✅ **Environment Configuration**
```yaml
# Centralized environment variables
environment:
  DB_HOST: database
  DB_PORT: 5432
```

## Docker Compose

Docker Compose simplifies application deployment by defining services in a single YAML file.

### docker-compose.yml for Streamlit App

```yaml
version: '3.8'

services:
  streamlit-app:
    build: 
      context: .
      dockerfile: Dockerfile
    container_name: streamlit-detector
    restart: unless-stopped
    ports:
      - "8501:8501"
    volumes:
      # Optional: Mount for saving detection results
      - ./outputs:/app/outputs
      # Optional: Mount for custom models
      - ./models:/app/models:ro
    environment:
      # Streamlit configuration
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/healthz"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

# Optional: Volume definitions for persistence
volumes:
  detection_outputs:
    driver: local
  model_cache:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ./data/postgres  # Optional: specify host location

# Network definitions
networks:
  todo-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

### Volume Configuration Explained

**1. Named Volumes in Compose:**
```yaml
volumes:
  postgres_data:/var/lib/postgresql/data
```
- **Purpose**: Persistent database storage
- **Location**: Managed by Docker (`/var/lib/docker/volumes/`)
- **Lifecycle**: Survives container recreation
- **Sharing**: Can be mounted by multiple containers

**2. Bind Mounts in Compose:**
```yaml
volumes:
  ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
```
- **Purpose**: Mount host files into container
- **Access Modes**: 
  - `ro` (read-only) - Container can't modify host file
  - `rw` (read-write) - Default, container can modify
- **Use Cases**: Configuration files, source code, logs

**3. Volume Driver Options:**
```yaml
volumes:
  postgres_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /host/path/to/data
```
- **Custom Location**: Specify where data is stored on host
- **Backup Strategy**: Easier to backup known locations
- **Performance**: May have different performance characteristics

**4. Cross-Platform Volume Considerations:**

**Linux/macOS:**
```yaml
volumes:
  - /tmp/.X11-unix:/tmp/.X11-unix:rw  # X11 GUI support
  - ./data:/app/data                   # Relative path
```

**Windows:**
```yaml
volumes:
  - //c/temp/.X11-unix:/tmp/.X11-unix:rw  # Windows path format
  - .\data:/app/data                      # Windows relative path
```

**5. Volume Best Practices:**

```yaml
services:
  database:
    volumes:
      # ✅ Named volume for data persistence
      - postgres_data:/var/lib/postgresql/data
      
      # ✅ Read-only bind mount for config
      - ./config/postgresql.conf:/etc/postgresql/postgresql.conf:ro
      
      # ✅ Initialization scripts
      - ./scripts:/docker-entrypoint-initdb.d:ro
      
      # ❌ Avoid: Binding entire host filesystem
      # - /:/host:rw
      
      # ❌ Avoid: Anonymous volumes for important data
      # - /var/lib/postgresql/data
```

### Docker Compose Commands

```bash
# Start the Streamlit app
docker-compose up -d

# View application logs
docker-compose logs -f streamlit-app

# Stop the service
docker-compose down

# Rebuild and start (after code changes)
docker-compose up --build

# Access the application
# Browser: http://localhost:8501

# Check service health
docker-compose ps
```

### Managing Detection Results

**Output Management Commands:**
```bash
# List detection output files
ls -la ./outputs/

# Remove containers but keep output files
docker-compose down

# Clean up everything including outputs (⚠️ Results loss!)
docker-compose down -v

# Backup detection results
tar czf detection-results-$(date +%Y%m%d).tar.gz ./outputs/

# Copy results from running container
docker cp streamlit-detector:/app/outputs/ ./local-outputs/

# Monitor disk usage
du -sh ./outputs/
```

### Deployment Workflow: Step by Step

**Phase 1: Setup**
```bash
# 1. Create project structure
mkdir -p outputs models

# 2. Build the application
docker-compose build

# 3. Start the service
docker-compose up -d
```

**Phase 2: Configuration**
```bash
# 4. Validate compose file
docker-compose config

# 5. Check services
docker-compose config --services

# 6. Verify port availability
netstat -an | grep 8501  # Should be free
```

**Phase 3: Deployment**
```bash
# 7. Start the application
docker-compose up -d

# 8. Check if service is running
docker-compose ps

# 9. Verify application is accessible
curl -f http://localhost:8501/healthz
```

**Phase 4: Testing**
```bash
# 10. Test application functionality
docker-compose logs streamlit-app

# 11. Open in browser
# Visit http://localhost:8501

# 12. Test object detection
# Upload an image or use camera
```

### Streamlit App Troubleshooting Guide

**Problem: Application Not Loading**
```bash
# Check if container is running
docker-compose ps

# Check application logs
docker-compose logs streamlit-app

# Verify port mapping
docker port streamlit-detector 8501
```

**Problem: Camera Not Working**
```bash
# Check browser permissions
# Enable camera access in browser settings

# For Linux: Check device permissions
ls -la /dev/video*

# For Docker: Add device access
devices:
  - /dev/video0:/dev/video0
```

**Problem: Model Loading Issues**
```bash
# Check model download
docker-compose exec streamlit-app ls -la /app/.cache/

# Check internet connectivity in container
docker-compose exec streamlit-app ping ultralytics.com

# Force model re-download
docker-compose exec streamlit-app rm -rf /app/.cache/
```

**Problem: Volume Not Found**
```bash
# List all volumes
docker volume ls

# Create volume manually if needed
docker volume create dockerproject_postgres_data

# Restart services
docker-compose down && docker-compose up -d
```

**Problem: Cross-Platform Path Issues**
```yaml
# Windows: Use forward slashes or escape backslashes
volumes:
  - ./data:/app/data          # ✅ Works
  - .\\data:/app/data         # ❌ May cause issues
  - /c/Users/user/data:/app/data  # ✅ Absolute path
```

---

## Hands-on Commands

### Complete Workflow:

1. **Prepare the Application**
   ```bash
   # Navigate to project directory
   cd docker-hands-on-project
   
   # Create required directories
   mkdir -p outputs models
   
   # Verify files are in place
   ls -la app/
   ```

2. **Build and Run with Docker**
   ```bash
   # Build the image
   docker build -t streamlit-detector:latest .
   
   # Run with docker-compose
   docker-compose up -d
   
   # Check running containers
   docker-compose ps
   ```

3. **Test Object Detection**
   ```bash
   # Open browser and navigate to:
   # http://localhost:8501
   
   # Upload test image or use camera
   # Check detection results
   ls -la outputs/
   ```

4. **Debugging**
   ```bash
   # View application logs
   docker-compose logs streamlit-app
   
   # Enter container shell
   docker exec -it streamlit-detector bash
   
   # Monitor container performance
   docker stats streamlit-detector
   ```

5. **Cleanup**
   ```bash
   # Stop the application
   docker-compose down
   
   # Keep detection results
   # Remove everything including results
   docker-compose down -v
   
   # Clean up unused resources
   docker system prune
   ```

---

## Best Practices

### 1. Dockerfile Optimization
- Use specific image versions (not `latest`)
- Minimize layers
- Use `.dockerignore` file
- Run as non-root user

### 2. Security
- Don't store secrets in images
- Use environment variables
- Scan images for vulnerabilities
- Keep images updated

### 3. Performance
- Use multi-stage builds
- Minimize image size
- Cache dependencies properly

### 4. Development Workflow
```bash
# Development with code mounting
docker-compose -f docker-compose.dev.yml up

# Production deployment
docker-compose up -d

# View logs for debugging
docker-compose logs -f streamlit-app

# Restart after code changes
docker-compose restart streamlit-app
```

---

## Next Steps

### Learning Path:
1. **Container Orchestration**: Learn Kubernetes
2. **CI/CD Integration**: GitHub Actions, Jenkins
3. **Monitoring**: Prometheus, Grafana
4. **Service Mesh**: Istio, Linkerd
5. **Cloud Platforms**: AWS ECS, Azure Container Instances

### Resources:
- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Docker Compose Examples](https://github.com/docker/awesome-compose)

---

## Summary

✅ **What we learned:**
- Docker fundamentals and benefits
- Containerizing a Python Streamlit application
- AI/ML model deployment with YOLO
- Web-based application deployment
- Practical Docker commands and workflows

✅ **Key takeaways:**
- Containers provide consistency for AI applications
- Docker simplifies ML model deployment
- Web apps are easier to containerize than desktop GUIs
- Camera integration requires proper device permissions

🎯 **Try it yourself:**
- Clone this example
- Experiment with different YOLO models
- Add new detection features
- Deploy to cloud platforms with GPU support

---

*Thank you for joining this Docker hands-on session! 🐳*

  </textarea>
</section>