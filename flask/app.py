from flask import Flask, Response, session,jsonify, request, redirect, url_for
from pymongo import MongoClient
import json, secrets, random, string
from datetime import datetime

# Connect to our local MongoDB
#client = MongoClient("172.18.0.1",27017)
client = MongoClient('mongodb://mongodb:27017')


# Choose InfoSys database
db = client["DigitalAirlines"]
users_collection = db["users_collection"]
flights_collection = db["flights_collection"]
reservations_collection = db["reservations_collection"]

# Initiate Flask App
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Add an initial administrator to the users_collection
initial_admin = {
    "name": "John",
    "surname": "Doe",
    "email": "admin@example.com",
    "password": "admin",
    "date_of_birth": "01-01-2000",
    "country_of_origin": "Greece",
    "passport_number": "E20113",
    "role": "admin"
}

# Insert the initial_admin document into the users_collection
users_collection.insert_one(initial_admin)

flight1 = {
    "code": "ABC123",
    "departure_airport": "New York",
    "destination_airport": "London",
    "flight_date": "25-06-2023",
    "business_tickets_available": 50,
    "business_tickets_cost": 800,
    "economy_tickets_available": 100,
    "economy_tickets_cost": 400
}
flights_collection.insert_one(flight1)

flight2 = {
    "code": "DEF456",
    "departure_airport": "Los Angeles",
    "destination_airport": "Tokyo",
    "flight_date": "30-06-2023",
    "business_tickets_available": 20,
    "business_tickets_cost": 1200,
    "economy_tickets_available": 150,
    "economy_tickets_cost": 600
}
flights_collection.insert_one(flight2)

flight3 = {
    "code": "GHI789",
    "departure_airport": "London",
    "destination_airport": "Paris",
    "flight_date": "12-07-2023",
    "business_tickets_available": 30,
    "business_tickets_cost": 900,
    "economy_tickets_available": 80,
    "economy_tickets_cost": 350
}
flights_collection.insert_one(flight3)

user1 = {
    "name": "Nearchos",
    "surname": "Nikolaidis",
    "email": "nearchos@example.com",
    "password": "12345",
    "date_of_birth": "06-05-2002",
    "country_of_origin": "Greece",
    "passport_number": "ABC123456",
    "role": "simple"
}
users_collection.insert_one(user1)

def generate_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return code

@app.route("/home")
def home():
    main_urls = [
        "/userRegistration (POST)",
        "/login (POST)"
    ]

    response = {
        "message": "Welcome to Digital Airlines! You have to register first if you are a simple user. If you are an admin you can login. If you want to POST, PUT OR DELETE data you should click Body --> form-data and fill key and value. If you want to GET data you should click Params and fill key and value. Please provide the date in the format dd-mm-yyyy.",
        "main_urls": main_urls
    }

    return jsonify(response)

@app.route("/adminHome")
def adminHome():
    admin_urls = [
        "/createFlight (POST)",
        "/updateTicketsPrice (PUT)",
        "/deleteFlight (DELETE)",
        "/searchFlight (GET)",
        "/flightDetails (GET)",
        "/logout (POST)"
    ]

    response = {
        "message": "Welcome Admin to Digital Airlines! If you want to POST, PUT OR DELETE data you should click Body --> form-data and fill key and value. If you want to GET data you should click Params and fill key and value.  Please provide the date in the format dd-mm-yyyy.",
        "admin_urls": admin_urls
        
    }

    return jsonify(response)

@app.route("/simpleUserHome")
def simpleUserHome():
    simple_urls = [
        "/searchFlight (GET)",
        "/flightDetails (GET)",
        "/makeReservation (POST)",
        "/displayReservations (GET)",
        "/displayReservationDetails (GET)",
        "/cancelReservation (DELETE)",
        "/deleteAccount (DELETE)",
        "/logout "
    ]

    response = {
        "message": "Welcome Simple User to Digital Airlines! If you want to POST, PUT OR DELETE data you should click Body --> form-data and fill key and value. If you want to GET data you should click Params and fill key and value.  Please provide the date in the format dd-mm-yyyy.",
        "simple_user_urls": simple_urls
    }

    return jsonify(response)

