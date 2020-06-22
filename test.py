from sys import exit
import time
save_car = []

def intro_user():
    global save_car
    print("Hello user. I haven't met you. ")
    name = input(" What is your name? ")
    save_car.append("Name:" + name)
    # Welcoming and Presentation message.
    print(f"""
    Hi {name}, Welcome to the Tesla Factory.
    Thank you for choosing us.
    First, tell us which model do you want?.
    """)
    model_choice()

def model_choice():
    global save_car
    
    exit = False
    while exit == False:
        exit = True
        print("All cars have Dual Motor All-Wheel Drive, adaptive air suspension, premium interior and sound.\nThe list of models are:\n\t1: Model S\t5: Cybertruck\n\t2: Model 3\t6: Roadster\n\t3: Model X\t7: Semi\n\t4: Model Y")
        choose = input("> ")
        if choose == "1":
            save_car.append("Tesla: Model S")
            model_s()
        elif choose == "2":
            save_car.append("Tesla: Model 3")
            model_3()
        elif choose == "3":
            save_car.append("Tesla: Model X")
            model_x()
        elif choose == "4":
            save_car.append("Tesla: Model Y")
        elif choose == "5":
            save_car.append("Tesla: Cybertruck")
        elif choose == "6":
            save_car.append("Tesla: Roadster")
        elif choose == "7":
            save_car.append("Tesla: Semi")
        else:
            print("Please, choose a model!")
            exit = False
# -------------------------------------------------------------------------------------------
# -------------------------------------- TESLA MODEL S --------------------------------------
# -------------------------------------------------------------------------------------------
def model_s():
    global save_car
    print("Choose your category: ")
    print("\t1. Long Range Plus: $69,490\t2. Performance: $89,490")
    
    exit = False
    while exit == False:
        exit = True
        category_model_s = input("> ")
        if category_model_s == "1":
            save_car.append("Category: Long Range Plus")
            exterior_model_s()
        elif category_model_s == "2":
            save_car.append("Category: Performance")
            exterior_model_s()
        else:
            print("Please, choose a category!")
            exit = False

def exterior_model_s():
    global save_car
    print("Choose your favorite color:\n\t1. Pearl White Multi-Coat\t4. Solid Black\n\t2. Midnight Silver Metallic\t5. Deep Blue Metallic\n\t3. Red Multi-Coat\n")
    print("The price are:\n Pearl White $0,00\n Red Multi-Coat: $2,500.\n The others color coast $1,500.")
    
    exit = False
    while exit == False:
        exit = True
        color_model_s = input("> ")
        if color_model_s == "1":
            save_car.append("Color: Pearl White Multi-Coat")
            wheel_model_s()
        elif color_model_s == "2":
            save_car.append("Color: Midnight Silver Metallic")
            wheel_model_s()
        elif color_model_s == "3":
            save_car.append("Color: Red Multi-Coat")
            wheel_model_s()
        elif color_model_s == "4":
            save_car.append("Color: Solid Black")
            wheel_model_s()
        elif color_model_s == "5":
            save_car.append("Color: Deep Blue Metallic")
            wheel_model_s()
        else:
            print("Please, choose a color!")
            exit = False

def wheel_model_s():
    global save_car
    print("Now, which kind of wheels do you want:")
    print("\t1. 19\" Tempest Wheels\t3. 21\" Sonic Carbon Twin Turbine Wheels\n\t2. 19\" Sonic Carbon Slipstream Wheels\n")
    print("The prices are:\n 19\" Tempest Wheels: $0,00\n 19\" Sonic Carbon Slipstream Wheels: $1,500\n 21\" Sonic Carbon Twin Turbine Wheels: $4,500")

    exit = False
    while exit == False:
        exit = True
        wheel_choice_model_s = input("> ")
        if wheel_choice_model_s == "1":
            save_car.append("Wheels: 19\" Tempest Wheels")
            interior_model_s()
        elif wheel_choice_model_s == "2":
            save_car.append("Wheels: 19\" Sonic Carbon Slipstream Wheels")
            interior_model_s()
        elif wheel_choice_model_s == "3":
            save_car.append("Wheels: 21\" Sonic Carbon Twin Turbine Wheels")
            interior_model_s()
        else:
            print("Please, choose a type of wheels.")
            exit = False

