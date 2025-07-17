def bouncing_ball(h, bounce, window):
    bounces = 0
    bounce_height = h * bounce
    while bounce_height > window:
        bounce_height * bounce
        bounces += 1
    return bounces * 2

#Working solution

def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1