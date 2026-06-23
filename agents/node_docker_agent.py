import ollama
import os


def generate_node_dockerfile(project_path):

    prompt = """
Generate a Dockerfile for a Node.js Express application.

Requirements:
- Use Node.js 20
- Set WORKDIR to /app
- Copy package.json files
- Run npm install
- Copy application code
- Expose port 3000
- Start application using npm start

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

    dockerfile = dockerfile.replace("```dockerfile", "")
    dockerfile = dockerfile.replace("```", "")

    with open(
        os.path.join(project_path, "Dockerfile"),
        "w"
    ) as f:
        f.write(dockerfile)

    print("✅ Node Dockerfile Generated")