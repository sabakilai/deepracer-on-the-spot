def reward_function(params):
    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ( ( params["progress"] / params["steps"] ) * 100 )**2 + ( params["speed"]**2 ) 
    else:
        reward = 0.01
        
    return float(reward)


""" 
Action space:

Straight 
{"steering_angle": 0,"speed": 4}
{"steering_angle": 0,"speed": 3.5},
{"steering_angle": 0,"speed": 3}
{"steering_angle": 0,"speed": 2}

Left
{"steering_angle": 30, "speed": 2}
{"steering_angle": 10, "speed": 3.5},

Right 
{"steering_angle": -30,"speed": 2} 
{"steering_angle": -10, "speed": 3.5}
"""