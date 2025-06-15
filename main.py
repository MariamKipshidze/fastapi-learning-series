from fastapi import FastAPI
from users.routes import router as users_router
from blog.routes import router as blog_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(blog_router, prefix="/blogs", tags=["Blogs"])
