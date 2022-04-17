from flask import Blueprint
from termproject.controllers.UserController import signup, signin, activateUser, forgotPassword, resetPassword, heartTest, fetchRecords, delete
user_bp = Blueprint('user_bp', __name__)


#Auth routes

#signup route
user_bp.route('/signup', methods=['POST'])(signup)

#verication route
user_bp.route('/verify', methods=['GET'])(activateUser)

#login route
user_bp.route('/signin', methods=['POST'])(signin)

#forgot password route
user_bp.route('/forgotpassword', methods=['POST'])(forgotPassword)

#reset password route
user_bp.route('/resetpassword', methods=['POST'])(resetPassword)


#admin panel routes

#route to test the model
user_bp.route('/hearttest', methods=['POST'])(heartTest)

#route to fetch all the records based on logged in user
user_bp.route('/fetchrecords', methods=['POST'])(fetchRecords)




