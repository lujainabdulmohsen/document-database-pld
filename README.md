# Document Database PLD

## Model

Document Database

## Database

MongoDB

## POC Features

- Connect to MongoDB
- Insert documents
- Query documents
- Update documents
- Delete documents
- Nested documents
- Nested field queries

## Run

```bash
docker run -d --name pld-mongodb -p 27017:27017 mongo:8.0
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 poc.py

