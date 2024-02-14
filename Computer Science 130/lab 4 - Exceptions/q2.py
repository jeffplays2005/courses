def get_semicircle_area(radius):
    try:
        radius = float(radius)
        a = (round(3.141592 * radius ** 2 / 2), '')
        if radius == 0:
            return (0, 'ERROR: Not a semicircle!')
        elif radius < 0:
            return (0, 'ERROR: radius must be positive!')
        return  a
    except ValueError:
        return (0, 'ERROR: The value is invalid!')
    except TypeError:
        return (0, 'ERROR: The type is incorrect!')
print(get_semicircle_area(10.5)) 
# (173, '')
print(get_semicircle_area(-1))
print(get_semicircle_area(0))
# (0, 'ERROR: radius must be positive!')
# (0, 'ERROR: Not a semicircle!')
print(get_semicircle_area('ten'))
# (0, 'ERROR: The value is invalid!')
print(get_semicircle_area([1,2,3]))
# (0, 'ERROR: The type is incorrect!')

print(get_semicircle_area('11.9'))
print(get_semicircle_area(4))