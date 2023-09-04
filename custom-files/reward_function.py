def reward_function(params):

    speed_weight = 100
    heading_weight = 100
    steering_weight = 50

    max_speed_reward = 10 * 10
    min_speed_reward = 3.33 * 3.33
    abs_speed_reward = params['speed'] * params['speed']
    speed_reward = (abs_speed_reward - min_speed_reward) / (max_speed_reward - min_speed_reward) * speed_weight
    
    
    if not params['all_wheels_on_track']:
        return 1e-3
    
    
    next_point = params['waypoints'][params['closest_waypoints'][1]]
    prev_point = params['waypoints'][params['closest_waypoints'][0]]

    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    track_direction = math.degrees(track_direction)

    direction_diff = abs(track_direction - params['heading'])
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    
    abs_heading_reward = 1 - (direction_diff / 180.0)
    heading_reward = abs_heading_reward * heading_weight
        
    abs_steering_reward = 1 - (abs(params['steering_angle'] - direction_diff) / 180.0)
    steering_reward = abs_steering_reward * steering_weight

    
    return speed_reward + heading_reward + steering_reward


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