def interior_model_s():
    global save_car
    print("Let's selected your interior:")
    print("." * 90)
    print("""
Includes:

* Premium audio system specifically tuned for a Tesla’s ultra-quiet cabin
* Cold weather features including heated seats for every passenger, heated steering wheel, wiper blade defrosters and washer nozzle heaters
* HEPA air filtration system prevents viruses, bacteria and offensive odors from entering the cabin

* Premium Connectivity (1 year included):
\t-Satellite maps with live traffic visualization
\t-In-car internet streaming music and media
\t-Video streaming
\t-Caraoke
\t-Internet browser

* Music and media over Bluetooth
* Location-aware automatic garage door opener
* LED fog lamps
* Tinted glass roof with ultraviolet and infrared protection
* Auto dimming, power folding, heated side mirrors
* Custom driver profiles
* Wireless phone charging in center console
""")
    print("." * 90)
    print("The colors choices are:\n\t1. All Black\t3. Cream\n\t2. Black & White\n")
    print("The price are:\n All Black w\\ Figured Ash Wood Décor: $0.00\n Black & White w\\ Dark Ash Wood Décor: $1,500\n Cream w\\ Oak Wood Décor: $1,500")

    exit = False
    while exit == False:
        exit = True
        interior_choice_model_s = input("> ")
        if interior_choice_model_s == "1":
            save_car.append("Interior: All Black")
            autopilot()
        elif interior_choice_model_s == "2":
            save_car.append("Interior: Black & White")
            autopilot()
        elif interior_choice_model_s == "3":
            save_car.append("Interior: Cream")
            autopilot()
        else:
            print("Please, choose the color interior.")
            exit = False

def autopilot():
    global save_car
    print("." * 90)
    print("""
* Autopilot Included
\t-Enables your car to steer, accelerate and brake automatically for other vehicles and pedestrians within its lane.

* Full Self-Driving Capability
\t-Navigate on Autopilot: automatic driving from highway on-ramp to off-ramp including interchanges and overtaking slower cars.
\t-Auto Lane Change: automatic lane changes while driving on the highway.
\t-Autopark: both parallel and perpendicular spaces.
\t-Summon: your parked car will come find you anywhere in a parking lot. Really.
\t-Traffic Light and Stop Sign Control: assisted stops at traffic controlled intersections.

* Upcoming:
\t-Autosteer on city streets.

**Select Full Self-Driving Option**
$7,000
\t-Includes the Full Self Driving Computer
\t-Full Self-Driving Capability is available for purchase post-delivery, prices are likely to increase over time with new feature releases
    """)
    print("." * 90)

    exit = False
    while exit == False:
        exit = True
        autopilot_choice = input("> [Yes/No] ")
        autopilot_choice = autopilot_choice.lower()
        if autopilot_choice == "yes":
            save_car.append("Autopilot: Full Self-Driving")
        elif autopilot_choice == "no":
            exit = True
        else:
            exit = False
# -------------------------------------------------------------------------------------------
# -------------------------------------- TESLA MODEL 3 --------------------------------------
# -------------------------------------------------------------------------------------------
def model_3():
    global save_car
    print("Choose your category: ")
    print("\t1. Long Range Plus: $40,690\t2. Performance: $48,690\nRear-Wheel Drive:\n\t3. Standard Range Plus $31,690")
    
    exit = False
    while exit == False:
        exit = True
        category_model_3 = input("> ")
        if category_model_3 == "1":
            save_car.append("Category: Long Range Plus")
            exterior_model_3()
        elif category_model_3 == "2":
            save_car.append("Category: Performance")
            exterior_model_3()
        elif category_model_3 == "3":
            save_car.append("Category: Standard Range Plus")
            exterior_model_3()
        else:
            print("Please, choose a category!")
            exit = False

