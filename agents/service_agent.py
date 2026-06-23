import ollama

def generate_service_yaml(app_name, port):

    prompt = f"""
Generate a Kubernetes Service YAML.

Requirements:
- Return only YAML
- No markdown
- No explanation
- apiVersion: v1
- kind: Service
- Service Name: {app_name}-service
- Type: NodePort
- Port: {port}
- TargetPort: {port}
- Selector key must be: app
- Selector value must be: {app_name}

Output only valid YAML.
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

    service_yaml = response['message']['content']

    service_yaml = service_yaml.replace("```yaml", "")
    service_yaml = service_yaml.replace("```", "")

    with open("generated/service.yaml", "w") as f:
        f.write(service_yaml)

    print("✅ service.yaml Generated")