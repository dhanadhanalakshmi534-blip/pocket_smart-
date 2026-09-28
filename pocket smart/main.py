from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from gemini_utils import get_ai_recommendation

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"result": None})

# UPDATED to match your HTML exactly: "/home-budget" and "room_type"
@app.post("/home-budget")
async def generate_home(request: Request, budget: str = Form(...), room_type: str = Form(...)):
    
    prompt = f"Act as an interior design expert. I have a budget of ₹{budget} to furnish this room: {room_type}. Recommend specific, cost-effective furniture and decor from platforms like IKEA and Amazon. Ensure it fits the budget. Format your response using basic HTML tags like <h3>, <p>, <ul>, <li>, and <strong>. Do NOT use markdown."
    
    ai_output = get_ai_recommendation(prompt)
    
    return templates.TemplateResponse(request=request, name="index.html", context={"result": ai_output})