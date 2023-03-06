def find_center(rect):
    from Point import Point
    from Rectangle import Rectangle
    from print_point import print_point
    
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2

    print_point(p)

    return p