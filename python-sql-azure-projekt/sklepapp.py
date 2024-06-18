from typing import Optional
from fastapi import FastAPI, Request, Header, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from variables import AZURE_SQL_CONNECTIONSTRING
import models

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/index/', response_class=HTMLResponse)
async def wyposazenie(
    request: Request, 
    hx_request: Optional[str] = Header(None),
    db: Session = Depends(get_db)
    ): 
    wyposazenie = db.query(models.Wyposazenie).all()
    context = {'request': request, 'wyposazenie': wyposazenie}
    return templates.TemplateResponse("index.html", context)

@app.post('/delete/', response_class=HTMLResponse)
async def usun_wyposazenie(
    request: Request,
    id: int = Form(...),
    hx_request: Optional[str] = Header(None),
    db: Session = Depends(get_db)
    ):
    #Usunięcie rekordu z bazy danych
    wyposazenie = db.query(models.Wyposazenie).filter(models.Wyposazenie.id == id).first()
    if wyposazenie:
        db.delete(wyposazenie)
        db.commit()
    wyposazenie = db.query(models.Wyposazenie).all()
    context = {'request': request, 'wyposazenie': wyposazenie}
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    

@app.post('/add/', response_class=HTMLResponse)
async def dodaj_wyposazenie(
    request: Request,
    nazwa: str = Form(...),
    wykonawca: str = Form(...),
    gatunek: str = Form(...),
    nosnik: str = Form(...),
    wydawnictwo: str = Form(...),
    wydano: str = Form(...),
    hx_request: Optional[str] = Header(None),
    db: Session = Depends(get_db)
    ):
    # Dodanie nowego rekordu do bazy danych
    nowe_wyposazenie = models.Wyposazenie(
        nazwa=nazwa,
        wykonawca=wykonawca,
        gatunek=gatunek,
        nosnik=nosnik,
        wydawnictwo=wydawnictwo,
        wydano=wydano
    )
    db.add(nowe_wyposazenie)
    db.commit()
    db.refresh(nowe_wyposazenie)
    
    # Pobierz zaktualizowaną listę wyposazenia
    wyposazenie = db.query(models.Wyposazenie).all()
    context = {'request': request, 'wyposazenie': wyposazenie}
    #Odpowiedz odpowiednim szablonem tylko dla tabeli
    if hx_request:
        return templates.TemplateResponse("table.html", context)
