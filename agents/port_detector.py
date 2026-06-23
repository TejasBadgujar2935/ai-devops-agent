import os
import json


def detect_port(project_path):

    package_json = os.path.join(
        project_path,
        "package.json"
    )

    if os.path.exists(package_json):

        try:

            with open(
                package_json,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

            scripts = data.get(
                "scripts",
                {}
            )

            # Vite

            if "dev" in scripts:

                dev_script = scripts["dev"]

                if "vite" in dev_script:

                    if "--port" in dev_script:

                        parts = dev_script.split()

                        index = parts.index("--port")

                        return int(
                            parts[index + 1]
                        )

                    return 5173

            # CRA

            if "start" in scripts:

                start_script = scripts["start"]

                if "react-scripts" in start_script:
                    return 3000

                if "node" in start_script:
                    return 3000

        except:
            pass

    requirements = os.path.join(
        project_path,
        "requirements.txt"
    )

    if os.path.exists(requirements):

        with open(
            requirements,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read().lower()

            if "fastapi" in content:
                return 8000

    pom_file = os.path.join(
        project_path,
        "pom.xml"
    )

    if os.path.exists(pom_file):
        return 8080

    return 3000