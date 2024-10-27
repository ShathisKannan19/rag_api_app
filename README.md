# QA RAG API Backend

This repository contains the backend for the QA RAG application. It is built using FastAPI and integrates with various libraries such as LangChain, SQLAlchemy, and more. The backend is containerized using Docker and managed with Docker Compose.

## Key Features

- **FastAPI**: High-performance web framework for building APIs.
- **LangChain Integration**: Utilizes LangChain for building applications with LLMs.
- **Chroma Integration**: Utilizes Chroma for vector storage and retrieval.
- **SQLAlchemy**: ORM for database interactions.
- **Dockerized**: Easily deployable using Docker and Docker Compose.
- **Environment Configuration**: Managed using .env files.

## Description

The QA RAG Backend is a robust backend service designed to support a QA application. It leverages FastAPI for creating high-performance APIs and integrates with LangChain for building applications with large language models (LLMs). The backend also uses SQLAlchemy for database interactions and is containerized using Docker for easy deployment and management.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Local Deployment

To deploy the application locally, follow these steps:

1. Ensure Docker and Docker Compose are installed on your machine.
2. Clone the repository and navigate to the project directory.
3. Copy the `.env-example` file to `.env` and update the environment variables as needed.
4. Run `docker-compose up --build` to build and start the services.
5. The backend API will be accessible at [http://localhost:8000](http://localhost:8000).

## Environment Configuration

Environment variables are managed using a `.env` file located in the `backend` directory. An example configuration is provided in `.env-example`. Here are some key environment variables:

- `GROQ_API_KEY`: API key for Groq integration.
- `DATA_PATH`: Path to the data directory.
- `CHROMA_PATH`: Path to the Chroma directory.
- `HF_TOKEN`: Token for Hugging Face integration.

### API Keys Configuration

To use the Groq and Hugging Face integrations, you need to obtain API keys and store them in the `.env` file.

#### Groq API Key

1. Sign up or log in to your Groq account at [Groq](https://groq.com).
2. Navigate to the API section in your account settings.
3. Generate a new API key.
4. Copy the API key and add it to your `.env` file:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

#### Hugging Face Token

1. Sign up or log in to your Hugging Face account at [Hugging Face](https://huggingface.co).
2. Go to your account settings and find the API tokens section.
3. Generate a new token.
4. Copy the token and add it to your `.env` file:
    ```env
    HF_TOKEN=your_hugging_face_token_here
    ```

Ensure that your `.env` file is not committed to version control to keep your API keys secure.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ShathisKannan19/rag_api_app.git
    cd rag_api_app
    ```

2. Create a `.env` file in the `backend` directory by copying the `.env-example` file and updating the values as needed:
    ```sh
    cp backend/.env-example backend/.env
    ```

3. Build and start the services:
    ```sh
    docker-compose up --build
    ```

4. Access the backend API at [http://localhost:8000](http://localhost:8000).

5. Check the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) using Swagger.

## API Endpoints

The backend provides several API endpoints for interacting with the QA application. Here are some key endpoints:

- **GET /api**: API working status check.
- **POST /api/login**: User login endpoint.
- **POST /api/register**: User registration endpoint.
- **POST /api/agent_chat**: Endpoint for initiating a chat with the llm and retriver.
- **POST /uploadfile**: Endpoint for uploading data.

## License

This project is licensed under the MIT License. See the [MIT-LICENSE.txt](MIT-LICENSE.txt) file for details.

## Authors

- **ShathisKannan19** - [vshathiskannan@gmail.com](mailto:vshathiskannan@gmail.com)

For more details, refer to the README.md file.