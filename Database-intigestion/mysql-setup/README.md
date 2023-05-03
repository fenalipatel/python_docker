# Docker and MySQL Setup

This guide provides instructions on how to install Docker and set up a MySQL container.

## Prerequisites

Before starting, make sure you have the following prerequisites:

- Operating System: Windows
- Docker: Make sure Docker is installed on your system. Refer to the official Docker documentation for installation instructions specific to your operating system.

## Installation Steps

Follow these steps to install Docker and set up MySQL:

1. **Install Docker**: Visit the official Docker website (https://www.docker.com/) and download the Docker installation package suitable for your operating system. Follow the installation instructions provided on the website.

2. **Pull MySQL Docker Image**: Open a terminal or command prompt and run the following command to pull the MySQL Docker image:

   ```bash
   docker pull mysql
   

## Docker, create a Dockerfile and Docker Compose file

Follow these steps to install Docker, create a Dockerfile and Docker Compose file, and set up MySQL:

1. **Create Dockerfile**: Create a file named `Dockerfile` (without any file extension) in your project directory.

2. **Create Docker Compose File**: Create a file named `docker-compose.yml` in your project directory.

3. **Build and Run the Container**: Open a terminal or command prompt in your project directory and run the following command to build and run the MySQL container:

```bash
docker-compose up -d 
```
# Connecting Python Script to Docker MySQL

This project demonstrates how to connect a Python script with a Dockerized MySQL database.


## Setup Instructions

1. **Install Docker**
   - Download and install Docker from the official Docker website: [https://www.docker.com/get-started](https://www.docker.com/get-started)

2. **Pull the MySQL Docker Image**
   - Open a terminal or command prompt and execute the following command:
     ```
     docker pull mysql
     ```

3. **Run the MySQL Container**
   - Create and start a new Docker container using the MySQL image. Execute the following command:
     ```
     docker run -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=your_password -d mysql
     ```

4. **Connect to the MySQL Container**
   - Use a MySQL client to connect to the MySQL container using the following details:
     - Host: localhost
     - Port: 3306
     - Username: root
     - Password: your_password (as specified in step 3)

5. **Create a Database**
   - Once connected to the MySQL container, create a new database that your Python script will interact with.

6. **Install Required Python Packages**
   - In your Python environment, install the `mysql-connector-python` package using the following command:
     ```
     pip install mysql-connector-python
     ```

7. **Write Python Script**
   - Create a Python script that connects to the MySQL database and performs the desired operations.

8. **Update Connection Details**
   - In your Python script, update the connection details (`host`, `port`, `user`, `password`, `database`) to match the configuration of your MySQL container.

9. **Run the Python Script**
   - Execute your Python script to connect to the Dockerized MySQL database and perform the desired operations.








