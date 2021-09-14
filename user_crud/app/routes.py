from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)


from app.database import User


@app.route("/")
def home():
    out = {
        "status": "ok",
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return out


@app.route("/users")
def get_all_users():
    out = {
        "status": "ok",
        "message": "Success",
    }
    # out ["body"] = scan()
    users = User.query.all()                        #this line returns all users in user table
    out["body"] = []                                #create an empty list
    for user in users:                              #loop: for each user in users
        user_dict = {}                              #create a new temporary dictionary
        user_dict["id"] = user.id                   #map each user attribute to its corresponding key in the user_dict.
        user_dict["first_name"] = user.first_name
        user_dict["hobbies"] = user.hobbies
        user_dict["active"] = user.active
        out["body"].append(user.dict)               #append temporary dictionary to our empty list

    return out              
    


#     User(
#         first_name=user.data.get("first_name"),
        
#     )

#     for U
#     users = User.query.all()
#     out["body"]

# (first_name, last_name, hobbies):
#     db.session.add(
#         User(
#             first_name=first_name,
#             last_name=last_name,
#             hobbies=hobbies
#         )
#     )                        #we return out.


@app.route("/users/<int:pk>")
def get_single_user(pk):
    out = {
        "status": "ok",
        "message": "Success"
    }
    user = User.query.filter_by(id=pk).first()
    out["body"] = {
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "hobbies": user.hobbies,
            "active": user.active
        }
    }
    return out


# @app.route("/users", methods=["POST"])
# def create_user():
#     out = {
#         "status": "ok",
#         "message": "Success"
#     }
#     user_data = request.json
#     out["user_id"] = insert(
#         user_data.get("first_name"),
#         user_data.get("last_name"),
#         user_data.get("hobbies")
#     )
#     return out, 201


    
@app.route("/users" methods=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": Success",
    }
    user.data = request.json
    db.session.add(
        User(
            first_name = user_data.get("first_name"),
            last_name = user_data.get("last_name"),
            hobbies = user_data.get("hobbies")
        )
    )
    db.session.commit()

    return out, 201





@app.route("/users", methods=["PUT"])
def update_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = insert(
        user_data.put("first_name"),
        user_data.put("last_name"),
        user_data.put("hobbies")
    )
    return out, 201

@app.route('/agent')
def agent(): 
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent




