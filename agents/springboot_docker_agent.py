import ollama
import os


def generate_springboot_dockerfile(project_path):

    prompt = """
Generate a Dockerfile for a Spring Boot application.

Requirements:
- Use OpenJDK 17
- Copy target/*.jar as app.jar
- Expose port 8080
- Run application using java -jar app.jar

Return only Dockerfile code.
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

    print("✅ Spring Boot Dockerfile Generated")