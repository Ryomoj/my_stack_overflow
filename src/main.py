import logging
import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).parent.parent))

logging.basicConfig(level=logging.DEBUG)

from src.api.questions import router as router_questions
from src.api.answers import router as router_answers

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.include_router(router_questions)
app.include_router(router_answers)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
