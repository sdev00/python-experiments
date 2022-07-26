def area_of_polygon(points):
    """
    Calculate the area of a complex polygon.
    """
    area = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    area = abs(area) / 2
    return area


def main():
    """
    Main function.
    """
    points = [(0, 0), (1, 1), (-10, 20), (10, 10), (50, 30)]
    print(area_of_polygon(points))

# Run the main function.
if __name__ == '__main__':
    main()