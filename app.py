from agents.project_detector import detect_project_type
from agents.port_detector import detect_port
from agents.deploy_agent import deploy_to_kubernetes

from agents.react_docker_agent import generate_react_dockerfile
from agents.node_docker_agent import generate_node_dockerfile
from agents.fastapi_docker_agent import generate_fastapi_dockerfile
from agents.springboot_docker_agent import generate_springboot_dockerfile

from agents.docker_build_agent import build_image

from agents.k8s_agent import generate_k8s_yaml
from agents.service_agent import generate_service_yaml

from agents.deploy_agent import deploy_to_kubernetes


project_path = input("Enter Project Path: ")

project_type = detect_project_type(project_path)

port = detect_port(project_path)

print(f"\nDetected Project Type: {project_type}")
print(f"Detected Port: {port}")


# =========================
# React
# =========================

if project_type == "react":

    app_name =input(
    "Enter Application Name: "
)

    generate_react_dockerfile(project_path)

    generate_k8s_yaml(app_name, port)

    generate_service_yaml(app_name, port)

    if build_image(app_name, project_path):
        deploy_to_kubernetes()


# =========================
# Node
# =========================

elif project_type == "node":

    app_name = "node-app"

    generate_node_dockerfile(project_path)

    generate_k8s_yaml(app_name, port)

    generate_service_yaml(app_name, port)

    if build_image(app_name, project_path):
        deploy_to_kubernetes()


# =========================
# FastAPI
# =========================

elif project_type == "fastapi":

    app_name = "fastapi-app"

    generate_fastapi_dockerfile(project_path)

    generate_k8s_yaml(app_name, port)

    generate_service_yaml(app_name, port)

    if build_image(app_name, project_path):
        deploy_to_kubernetes()


# =========================
# Spring Boot
# =========================

elif project_type == "springboot":

    app_name = "springboot-app"

    generate_springboot_dockerfile(project_path)

    generate_k8s_yaml(app_name, port)

    generate_service_yaml(app_name, port)

    if build_image(app_name, project_path):
        deploy_to_kubernetes()


# =========================
# Unsupported
# =========================

else:

    print("❌ Unsupported Project Type")