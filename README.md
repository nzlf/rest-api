# Portfolio REST API

Portfolio REST API adalah backend sederhana untuk mengelola data project portofolio menggunakan FastAPI, SQLAlchemy, dan SQLite.

## Fitur

- Menampilkan semua project
- Menampilkan detail project berdasarkan ID
- Menambahkan project baru
- Mengupdate project
- Menghapus project
- Dokumentasi API otomatis dengan Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Instalasi

Clone repository lalu masuk ke folder project:

```bash
git clone https://github.com/nzlf/rest-api.git
cd portfolio-api
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan server:

```bash
uvicorn app.main:app --reload
```

## Akses Aplikasi

Root endpoint:

```txt
http://127.0.0.1:8000/
```

Swagger docs:

```txt
http://127.0.0.1:8000/docs
```

## Endpoint API

### GET /projects
Mengambil semua data project.

### GET /projects/{project_id}
Mengambil detail project berdasarkan ID.

### POST /projects
Menambahkan project baru.

Contoh request body:

```json
{
  "title": "Portfolio Website",
  "description": "Website portofolio pribadi dengan backend FastAPI",
  "tech_stack": "FastAPI, SQLite, HTML, CSS",
  "github_url": "https://github.com/nzlf/rest-api",
  "demo_url": "https://myportfolio.com"
}
```

### PUT /projects/{project_id}
Mengupdate data project berdasarkan ID.

### DELETE /projects/{project_id}
Menghapus data project berdasarkan ID.

## Cara Menjalankan Project

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Author

Nazala Furqon