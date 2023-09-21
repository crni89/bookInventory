## Pokretanje
1. Pre pokretanja aplikacije potrebno je instalirati potrebne biblioteke unosom komande u terminalu: <br> `pip install -r requirements.txt`
2. Posle instalacije moze se pokrenuti aplikacija komandom u terminalu: <br> `uvicorn main:app --reload`
3. Aplikacija ce biti dostupna na: <br> `localhost:8000`
4. Testiranje API-a preko Swagger-a: <br> `localhost:8000/docs`

### Aplikacija radi osnovne CRUD operacije
Aplikacija za vodjenje evidencija knjiga ima par putanja(endpoints) za dodavanje, pretragu, izmenu i brisanje knjiga.
Knjige se cuvaju lokalno u aplikaciji.

Dodavanje knjige
: - URL(endpoint): `/books`
: - Metod: `POST`
: - Primer JSON-a <br> 
```json
{
  "id": 0,
  "naslov": "Naslov knjige",
  "autor": "Autor knjige",
  "isnb": "1234567890123",
  "datum": "20.09.2023."
}
```
: - Dodavanje knjige sa posebnim ID

Pregled svih knjiga
: - URL(endpoint): `/books`
: - Metod: `GET`
: - Prikaz liste svih knjiga

Pregled pojedinacne knjige po ID-u
: - URL(endpoint): `/books/{book_id}`
: - Metod: `GET`
: - Prikaz odredjene knjige sa odgovarajucim ID-om
: - `book_id`: ID knige koje se trazi

Izmenja knjige po ID-u
: - URL(endpoint): `/books/{book_id}`
: - Metod: `PUT`
: - Izmena odredjene knjige sa odgovarajucim ID-om
: - `book_id`: ID knige koje se izmenjuje

Brisanje knjige po ID-u
: - URL(endpoint): `/books/{book_id}`
: - Metod: `DELETE`
: - Brisanje odredjene knjige sa odgovarajucim ID-om
: - `book_id`: ID knige koje se izmenjuje