from flask import Flask, jsonify
import folium

app = Flask(__name__)

@app.route("/")
def home():
    # Create a world map centered at latitude 20, longitude 0
    world_map = folium.Map(
        location=[20, 0],
        zoom_start=2,
        tiles="OpenStreetMap"
    )

    # Add a marker for Jerusalem
    folium.Marker(
        location=[31.77, 35.21],
        popup="Jerusalem",
        icon=folium.Icon(color="blue")
    ).add_to(world_map)

    # Return the map as HTML
    return world_map._repr_html_()

@app.route("/health")
def health_check():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
