import matplotlib.pyplot as plt
import numpy as np

np.random.seed(88)



total_star_nodes = 1000



radii = np.random.exponential(scale=2.0, size=total_star_nodes)
angles = 2.5 * radii + np.random.normal(0, 0.4, size=total_star_nodes)



x_coordinates = radii * np.cos(angles)
y_coordinates = radii * np.sin(angles)

core_thermal_energy = 100 / (radii + 0.5) + np.random.randint(0, 30, size=total_star_nodes)


stellar_mass_sizes = (np.random.random(size=total_star_nodes) * 18)**2 + 5


plt.figure(figsize=(14, 9), facecolor='#06060C')
ax = plt.gca()
ax.set_facecolor("#06060C")



scatter_engine = plt.scatter(
    x_coordinates, 
    y_coordinates, 
    c=core_thermal_energy,     # Color mapped dynamically to local system energy
    s=stellar_mass_sizes,      # Variable dot sizes based on structural mass calculations
    alpha=0.65,                # Alpha overlay allows clean transparency blending at dense clusters
    cmap='magma',              # Premium deep black-purple-orange-white cosmic spectrum
    edgecolors='none'          # Erase dot borders so dense clusters merge smoothly
)

color_bar = plt.colorbar(scatter_engine, pad=0.03)
color_bar.set_label('Thermal Radiation Energy Index ($\Psi$)', color='#A1A1AA', fontsize=12, labelpad=15)
color_bar.ax.yaxis.set_tick_params(colors='#52525B')

plt.title("HIGH-THROUGHPUT STELLAR SPECTRAL ANALYSIS", fontsize=16, fontweight='bold', color='#FAFAFA', pad=25)
plt.xlabel("Galactic X-Axis Plane (Lightyears)", color='#A1A1AA', fontsize=11, labelpad=10)
plt.ylabel("Galactic Y-Axis Plane (Lightyears)", color='#A1A1AA', fontsize=11, labelpad=10)



plt.grid(color='#1E1E2F', linestyle='--', linewidth=0.7, alpha=0.5)


ax.tick_params(colors='#52525B', labelsize=10)
for spine in ax.spines.values():
    spine.set_color('#1E1E2F')

# Lock down layout boundaries
plt.tight_layout()
plt.show()