@app.route("/userRegistration", methods=["POST"])
def user_registration():
    try:
        user_data = {
            "name": request.form.get("name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
            "date_of_birth": datetime.strptime(request.form.get("date_of_birth"), "%d-%m-%Y").strftime("%d-%m-%Y"),
            "country_of_origin": request.form.get("country_of_origin"),
            "passport_number": request.form.get("passport_number"),
            "role": "simple"
        }

        if user_data.get("role") == "simple" and not all(user_data.get(field) for field in ["name", "surname", "password", "date_of_birth", "country_of_origin", "passport_number"]):
            return Response("Incomplete data was given"), 400

        # Check if user with the same email already exists
        if users_collection.find_one({"email": user_data["email"]}):
            return Response("User with the same email already exists"), 400
        else:
            # Insert the user data into the users_collection
            users_collection.insert_one(user_data)
            return Response("User registration successful with the given email: {}".format(user_data["email"])), 200

    except ValueError:
        return Response("Invalid date format. Please provide the date of birth in the format dd-mm-yyyy."), 400

@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("email")
    password = request.form.get("password")

    user = users_collection.find_one({'email': email, 'password': password})

    if user["email"] is not None: # Check if user exists
        session['email'] = email
        session['role'] = user['role']
        session.permanent = True

        if user['role'] == 'admin':
            return redirect(url_for('adminHome'))
        elif user['role'] == 'simple':
            return redirect(url_for('simpleUserHome'))
    else:
        return Response("Wrong email or password."), 401

    return Response("Wrong email or password.", 401)  # Additional response for incorrect email or password

@app.route("/createFlight", methods=["POST"]) # admin 
def createFlight():
    
    if 'email' in session and session['role'] == 'admin':
        try:
            flight_data = {
                "code": generate_code(),
                "departure_airport": request.form.get("departure_airport"),
                "destination_airport": request.form.get("destination_airport"),
                "flight_date": datetime.strptime(request.form.get("flight_date"), "%d-%m-%Y").strftime("%d-%m-%Y"),
                "business_tickets_available": request.form.get("business_tickets_available"),
                "business_tickets_cost": request.form.get("business_tickets_cost"),
                "economy_tickets_available": request.form.get("economy_tickets_available"),
                "economy_tickets_cost": request.form.get("economy_tickets_cost")
            }

            if flight_data.get("code") is not None and not all(flight_data.get(field) for field in ["departure_airport", "destination_airport", "flight_date", "business_tickets_available", "business_tickets_cost", "economy_tickets_available","economy_tickets_cost"]):
                return Response("Incomplete data was given"), 400
            flights_collection.insert_one(flight_data)

        except ValueError:
            return Response("Invalid date format. Please provide the date in the format dd-mm-yyyy."), 400
        
        return Response("The flight(code: {}) with departure from {} and destination to {} was added to the MongoDB".format(flight_data['code'],flight_data['departure_airport'], flight_data['destination_airport'])), 200
    
    else:
        return Response("Unauthorized access."), 401

@app.route("/updateTicketsPrice", methods=["PUT"]) # admin
def updateTicketsPrice():
    if 'email' in session and session['role'] == 'admin':
        flight_code = request.form.get("flight_code")
        new_business_tickets_cost = request.form.get("new_business_tickets_cost")
        new_economy_tickets_cost = request.form.get("new_economy_tickets_cost")

        if not all([flight_code, new_business_tickets_cost, new_economy_tickets_cost]):
            return Response("Incomplete data provided"), 400

        # Update the flight ticket prices in the database
        flight = flights_collection.update_one(
            {"code": flight_code},
            {
                "$set": {
                    "business_tickets_cost": new_business_tickets_cost,
                    "economy_tickets_cost": new_economy_tickets_cost
                }
            }
        )

        if flight.modified_count == 0:
            return Response("Flight not found"), 404
        
        flight = flights_collection.find_one({"code":flight_code})
        flight_data = {
        "departure_airport": flight["departure_airport"],
        "destination_airport": flight["destination_airport"],
        "flight_date": flight["flight_date"],
        "business_tickets_available": flight["business_tickets_available"],
        "business_tickets_cost": flight["business_tickets_cost"],
        "economy_tickets_available": flight["economy_tickets_available"],
        "economy_tickets_cost": flight["economy_tickets_cost"]
    }
        return Response("Ticket prices updated for flight {} \n The updated data: {}".format(flight_code,flight_data)), 200

    else:
        return Response("Unauthorized access."), 401

@app.route("/deleteFlight", methods=["DELETE"]) # admin
def deleteFlight():
    if 'email' in session and session['role'] == 'admin':
        flight_code = request.form.get("flight_code")

        flight = flights_collection.find_one({"code": flight_code})

        if flight:
            reservations = reservations_collection.find_one({"reservation_code": flight_code})

            if reservations:
                return Response("Flight cannot be deleted as there are existing reservations."), 403
            else:
                flights_collection.delete_one({"code": flight_code})
                return Response("Flight deleted successfully."), 200
        else:
            return Response("Flight not found."), 404
    else:
        return Response("Unauthorized access."), 401

@app.route("/makeReservation", methods=["POST"]) # simple
def makeReservation():
    if 'email' in session and session['role'] == 'simple':
        try:
            flight_code = request.form.get("flight_code")
            reservation_data = {
                "first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name"),
                "passport_number": request.form.get("passport_number"),
                "date_of_birth": datetime.strptime(request.form.get("date_of_birth"), "%d-%m-%Y").strftime("%d-%m-%Y"),
                "email": request.form.get("email"),
                "ticket_class": request.form.get("ticket_class")
            }

            if not all(reservation_data.get(field) for field in ["first_name", "last_name", "passport_number", "date_of_birth", "email", "ticket_class"]):
                return Response("Incomplete passenger information."), 400

            flight = flights_collection.find_one({"code": flight_code})
            if not flight:
                return Response("Flight not found."), 404

            # Check ticket availability based on the ticket class
            ticket_class = reservation_data['ticket_class']
            if ticket_class == 'business' and flight['business_tickets_available'] <= 0:
                return Response("No business class tickets available for this flight."), 400
            elif ticket_class == 'economy' and flight['economy_tickets_available'] <= 0:
                return Response("No economy class tickets available for this flight."), 400

            # Reduce available ticket count
            if ticket_class == 'business':
                flights_collection.update_one({"code": flight_code}, {"$inc": {"business_tickets_available": -1}})
            elif ticket_class == 'economy':
                flights_collection.update_one({"code": flight_code}, {"$inc": {"economy_tickets_available": -1}})
            else:
                return Response("There isn't such a ticket class."), 400

            # Save reservation details
            reservations_collection.insert_one({
                "reservation_code": flight_code,
                "reservation_data": reservation_data
            })

            return Response("Ticket booked successfully for flight {} in {}.".format(flight_code,ticket_class)), 200

        except ValueError:
            return Response("Invalid date format. Please provide the date in the format dd-mm-yyyy."), 400

    else:
        return Response("Unauthorized access."), 401
    
