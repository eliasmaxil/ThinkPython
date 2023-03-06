def move_rectangle(rect,dx,dy):
    from Point import Point
    from Rectangle import Rectangle
    from print_point import print_point
    
    p = Point()
    p.x = rect.corner.x + dx
    p.y = rect.corner.y + dy

    print_point(p)

    return p