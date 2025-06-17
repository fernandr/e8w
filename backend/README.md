# Flask Backend for Person App

## Setup

```
pip install -r requirements.txt
```

## Run
```
python app.py
```

The API will be available at http://localhost:5000

### Endpoints
- `GET /api/persons` — List all persons
- `POST /api/person` — Add a new person (JSON: {"name": ..., "email": ...})
- `POST /api/person/<name>` — Edit a person by name (JSON: {"name": ..., "email": ...})
- `GET /` — Home endpoint (returns welcome message)

## Test Data
On first run, the database is seeded with Alice, Bob, and Charlie.