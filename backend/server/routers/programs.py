from fastapi import APIRouter
from server.database import programsCOL
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix='/programs',
    tags=['programs'],
    responses={404: {"description": "Not found"}}
)

flexEd = ['3778']

@router.get("/")
def specialisations_index():
    return "Index of programs"

@router.get("/getProgram/{code}")
def getProgram(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)
    del result["_id"]

    return result

@router.get("/getDuration/{code}")
def  getDuration(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['duration']

@router.get("/getUOC/{code}")
def  getUOC(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['UOC']

@router.get("/getFaculty/{code}")
def  getFaculty(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    result['faculty']

@router.get("/getDiscipline/{code}")
def getDiscipline(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['components']['disciplinary_component']

@router.get("/getDisciplineUOC/{code}")
def getDisciplineUOC(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['components']['disciplinary_component']['credits_to_complete']

@router.get("/getMajors/{code}")
def getMajor(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['components']['disciplinary_component']['Majors']

@router.get("/getFlex/{code}")
def getFlex(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['components']['FE']

@router.get("/getFlexUOC/{code}")
def getFlexUOC(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['components']['FE']['credits_to_complete']

# @router.get("/getFlexMinors/{code}")
# def getMinors(code):
#     query = { "code" : code }
#     result = programsCOL.find_one(query)

#     return result['components']['FE']['Minors']

@router.get("/getGenUOC/{code}")
def getGENUOC(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    return result['components']['GE']['credits_to_complete']

@router.get("/getMinors/{code}")
def getMinors(code):
    query = { "code" : code }
    result = programsCOL.find_one(query)

    if (code in flexEd):
        return result['components']['FE']['Minors']

    return result['components']['Minors']  