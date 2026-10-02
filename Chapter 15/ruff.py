from pathlib import Path
import json

list =  ['size', 'width', 'color', 'tickdir', 'pad', 'labelsize', 'labelcolor', 'labelfontfamily', 'zorder', 'gridOn', 'tick1On', 'tick2On', 'label1On', 'label2On', 'length', 'direction', 'left', 'bottom', 'right', 'top', 'labelleft', 'labelbottom', 'labelright', 'labeltop', 'labelrotation', 'labelrotation_mode', 'grid_agg_filter', 'grid_alpha', 'grid_animated', 'grid_antialiased', 'grid_clip_box', 'grid_clip_on', 'grid_clip_path', 'grid_color', 'grid_dash_capstyle', 'grid_dash_joinstyle', 'grid_dashes', 'grid_data', 'grid_drawstyle', 'grid_figure', 'grid_fillstyle', 'grid_gapcolor', 'grid_gid', 'grid_in_layout', 'grid_label', 'grid_linestyle', 'grid_linewidth', 'grid_marker', 'grid_markeredgecolor', 'grid_markeredgewidth', 'grid_markerfacecolor', 'grid_markerfacecoloralt', 'grid_markersize', 'grid_markevery', 'grid_mouseover', 'grid_path_effects', 'grid_picker', 'grid_pickradius', 'grid_rasterized', 'grid_sketch_params', 'grid_snap', 'grid_solid_capstyle', 'grid_solid_joinstyle', 'grid_transform', 'grid_url', 'grid_visible', 'grid_xdata', 'grid_ydata', 'grid_zorder', 'grid_aa', 'grid_c', 'grid_ds', 'grid_ls', 'grid_lw', 'grid_mec', 'grid_mew', 'grid_mfc', 'grid_mfcalt', 'grid_ms']

# if "labelsize" in list:
#     print("Present")
# else:
#     print("Not present")

# styles = ['Solarize_Light2', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'petroff6', 'petroff8', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10',]
# prompt_style = input("Enter name: ")
# while True:
#     for style in styles:
#         new = style
#         prompt_style += f"\n{new}"
        
#     break
# path = Path("Styles.txt")
# path.write_text(prompt_style)
    



import matplotlib.pyplot as plt

original_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
rendom_numbers = [1,10,30,4,67,34,21,67,94,34,65,87,34,26,1]

fig, ax = plt.subplots()

ax.scatter(original_value, square, s=50, c='g')
ax.plot(original_value, square, linewidth=2, color='b')
# ax.plot(rendom_numbers, color='r')

ax.set_title("Square Number", fontsize=20)
ax.set_xlabel("Numbers", fontsize=12)
ax.set_ylabel("Square of numbers",fontsize=12)

ax.tick_params(labelsize=10)

plt.show()