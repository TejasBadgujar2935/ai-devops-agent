import os
import json


def generate_react_dockerfile(project_path):

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

        scripts = package_data.get(
            "scripts",
            {}
        )

        # Vite React

        if (
            "dev" in scripts and
            "vite" in scripts["dev"]
        ):

            dockerfile = """
FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm","run","dev","--","--host"]
"""

            print("✅ Vite React Detected")

        # CRA React

        elif (
            "start" in scripts and
            "react-scripts" in scripts["start"]
        ):

            dockerfile = """
FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm","start"]
"""

            print("✅ CRA React Detected")

        else:

            dockerfile = """
FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm","start"]
"""

            print("⚠️ Unknown React Type - Using Default")

    except Exception as e:

        print(f"❌ Error: {e}")

        return

    with open(
        os.path.join(project_path, "Dockerfile"),
        "w"
    ) as f:

        f.write(dockerfile.strip())

    print("✅ React Dockerfile Generated")