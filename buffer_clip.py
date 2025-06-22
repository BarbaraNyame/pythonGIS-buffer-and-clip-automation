import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Confirm working directory
print("Current working directory:", os.getcwd())

# Load shapefiles
submetro = gpd.read_file("/Users/mac/Desktop/pythonGIS buffer and clip automation/Kumasi_SubMetros.shp")
stations = gpd.read_file("/Users/mac/Desktop/pythonGIS buffer and clip automation/police_stations.shp")

# Ensure both layers use the same CRS
stations = stations.to_crs(submetro.crs)

# Check and reproject to a projected CRS if needed
if submetro.crs.is_geographic:
    print("Reprojecting to EPSG:32630 (UTM Zone 30N)...")
    submetro = submetro.to_crs(epsg=32630)
    stations = stations.to_crs(epsg=32630)

# Create 500m buffer
stations['buffer'] = stations.geometry.buffer(500)

# Set active geometry to 'buffer'
buffered_gdf = stations.set_geometry('buffer')

# Clip the buffered areas to the Kumasi Sub-Metro
clipped_buffers = gpd.clip(buffered_gdf, submetro)

# Set the active geometry to 'buffer' again (just in case)
clipped_buffers = clipped_buffers.set_geometry('buffer')

# Drop any other geometry columns if present (like 'geometry' points)
if 'geometry' in clipped_buffers.columns:
    clipped_buffers = clipped_buffers.drop(columns=['geometry'])

# Save the clipped buffers as a shapefile
clipped_buffers.to_file("/Users/mac/Desktop/pythonGIS buffer and clip automation/buffered_clipped_stations.shp")

# Plot everything
fig, ax = plt.subplots(figsize=(10, 10))
submetro.plot(ax=ax, color='white', edgecolor='black')
clipped_buffers.plot(ax=ax, color='skyblue', alpha=0.5)
stations.set_geometry('geometry').plot(ax=ax, color='red')
plt.title("Buffered Police Stations Clipped to Kumasi Sub-Metro")

# Save the figure as a PNG image
plt.savefig("/Users/mac/Desktop/pythonGIS buffer and clip automation/buffered_map.png", dpi=300)

# Display the plot
plt.show()