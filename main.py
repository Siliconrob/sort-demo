from numbers import Number

from fastapi import FastAPI
import pydantic
from pydantic import StrictFloat
from starlette.middleware.exceptions import ExceptionMiddleware

from middleware.exceptionhandler import ExceptionHandlerMiddleware
from sort import sort

app = FastAPI()

app.add_middleware(ExceptionHandlerMiddleware)

class SortRequest(pydantic.BaseModel):
    width: StrictFloat
    height: StrictFloat
    length: StrictFloat
    mass: StrictFloat


class SortResponse(pydantic.BaseModel):
    type: str

@app.post("/sort")
async def sort_classifier(input_args: SortRequest) -> SortResponse:
    return SortResponse(type=sort(input_args.width, input_args.height, input_args.length, input_args.mass))
