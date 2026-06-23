import os


def build_image(app_name, project_path):

    print("\n🐳 Building Docker Image...")

    build_status = os.system(
        f"docker build -t {app_name}:latest {project_path}"
    )

    if build_status != 0:

        print("❌ Docker Build Failed")
        return False

    print("✅ Docker Image Built")

    print("\n📦 Loading Image Into Minikube...")

    load_status = os.system(
        f"minikube image load {app_name}:latest"
    )

    if load_status != 0:

        print("❌ Minikube Image Load Failed")
        return False

    print("✅ Image Loaded Into Minikube")

    return True