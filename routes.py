from fastapi import APIRouter
from data_fetcher import fetch_data
from ai_analyzer import analyze_data
from report_generator import generate_report

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze_sector(sector: str):
    data = fetch_data(sector)
    analysis = analyze_data(data)
    report = generate_report(sector, analysis)
    return {"report": report}