from flask import Flask, jsonify
import folium

app = Flask(__name__)

@app.route("/")
def home():
    # יצירת מפה עולמית
    world_map = folium.Map(
        location=[20, 0],   # מרכז העולם
        zoom_start=2,
        tiles="OpenStreetMap"
    )

    # הוספת Marker לדוגמה
    folium.Marker(
        location=[31.77, 35.21],
        popup="Jerusalem",
        icon=folium.Icon(color="blue")
    ).add_to(world_map)

    # החזרת המפה כ-HTML
    return world_map._repr_html_()

@app.route("/health")
def health_check():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

