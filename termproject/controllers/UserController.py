import pymysql
import numpy as np
import pickle
from flask import jsonify, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from termproject.config import mysql
from termproject.utils.helpers import encodeToken, decodeToken, sendEmail

model = pickle.load(open('random_forest.pkl', 'rb'))

# helper methods

# check if account already exists
def accountExists(email):
    conn = None
    cursor = None
    params = [email]
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        count = cursor.execute('select * from users where email=%s', params)
        if count == 0:
            return False
        else:
            return True
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Adding user to the database
def signup():
    conn = None
    cursor = None
    _name = request.json['Name']
    _email = request.json['Email']
    _contact = request.json['Contact']
    _password = request.json['Password']
    print(request.json)
    if (accountExists(_email)):
        return jsonify({
            "msg": "Account already exists"
        })
    else:
        try:
            _hashed_password = generate_password_hash(_password)
            sql = "INSERT INTO users(name, email, password, contact, isActive) VALUES(%s, %s, %s, %s, %s)"
            data = (_name, _email, _hashed_password, _contact, '0')
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            token = encodeToken(_email)
            email_response = sendEmail(_email, _name, token, "verify")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    return jsonify({
        "msg": "Successfully added user."
    })


# Verify user through email link
def activateUser():
    conn = None
    cursor = None
    token = request.args.get('token')
    try:
        email = decodeToken(token)
        sql = "UPDATE users SET isActive=%s WHERE email=%s"
        data = (1, email)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return render_template("F:/Lambton/Sem1/thursday/Heart-Disease-classifier/admin/activation.html")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#signin user through email and password
def signin():
    conn = None
    cursor = None

    auth = request.json

    if not auth or not auth.get('Email') or not auth.get('Password'):
        # returns 401 if any email or / and password is missing
        return jsonify({
            'msg': 'Could not verify. Login required!'
        }
        )

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from users where email=%s', auth.get('Email'))
    user = cursor.fetchone()
    if not user:
        # returns 401 if user does not exist
        return jsonify({
            'msg': 'Could not verify. User does not exist!'
        }
        )

    if user['isActive'] == 0:
        return jsonify({
            'msg': 'Could not verify. User is not verified!'
        }
        )

    if check_password_hash(user['password'], auth.get('Password')):
        # generates the JWT Token
        token = encodeToken(user['email'])

        return jsonify({
            'msg': 'success. Login successful!',
            'token': token
        }
        )
    # returns 403 if password is wrong
    return jsonify({
        'msg': 'Could not verify. password is wrong!'
    }
    )

#Sending an email link to reset the password
def forgotPassword():
    _email = request.json['Email']
    token = encodeToken(_email)
    email_response = sendEmail(_email, "", token, "reset")
    return jsonify({
        'msg': 'success. Email sent successfully!',
    })

#function to reset the password
def resetPassword():
    conn = None
    cursor = None
    token = request.json['token']
    _password = request.json['Password']
    try:
        email = decodeToken(token)
        _hashed_password = generate_password_hash(_password)
        sql = "UPDATE users SET password=%s WHERE email=%s"
        data = (_hashed_password, email)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return jsonify({
            "msg": "Password change successful"
        })
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#function to call the model and test if a user have a heart disease
def heartTest():
    conn = None
    cursor = None
    age = request.json['age']
    sex = request.json['sex']
    cp = request.json['cp']
    trestbps = request.json['trestbps']
    chol = request.json['chol']
    fbs = request.json['fbs']
    restecg = request.json['restecg']
    thalach = request.json['thalach']
    exang = request.json['exang']
    oldpeak = request.json['oldpeak']
    slope = request.json['slope']
    ca = request.json['ca']
    thal = request.json['thal']
    token = request.json['token']
    user = getUserId(token)
    id = user[0]['id']

    array_features = [np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])]
    output = model.predict(array_features)
    print(output[0])
    try:
        sql = "INSERT INTO testrecords(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, userid, target) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, id, output[0])
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        if output == 1:
            return jsonify({
            "msg": "The patient is not likely to have heart disease!"
        })
        else:
            return jsonify({
            "msg": "The patient is likely to have heart disease!"
        })

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#fetching all the records based on user id
def fetchRecords():
    conn = None
    cursor = None
    token = request.json['token']
    user = getUserId(token)
    id = user[0]['id']
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM testrecords where userid = %s", id)
        rows = cursor.fetchall()
        return jsonify({
            "records": rows
        })
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#function to get the userid from the provided token
def getUserId(token):
    try:
        email = decodeToken(token)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id FROM users where email =  %s", email)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# deleting the user
def delete():
    conn = None
    cursor = None
    # try:
    #     conn = mysql.connect()
    #     cursor = conn.cursor()
    #     cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    #     conn.commit()
    #     return jsonify({
    #         "msg": "success"
    #     })
    # except Exception as e:
    #     print(e)
    # finally:
    #     cursor.close()
    #     conn.close()
