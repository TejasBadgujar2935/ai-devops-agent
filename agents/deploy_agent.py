import os

def deploy_to_kubernetes():

    print("\n☸️ Deploying Application...")

    deployment_status = os.system(
        "kubectl apply -f generated/deployment.yaml"
    )

    service_status = os.system(
        "kubectl apply -f generated/service.yaml"
    )

    if deployment_status == 0 and service_status == 0:
        print("✅ Deployment Completed")
    else:
        print("❌ Deployment Failed")