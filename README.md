Develop a basic CRUD application.

- Using a simple Excalidraw as a starting point (draft)
- Prompting iteratively in Cursor IDE ("vibe coding")
- Safeguarding intermediate milestones in this Git repo

This section and the below images are edited manually.

- The rest of this repo was edited by Cursor

This model was drafted as a starting point:

![](./model.svg)

This webapp was the first result after a couple of small iterations:

![](./webapp-home.png)

![](./webapp-list1.png)

![](./webapp-add.png)

![](./webapp-add-ok.png)

![](./webapp-list2.png)

# Person Web App (Flask + Vue)

## Structure
- `backend/` — Flask + SQLAlchemy API
- `frontend/` — Vue 3 app

## Quickstart

### 1. Backend
```
cd backend
pip install -r requirements.txt
python app.py
```
API: http://localhost:5000

### 2. Frontend
```
cd frontend
npm install
npm run serve
```
App: http://localhost:8080

## Features
- List, add, and edit persons
- Test data: Alice, Bob, Charlie
