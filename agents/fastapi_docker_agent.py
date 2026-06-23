import ollama
import os


def generate_fastapi_dockerfile(project_path):

    prompt = """
Generate a Dockerfile for a FastAPI application.

Requirements:
- Use Python 3.11
- Set WORKDIR to /app
- Copy requirements.txt
- Run pip install
- Copy application code
- Expose port 8000
- Start using uvicorn

Return only Dockerfile.
No markdown.
No explanation.
"""

    response = ollama.chat(
        model='llama3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    dockerfile = response['message']['content']

    dockerfile = dockerfile.replace(
        "```dockerfile",
        ""
    )

    dockerfile = dockerfile.replace(
        "```",
        ""
    )

    with open(
        os.path.join(project_path, "Dockerfile"),
        "w"
    ) as f:

        f.write(dockerfile)

    print("✅ FastAPI Dockerfile Generated")