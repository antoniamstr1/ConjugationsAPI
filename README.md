# Flask Verb Conjugation API

This Flask application provides a simple REST API to retrieve full verb conjugations for various languages using the [`mlconjug3`](https://mlconjug3.readthedocs.io/en/latest/usage.html) library.

---

## Features

- Conjugate verbs in multiple tenses.
- Returns JSON with all conjugated forms organized by tense and grammatical person.
- Simple query via HTTP GET with params

---

## Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd <ConjugationsAPI>
```

2. **Create a Python virtual environment in that folder:**
```bash
python -m venv venv
```

3. **Activate venv in cmd**
```bash
venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **run Flask app**
```bash
python server.py

```
**API Local Endpoint:** 
- GET http://127.0.0.1:5000/verb?language=ita&verb=mangiare

