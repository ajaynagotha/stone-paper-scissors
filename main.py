from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.get("/play", response_class=HTMLResponse)
def play(request: Request, yourstr: str):
    yourdict = {'s': -1, "p": 0, "sc": 1}
    reverseDict = {-1: "Stone", 0: "Paper", 1: "Scissor"}

    if yourstr not in yourdict:
        result = {"error": "Invalid input. Use 's', 'p', or 'sc'."}
        return templates.TemplateResponse("index.html", {"request": request, "result": result})

    you = yourdict[yourstr]
    computer = random.choice([1, -1, 0])

    if computer == you:
        outcome = "Draw"
    elif (computer == -1 and you == 0) or (computer == 0 and you == 1) or (computer == 1 and you == -1):
        outcome = "You Win"
    else:
        outcome = "You Lose"

    result = {
        "You Chose": reverseDict[you],
        "Computer Chose": reverseDict[computer],
        "Result": outcome
    }

    return templates.TemplateResponse("index.html", {"request": request, "result": result})