def exterior_model_3():
    global save_car
    print("Choose your favorite color:\n\t1. Pearl White Multi-Coat\t4. Solid Black\n\t2. Midnight Silver Metallic\t5. Deep Blue Metallic\n\t3. Red Multi-Coat\n")
    print("The price are:\n Pearl White $0,00\n Red Multi-Coat: $2,000.\n The others color coast $1,000.")
    
    exit = False
    while exit == False:
        exit = True
        color_model_3 = input("> ")
        if color_model_3 == "1":
            save_car.append("Color: Pearl White Multi-Coat")
            wheel_model_3()
        elif color_model_3 == "2":
            save_car.append("Color: Midnight Silver Metallic")
            wheel_model_3()
        elif color_model_3 == "3":
            save_car.append("Color: Red Multi-Coat")
            wheel_model_3()
        elif color_model_3 == "4":
            save_car.append("Color: Solid Black")
            wheel_model_3()
        elif color_model_3 == "5":
            save_car.append("Color: Deep Blue Metallic")
            wheel_model_3()
        else:
            print("Please, choose a color!")
            exit = False

def wheel_model_3():
    global save_car
    print("Now, which kind of wheels do you want:")
    print("\t1. 18’’ Aero Wheels\t2. 19’’ Sport Wheels\n")
    print("The prices are:\n 18\" Aero Wheels: $0,00\n 19\" Sport Wheels: $1,500")

    exit = False
    while exit == False:
        exit = True
        wheel_choice_model_3 = input("> ")
        if wheel_choice_model_3 == "1":
            save_car.append("Wheels: 18\" Aero Wheels")
            interior_model_3()
        elif wheel_choice_model_3 == "2":
            save_car.append("Wheels: 19\" Sport Wheels")
            interior_model_3()
        else:
            print("Please, choose a type of wheels.")
            exit = False

def interior_model_3():
    global save_car
    print("Let's selected your interior:")
    print("." * 90)
    print("""
    Includes:

* 12-way power adjustable heated front seats
* Premium seat material and trim
* Upgraded audio – immersive sound

* Premium Connectivity (30 days included):
\t-Satellite maps with live traffic visualization
\t-In-car internet streaming music and media
\t-Video streaming
\t-Caraoke
\t-Internet browser
* Music and media over Bluetooth®
* Tinted glass roof with ultraviolet and infrared protection
* Power folding, heated side mirrors
* Custom driver profiles
* Center console with storage, 4 USB ports and docking for 2 smartphones.
""")
    print("." * 90)
    print("The colors choices are:\n\t1. All Black\t2. Black & White\n")
    print("The price are:\n All Black: $0.00\n Black & White: $1,000")

    exit = False
    while exit == False:
        exit = True
        interior_choice_model_3 = input("> ")
        if interior_choice_model_3 == "1":
            save_car.append("Interior: All Black")
            autopilot()
        elif interior_choice_model_3 == "2":
            save_car.append("Interior: Black & White")
            autopilot()
        else:
            exit = False
# -------------------------------------------------------------------------------------------
# -------------------------------------- TESLA MODEL X --------------------------------------
# -------------------------------------------------------------------------------------------
def model_x():
    global save_car
    print("Choose your category: ")
    print("\t1. Long Range Plus: $74,690\t2. Performance: $94,690")
    
    exit = False
    while exit == False:
        exit = True
        category_model_x = input("> ")
        if category_model_x == "1":
            save_car.append("Category: Long Range Plus")
            exterior_model_x()
        elif category_model_x == "2":
            save_car.append("Category: Performance")
            exterior_model_x()
        else:
            print("Please, choose a category!")
            exit = False

def exterior_model_x():
    global save_car
    print("Choose your favorite color:\n\t1. Pearl White Multi-Coat\t4. Solid Black\n\t2. Midnight Silver Metallic\t5. Deep Blue Metallic\n\t3. Red Multi-Coat\n")
    print("The price are:\n Pearl White $0,00\n Red Multi-Coat: $2,500.\n The others color coast $1,500.")
    
    exit = False
    while exit == False:
        exit = True
        color_model_x = input("> ")
        if color_model_x == "1":
            save_car.append("Color: Pearl White Multi-Coat")
            wheel_model_x()
        elif color_model_x == "2":
            save_car.append("Color: Midnight Silver Metallic")
            wheel_model_x()
        elif color_model_x == "3":
            save_car.append("Color: Red Multi-Coat")
            wheel_model_x()
        elif color_model_x == "4":
            save_car.append("Color: Solid Black")
            wheel_model_x()
        elif color_model_x == "5":
            save_car.append("Color: Deep Blue Metallic")
            wheel_model_x()
        else:
            print("Please, choose a color!")
            exit = False

