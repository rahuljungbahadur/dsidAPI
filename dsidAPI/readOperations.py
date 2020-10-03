from sqlalchemy.orm import Session

from . import dataModels, schemas, functions


def get_ingredient(db: Session, name: str):
    firstQ =  db.query(dataModels.Ingredient).filter(dataModels.Ingredient.name == name).all()

    LabelList = []
    for i in firstQ:
        LabelList.append(i.label)


    return LabelList  ## This works


#def get_user_by_email(db: Session, email: str):
#    return db.query(models.User).filter(models.User.email == email).first()

def getAllDefault(db: Session, product : int, ingredient : str, label : float):

    if ingredient and label:
        ingredResult = db.query(dataModels.Ingredient).filter(dataModels.Ingredient.product == product,
         dataModels.Ingredient.name == ingredient).first()
        
        ##Mean Estimate
        meanParams = [ingredResult.pm0, ingredResult.pm1, ingredResult.pm2]
        meanEstimate = round(functions.parameterEstimate(meanParams, label), 2)

        ## StdError Estimate
        stdErrorParams = [ingredResult.sem0, ingredResult.sem1, ingredResult.sem2, ingredResult.sem3,
         ingredResult.sem4, ingredResult.sem5, ingredResult.sem6, ingredResult.sem7, ingredResult.sem8, ingredResult.sem9]

        stdErrorEstimate = round(functions.parameterEstimate(stdErrorParams, label), 2)

        ## 

        returnDict = [dict(product = ingredResult.product, name = ingredResult.name,
         min = ingredResult.min, max = ingredResult.max, label = label, meanEstimate = meanEstimate,
         meanStdError = stdErrorEstimate)]

        return returnDict


    else :
        ingredResult = db.query(dataModels.Ingredient).filter(dataModels.Ingredient.product == product).all()

        results = []
        for ingredRow in ingredResult:

            ## Mean Estimate
            meanParams = [ingredRow.pm0, ingredRow.pm1, ingredRow.pm2]
            meanEstimate = round(functions.parameterEstimate(meanParams, ingredRow.label), 2)

            ##StdError Estimate
            stdErrorParams = [ingredRow.sem0, ingredRow.sem1, ingredRow.sem2, ingredRow.sem3, 
            ingredRow.sem4, ingredRow.sem5, ingredRow.sem6, ingredRow.sem7, ingredRow.sem8, ingredRow.sem9]

            stdErrorEstimate = round(functions.parameterEstimate(stdErrorParams, ingredRow.label), 2)

            returnDict = dict(product = ingredRow.product, name = ingredRow.name, 
            min = ingredRow.min, max = ingredRow.max, label = ingredRow.label, meanEstimate = meanEstimate,
            meanStdError = stdErrorEstimate)

            results.append(returnDict)



        return results

def getSomeResult(db: Session):
    twoVal = db.query(dataModels.Ingredient).filter(dataModels.Ingredient.product == 'CALCIUM').first()

    return twoVal.min