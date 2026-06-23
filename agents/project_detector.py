import os
import json


def detect_project_type(project_path):

    files = os.listdir(project_path)

    # React / Vite
    if (
        "vite.config.js" in files
        or "vite.config.ts" in files
        or "vite.config.mjs" in files
    ):
        return "react"

    # FastAPI
    elif "requirements.txt" in files:

        requirements_path = os.path.join(
            project_path,
            "requirements.txt"
        )

        with open(
            requirements_path,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read().lower()

            if "fastapi" in content:
                return "fastapi"

    # Spring Boot
    elif "pom.xml" in files:
        return "springboot"

    # Node.js
    elif "package.json" in files:

        package_json_path = os.path.join(
            project_path,
            "package.json"
        )

        try:

            with open(
                package_json_path,
                "r",
                encoding="utf-8"
            ) as f:

                package_data = json.load(f)

            dependencies = {}

            dependencies.update(
                package_data.get("dependencies", {})
            )

            dependencies.update(
                package_data.get("devDependencies", {})
            )

            if "react" in dependencies:
                return "react"

            return "node"

        except Exception:
            return "node"

    return "unknown"