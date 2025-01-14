import os


# version 1 - saving require data in env -> The best option
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# version 2 - using "const" in Class which is importet, in file -> Worse option
# class Config:
#     app.config['SECRET_KEY'] = 'wdwdqdcqwcaf3fgr'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:secret@env-db/STX'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# version 3 - The worst option
# app.config['SECRET_KEY'] = 'wdwdqdcqwcaf3fgr'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:secret@env-db/STX'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False