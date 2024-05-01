import pandas as pd
import matplotlib.pyplot as plt
import json
from matplotlib.patches import Patch


# Load the data from the JSON file
file_path = 'treatment_data.json'  # Replace with your actual file path
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert JSON data into a DataFrame
df = pd.DataFrame([{
    'Treatment Name': item['message']['event']['medicine']['name'],
    'Dose (MLT)': item['message']['event']['dose']['doseQuantity'],
    'Date': item['eventDateTime'],  # Assuming each item has an 'eventDateTime'
} for item in data])

# Convert 'Date' to datetime format and extract just the date part
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Aggregate data for visualizations
treatment_summary = df['Treatment Name'].value_counts()
treatments_over_time_summary = df.groupby(['Date', 'Treatment Name']).size().unstack(fill_value=0)
dose_stats = df.groupby('Treatment Name')['Dose (MLT)'].agg(['mean', 'min', 'max'])
total_treatments_over_time_summary = df['Date'].value_counts().sort_index()

# Assign colors to each treatment name
unique_treatments = df['Treatment Name'].unique()
color_map = plt.get_cmap('tab10', len(unique_treatments))
treatment_colors = {treatment: color_map(i) for i, treatment in enumerate(unique_treatments)}

# Plotting
plt.figure(figsize=(15, 7))
plt.suptitle('AgriVet Treatment Grapher', fontsize=20, fontweight='bold', color='navy', position=(0.5, 0.98))


# Treatment Names Summary
plt.subplot(1, 4, 1)
bars = treatment_summary.plot(kind='bar', color=[treatment_colors[treatment] for treatment in treatment_summary.index], width=0.5)  # Adjust the width
plt.title('Treatment accross a dataset')
plt.ylabel('Number of animals')
plt.xticks(rotation=45)
for bar in bars.patches:
    bars.annotate(format(bar.get_height(), '.0f'),
                   (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                   ha='center', va='center', size=10, xytext=(0, 8), textcoords='offset points')
plt.gca().set_xticklabels(treatment_summary.index, rotation=45, ha='right')

# Treatments Over Time Summary
plt.subplot(1, 4, 2)
ax = treatments_over_time_summary.plot(kind='bar', stacked=True, ax=plt.gca(), color=[treatment_colors[treatment] for treatment in treatments_over_time_summary.columns], width=0.5)  # Adjust the width
plt.title('Daily treatment distribution')
plt.ylabel('Number of animals')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.gca().set_xticklabels(treatments_over_time_summary.index, rotation=45, ha='right')


# Add annotations for treatment counts inside the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if height > 0:  # To avoid placing annotations on empty bars
        ax.annotate(f'{int(height)}', (x + width / 2, y + height / 2), ha='center', va='center', color='white')

# Adjust y-axis limits to make the scale larger
ax.set_ylim(0, ax.get_ylim()[1]*1.2)  # Increase the upper limit of y-axis by 20%

# Generate and add the legend for the bar chart, positioned inside on the top left
legend_patches = [Patch(color=color, label=label) for label, color in zip(treatments_over_time_summary.columns, [treatment_colors[treatment] for treatment in treatments_over_time_summary.columns])]
ax.legend(handles=legend_patches, loc='upper left', ncol=1)



# Treatments Over Time Summary as Pie Chart
plt.subplot(1, 4, 3)
# Note: Removed labels from the pie chart slices by not specifying the 'labels' parameter
pie = treatments_over_time_summary.sum().plot(kind='pie', autopct='%1.1f%%', colors=[treatment_colors[treatment] for treatment in treatments_over_time_summary.columns],  labels=['']*len(treatments_over_time_summary.columns))
plt.title('Treatments proportions')
plt.ylabel('')
# Generate and add the legend for the pie chart, positioned to not overlap with the chart
legend_patches = [Patch(color=color, label=label) for label, color in zip(treatments_over_time_summary.columns, [treatment_colors[treatment] for treatment in treatments_over_time_summary.columns])]
plt.legend(handles=legend_patches, bbox_to_anchor=(0.5, -0.1), loc='upper center', ncol=2)


# Dose Quantity Statistics with enhancements
plt.subplot(1, 4, 4)
# Plot average dose
average_bars = dose_stats['mean'].plot(kind='bar', label='Average Dose', yerr=[dose_stats['mean'] - dose_stats['min'], dose_stats['max'] - dose_stats['mean']], error_kw=dict(capsize=5, capthick=2, ecolor='darkred'), color=[treatment_colors[treatment] for treatment in dose_stats.index], width=0.5)  # Adjust the width
plt.title('Average dose by treatment')
plt.xlabel('Treatment Name')
plt.ylabel('Dose (ml)')
plt.xticks(rotation=45)

# Add x-axis labels under the bars
plt.gca().set_xticklabels(dose_stats.index, rotation=45, ha='right')



# Annotate the average dose on each bar
for i, mean_value in enumerate(dose_stats['mean']):
    plt.text(i, mean_value, f'{mean_value:.0f}', ha='center', va='bottom')


# # Treatments Over Time Summary
# plt.subplot(1, 4, 4)
# pie = total_treatments_over_time_summary.plot(kind='pie', autopct='%1.1f%%', startangle=140)
# plt.title('Treatments Over Time')
# plt.ylabel('')


plt.tight_layout()
plt.show()
