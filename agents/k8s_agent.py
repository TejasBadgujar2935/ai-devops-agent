def generate_k8s_yaml(app_name, port):

    yaml_content = f"""
apiVersion: apps/v1
kind: Deployment

metadata:
  name: {app_name}
  labels:
    app: {app_name}

spec:
  replicas: 1

  selector:
    matchLabels:
      app: {app_name}

  template:
    metadata:
      labels:
        app: {app_name}

    spec:
      containers:
      - name: {app_name}
        image: {app_name}:latest
        imagePullPolicy: Never
        ports:
        - containerPort: {port}
"""

    with open("generated/deployment.yaml", "w") as f:
        f.write(yaml_content.strip())

    print("✅ deployment.yaml Generated")