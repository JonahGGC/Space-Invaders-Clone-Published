# 🚀 Space Invaders Clone

A Space Invaders clone built with **Unity 2022 LTS**, served as a **WebGL** application via **FastAPI**, fully containerized with **Docker** and deployed automatically through a **CI/CD pipeline with GitHub Actions**.

## 🎮 Demo

Play directly in your browser — desktop and mobile supported.

> Mobile controls: virtual joystick for movement, tap to shoot.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Game Engine | Unity 2022 LTS (WebGL build) |
| Backend | FastAPI + Uvicorn |
| Containerization | Docker + Docker Compose |
| CI/CD | GitHub Actions + Self-hosted runner |
| Asset Storage | Git LFS |

---

## 📁 Project Structure

```
Space-Invaders-Clone-Published/
├── WebGame/                  ← Unity WebGL build (served as static files)
│   ├── Build/
│   │   ├── WebGame.wasm
│   │   ├── WebGame.data
│   │   ├── WebGame.framework.js
│   │   └── WebGame.loader.js
│   ├── TemplateData/
│   └── index.html
├── main.py                   ← FastAPI server
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .github/
    └── workflows/
        └── ci.yml            ← CI/CD pipeline
```

---

## 🚀 Running Locally

### With Docker (recommended)

```bash
git clone https://github.com/JonahGGC/Space-Invaders-Clone-Published.git
cd Space-Invaders-Clone-Published
git lfs pull
docker-compose up --build
```

Open **http://localhost:8000** in your browser.

### Without Docker

```bash
git clone https://github.com/JonahGGC/Space-Invaders-Clone-Published.git
cd Space-Invaders-Clone-Published
git lfs pull
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## ⚙️ CI/CD Pipeline

Every push to `main` triggers the GitHub Actions pipeline:

1. **Checkout** — clones the repo including Git LFS assets
2. **Build** — builds the Docker image
3. **Smoke test** — starts the container and verifies the server responds
4. **Deploy** — restarts the container on the self-hosted runner with the new build

```
git push → GitHub Actions → Docker build → Smoke test → Auto deploy ✅
```

---

## 🎯 Features

- Classic Space Invaders gameplay
- Component-based architecture (SRP, inheritance, encapsulation, polymorphism)
- Sandevistan afterimage trail effect
- Slow-motion mechanic
- Shield system
- Dash mechanic
- Mobile virtual joystick controls
- WebGL build served via FastAPI

---

## 📋 Requirements

- Docker + Docker Compose
- Git LFS (for WebGL binary assets)

---

## 👤 Author

**Jonahtan González** — [@JonahGGC](https://github.com/JonahGGC)
