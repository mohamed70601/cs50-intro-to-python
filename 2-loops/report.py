def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft.update({"orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(sc):
    return f"""
    ========== REPORT ==========

    # * Name: {sc["name"]}
    # * Distance: {sc["distance"]} AU

    Name: {sc.get("name", "Unknown")}
    Distance: {sc.get("distance", "Unknown")} AU
    
    ============================
    """


main()