@app.route("/displayReservations", methods=["GET"]) # simple error empty reservation but it is the same format as the def flightDetails()
def displayReservations():
    if 'email' in session and session['role'] == 'simple':
        user_email = session['email']
        reservations = reservations_collection.find({"email": user_email})

        
        if reservations:
            response= {
                'user_email': user_email,
                'reservations': []
            }
            for reservation in reservations:
                reservation_data = reservation["reservation_data"]
                reservation_details = {
                    "reservation_code": reservation_data["reservation_data"],
                    "passenger_name": reservation_data["first_name"] + " " + reservation_data["last_name"],
                    "passport_number": reservation_data["passport_number"],
                    "date_of_birth": reservation_data["date_of_birth"],
                    "email": reservation_data["email"],
                    "ticket_class": reservation_data["ticket_class"]
                }

                response["reservations"].append(reservation_details)
            return json.dumps(response), 200
        else:
            return Response("No reservations found for the user with email: {}".format(user_email)), 404

    else:
        return Response("Unauthorized access."), 401

@app.route("/displayReservationDetails", methods=["GET"]) # simple
def displayReservationDetails():
    if 'email' in session and session['role'] == 'simple':
        reservation_code = request.args.get("reservation_code")
        reservation = reservations_collection.find_one({"reservation_code": reservation_code})

        if not reservation:
            return Response("Reservation not found."), 404
        else:
            flight_code = reservation["reservation_code"]
            flight = flights_collection.find_one({"code": flight_code})

            if not flight:
                return Response("Flight not found."), 404
            else:
                reservation_data = reservation["reservation_data"]
                reservation_details = {
                    "departure_airport": flight["departure_airport"],
                    "destination_airport": flight["destination_airport"],
                    "flight_date": flight["flight_date"],
                    "passenger_name": reservation_data["first_name"] + " " + reservation_data["last_name"],
                    "passport_number": reservation_data["passport_number"],
                    "date_of_birth": reservation_data["date_of_birth"],
                    "email": reservation_data["email"],
                    "ticket_class": reservation_data["ticket_class"]
                }
                

                return  json.dumps(reservation_details), 200

    else:
        return Response("Unauthorized access."), 401

@app.route("/cancelReservation", methods=["DELETE"]) # simple
def cancelReservation():
    if 'email' in session and session['role'] == 'simple':
        reservation_code = request.args.get("reservation_code")
        reservation = reservations_collection.find_one({"reservation_code": reservation_code})

        if not reservation:
            return Response("Reservation not found."), 404
        else:
            flight_code = reservation["reservation_code"]
            flight = flights_collection.find_one({"code": flight_code})

            if not flight:
                return Response("Flight not found."), 404
            else:
                # Increase available ticket count based on ticket class
                ticket_class = reservation["reservation_data"]["ticket_class"]
                if ticket_class == 'business':
                    flights_collection.update_one({"code": flight_code}, {"$inc": {"business_tickets_available": 1}})
                elif ticket_class == 'economy':
                    flights_collection.update_one({"code": flight_code}, {"$inc": {"economy_tickets_available": 1}})

                # Delete the reservation
                reservations_collection.delete_one({"reservation_code": reservation_code})

                return Response("Reservation with code {} has been canceled.".format(reservation_code)), 200

    else:
        return Response("Unauthorized access."), 401

