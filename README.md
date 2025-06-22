# 📍 PythonGIS Buffer and Clip Automation 🚀

A simple geospatial Python project that automates the creation of buffer zones around police stations and clips them to sub-metropolitan boundaries in Kumasi, Ghana.

This was part of my personal learning journey in geospatial development using Python and GeoPandas, and I'm opening it up for others to learn from and collaborate on.

---

## 📌 What This Project Does

- Creates **500-meter buffers** around police stations in Kumasi.
- Clips these buffers to the sub-metro boundary shapefile.
- Generates a static map showing police stations, buffer areas, and sub-metro boundaries.
- Outputs a shapefile of the buffered, clipped police station areas.
- Optionally counts how many stations fall within each sub-metro.

---

## 📂 Project Structure
pythonGIS buffer and clip automation/
├── data/
│   ├── Kumasi_SubMetros.shp
│   ├── police_stations.shp
├── outputs/
│   ├── buffered_clipped_stations.shp
│   ├── buffered_map.png
│   └── station_counts.csv (optional)
├── scripts/
│   └── buffer_clip.py
├── README.md
└── .gitignore

---

## 📚 Tools & Libraries Used

- Python 3.11  
- GeoPandas  
- Matplotlib  
- Conda Environment (`gispro`)  
- Shapely (via GeoPandas)

---

## 📈 How to Run This Project

1. **Clone the repo**
   ```bash
   git clone https://github.com/BarbaraNyame/pythonGIS-buffer-clip-automation.git

**📄 License**

This project is licensed under the MIT License — free to use, modify, and contribute to.

# Contributing

I welcome open-source contributors to help improve and extend this tool!

To contribute:
1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Open a pull request describing your updates.

# Acknowledgments

Built with ❤️ by [Barbara Nyame](https://github.com/BarbaraNyame) and open-source contributors.

