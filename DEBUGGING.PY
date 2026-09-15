# ── driver_dispatch.py  (RideSurge Technologies · Core Dispatch Module) ──
# Business rules (Ops Manual v5.1):
#   
Rule A:  Driver can accept a PREMIUM ride ONLY IF all three hold:
#              
#   
#              
#   
#              
#              
driver_rating     
trips_completed   
car_type          
active_riders     
active_drivers    
rain              
is_new_user       
referral_code     
promo_active      
rating >= 4.7  AND  trips_completed >= 200  AND  car_type == "sedan"
Rule B:  SURGE pricing fires when the rider/driver ratio is AT LEAST 3 (>= 3)
AND it is currently raining.
Rule C:  FREE-RIDE coupon issued when customer is a new user AND at least one
of: (referral code used) OR (promo is active).
Existing users are NOT eligible, even if a promo is running.
= 4.8
= 150       
= "sedan"
= 114       
= 38
= True
= False     
= ""
= True
# below the required 200-trip threshold
# exactly 3 times active_drivers
# this is a returning customer, not a new one
# Rule A — Premium ride eligibility
can_take_premium = driver_rating >= 4.7 or trips_completed >= 200 or car_type == "sedan"
# Rule B — Surge pricing
surge_active = (active_riders / active_drivers) > 3 and rain == True
# Rule C — Free-ride coupon
free_ride_coupon = is_new_user and referral_code != "" or promo_active
print("Premium eligible:", can_take_premium)
print("Surge active:)   
", surge_active)
print("Free ride coupon:", free_ride_coupon