@app.route("/deleteAccount", methods=["DELETE"]) # simple
def deleteAccount():
    if 'email' in session and session['role'] == 'simple':
        user_email = session['email']

        # Delete the user account
        users_collection.delete_one({"email": user_email})

        # Clear the session
        session.clear()

        return Response("Account deleted successfullyfor user {}.".format(user_email)), 200

    else:
        return Response("Unauthorized access."), 401

@app.route("/searchFlight", methods=["GET"]) # admin and simple 
def searchFlight():
    if 'email' in session:
        query_type = request.args.get("query_type")

        if query_type == "by_airports":
            # Search based on departure airport and destination airport
            departure_airport = request.args.get("departure_airport")
            destination_airport = request.args.get("destination_airport")
            flights = flights_collection.find({
                "departure_airport": departure_airport,
                "destination_airport": destination_airport
            })

        elif query_type == "by_airports_and_date":
            # Search based on departure airport, destination airport, and flight date
            departure_airport = request.args.get("departure_airport")
            destination_airport = request.args.get("destination_airport")
            flight_date = request.args.get("flight_date")
            flights = flights_collection.find({
                "departure_airport": departure_airport,
                "destination_airport": destination_airport,
                "flight_date": flight_date
            })

        elif query_type == "by_date":
            # Search based on flight date
            flight_date = request.args.get("flight_date")
            flights = flights_collection.find({
                "flight_date": flight_date
            })

        elif query_type == "all":
            # Retrieve all available flights
            flights = flights_collection.find()

        else:
            return Response("Invalid query type.  (ex: http://localhost:5000/searchFlight?query_type=all)"), 400

        flight_list = []
        for flight in flights:
            flight_info = {
                "flight_code": flight["code"],
                "flight_date": flight["flight_date"],
                "departure_airport": flight["departure_airport"],
                "destination_airport": flight["destination_airport"]
            }
            flight_list.append(flight_info)

        response = {
            "message": "Flight search results:",
            "flights": flight_list
        }

        return json.dumps(response), 200
    
    else:
        return Response("Unauthorized access."), 401

@app.route("/flightDetails", methods=["GET"]) # admin and simple
def flightDetails():
    if 'email' in session:
        flight_code = request.args.get("flight_code")
        flight = flights_collection.find_one({"code": flight_code})

        if flight:
            # Retrieve flight details
            departure_airport = flight["departure_airport"]
            destination_airport = flight["destination_airport"]
            total_tickets = int(flight["economy_tickets_available"]) + int(flight["business_tickets_available"])
            total_economy_tickets = int(flight["economy_tickets_available"])
            total_business_tickets = int(flight["business_tickets_available"])
            economy_ticket_cost = float(flight["economy_tickets_cost"])
            business_ticket_cost = float(flight["business_tickets_cost"])

            # Retrieve reservations for the flight
            reservations = reservations_collection.find({"reservation_code": flight_code})

            # Prepare flight details JSON object
            flight_details = {
                "flight_code": flight_code,
                "departure_airport": departure_airport,
                "destination_airport": destination_airport,
                "total_tickets": total_tickets,
                "total_economy_tickets": total_economy_tickets,
                "total_business_tickets": total_business_tickets,
                "economy_ticket_cost": economy_ticket_cost,
                "business_ticket_cost": business_ticket_cost,
                "reservations": []
            }
            
           
            # Prepare reservations JSON objects
            for reservation in reservations:
                reservation_data = reservation["reservation_data"]
                reservation_details = {
                    "passenger_name": reservation_data["first_name"] + " " + reservation_data["last_name"],
                    "ticket_class": reservation_data["ticket_class"]
                }
                
                flight_details["reservations"].append(reservation_details)

            return json.dumps(flight_details), 200

        else:
            return Response("Flight not found. (http://localhost:5000/flightDetails?flight_code=xxxxxx)"), 404

    else:
        return Response("Unauthorized access."), 401
    
@app.route("/logout")
def logout():
    if 'email' in session:
        email = session['email']
        session.pop('email', None)
        session.pop('role', None)
        return Response("Logged out successfully for user {}.".format(email)), 200
    else:
        return Response("No active session."), 401


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True, port = 5000)