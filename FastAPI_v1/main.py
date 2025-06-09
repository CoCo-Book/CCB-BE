from fastapi import FastAPI
from enum import Enum
from starlette.middleware.cors import CORSMiddleware

from fastapi.responses import FileResponse

from board import board_router
from user import user_router
from oauth import social_router

import models 
import os #
from dotenv import load_dotenv #
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from database import engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(board_router.app, tags=["[꼬꼬북] '나만의 동화' 게시판 for CRUD"])
app.include_router(user_router.app, tags=["[꼬꼬북] 일반 회원가입 for Email"])
app.include_router(social_router.app, tags=["[꼬꼬북] 소셜 회원가입 for Google"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    #return {"Hello": "World"}
    test_env = os.environ["TEST_ENV"]
    return {"result": test_env}