def wheel_model_x():
    global save_car
    print("Now, which kind of wheels do you want:")
    print("\t1. 20\" Silver Wheels\t2. 22\" Onyx Black Wheels\n")
    print("The prices are:\n 20\" Silver Wheels: $0,00\n 22\" Onyx Wheels: $5,500")

    exit = False
    while exit == False:
        exit = True
        wheel_choice_model_x = input("> ")
        if wheel_choice_model_x == "1":
            save_car.append("Wheels: 20\" Silver Wheels")
            interior_model_x()
        elif wheel_choice_model_x == "2":
            save_car.append("Wheels: 22\" Onyx Black Wheels")
            interior_model_x()
        else:
            print("Please, choose a type of wheels.")
            exit = False

def interior_model_x():
    global save_car
    print("Let's selected your interior:")
    print("." * 90)
    print("""
Includes:

* Self-presenting and closing front doors
* Premium audio system specifically tuned for a Tesla’s ultra-quiet cabin
* Cold weather features including heated seats for every passenger, heated steering wheel, wiper blade defrosters and washer nozzle heaters
* HEPA air filtration system prevents viruses, bacteria and offensive odors from entering the cabin

* Premium Connectivity (1 year included):
\t-Satellite maps with live traffic visualization
\t-In-car internet streaming music and media
\t-Video streaming
\t-Caraoke
\t-Internet browser

* Music and media over Bluetooth
* Location-aware automatic garage door opener
* LED fog lamps
* Tinted glass roof with ultraviolet and infrared protection
* Auto dimming, power folding, heated side mirrors
* Custom driver profiles
* Wireless phone charging in center console
""")
    print("." * 90)
    print("The colors choices are:\n\t1. All Black\t3. Cream\n\t2. Black & White\n")
    print("The price are:\n All Black w\\ Figured Ash Wood Décor: $0.00\n Black & White w\\ Dark Ash Wood Décor: $1,500\n Cream w\\ Oak Wood Décor: $1,500")

    exit = False
    while exit == False:
        exit = True
        interior_choice_model_x = input("> ")
        if interior_choice_model_x == "1":
            save_car.append("Interior: All Black")
            autopilot()
        elif interior_choice_model_x == "2":
            save_car.append("Interior: Black & White")
            autopilot()
        elif interior_choice_model_x == "3":
            save_car.append("Interior: Cream")
            autopilot()
        else:
            print("Please, choose the color interior.")
            exit = False
def interior_model_x_seat():
    global save_car
    print("Choose a number of seat:")
    print("\t1. Five Seat Interior\t3. Seven Seat Interior\n\t2. Six Seat Interior")
    print("Five Seat: $00,00\nSix Seat: $6,500\nSeven Seat: $3,500")

    exit = False
    while exit == False:
        exit = True
        interior_model_x_seat_choice = input("> ")
        if interior_model_x_seat_choice == "1":
            save_car.apprend("Seat: Five")
            autopilot()
        elif interior_model_x_seat_choice == "2":
            save_car.append("Seat: Six")
            autopilot()
        elif interior_model_x_seat_choice == "3":
            save_car.append("Seat: Seven")
            autopilot()
# -------------------------------------------------------------------------------------------
# -------------------------------------- TESLA MODEL Y --------------------------------------
# -------------------------------------------------------------------------------------------


Timer = time.asctime( time.localtime(time.time()) )
print("." * 45)
print("Local current time :", Timer)
print("." * 45)
intro_user()
print( "." * 25,"\nHere you're selection:\n","." * 25,"\n", save_car)