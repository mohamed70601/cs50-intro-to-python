import sys


def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    lagitude, longitude = coordinates_tuple

    print(f"Latitude: {lagitude}")
    print(f"Longitude: {longitude}")

    # tuples are more memory efficient
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")


main()
