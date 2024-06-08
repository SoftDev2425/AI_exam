import customtkinter
import tkinter as tk
import threading
import requests
from tkintermapview import TkinterMapView

# Replace 'YOUR_API_KEY' with your actual OpenCage API key
OPENCAGE_API_KEY = 'f3b9a12a21f64b66b9aa66c7a215adcb'

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window
app.title("AI Exam")
app.marker_list = []

def clear_marker_event():
    for marker in app.marker_list:
        marker.delete()

# Center the window on the screen
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 1200
window_height = 800
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

app.grid_columnconfigure(0, minsize=250)  # Set the minimum width of the first column
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

app.frame_left = customtkinter.CTkFrame(master=app, corner_radius=0, fg_color=None)
app.frame_left.grid(row=0, column=0, pady=0, padx=10, sticky='nsew')
app.frame_left.grid_rowconfigure(2, weight=1)

# LEFT SIDE
input_padx = 10
input_pady = 10
input_width = 300

label = customtkinter.CTkLabel(master=app.frame_left, text='Calculate price', font=('Roboto', 24))
label.pack(pady=12, padx=10)

# clear markers button
clear_markers_btn = customtkinter.CTkButton(master=app.frame_left,
                                            text="Clear Markers",
                                            command=clear_marker_event, fg_color="blue",
                                            width=input_width)
clear_markers_btn.pack(pady=input_pady, padx=input_padx)

entry_address = customtkinter.CTkEntry(master=app.frame_left, placeholder_text='Address',
                                       width=input_width)
entry_address.pack(pady=input_pady, padx=input_padx)

entry_zip_code = customtkinter.CTkOptionMenu(app.frame_left, values=[
    'Choose Zip', '2100 (København Ø)', '2620 (Albertslund)', '2740 (Skovlunde)', '2750 (Ballerup)',
    '2760 (Måløv)', '2950 (Vedbæk)', '2960 (Rungsted Kyst)', '2970 (Hørsholm)', '2980 (Kokkedal)',
    '2990 (Nivå)', '3000 (Helsingør)', '3050 (Humlebæk)', '3060 (Espergærde)', '3070 (Snekkersten)',
    '3080 (Tikøb)', '3100 (Hornbæk)', '3120 (Dronningmølle)', '3140 (Ålsgårde)', '3150 (Hellebæk)',
    '3200 (Helsinge)', '3210 (Vejby)', '3220 (Tisvildeleje)', '3230 (Græsted)', '3250 (Gilleleje)',
    '3320 (Skævinge)', '3480 (Fredensborg)', '3490 (Kvistgård)', '2300 (København S)', '2400 (København NV)',
    '2450 (København SV)', '2500 (Valby)', '2600 (Glostrup)', '2610 (Rødovre)', '2630 (Taastrup)',
    '2640 (Hedehusene)', '2650 (Hvidovre)', '2690 (Karlslunde)', '2700 (Brønshøj)', '2720 (Vanløse)',
    '2765 (Smørum)', '2770 (Kastrup)', '2791 (Dragør)', '2800 (Lyngby)', '2820 (Gentofte)', '2830 (Virum)',
    '2840 (Holte)', '2850 (Nærum)', '2860 (Søborg)', '2870 (Dyssegård)', '2880 (Bagsværd)', '2900 (Hellerup)',
    '2920 (Charlottenlund)', '2930 (Klampenborg)', '2942 (Skodsborg)', '3300 (Frederiksværk)',
    '3310 (Ølsted)', '3360 (Liseleje)', '3370 (Melby)', '3400 (Hillerød)', '3450 (Allerød)', '3460 (Birkerød)',
    '3540 (Lynge)', '3550 (Slangerup)', '3600 (Frederikssund)', '3650 (Ølstykke)', '3660 (Stenløse)',
],
width=input_width)
entry_zip_code.pack(pady=input_pady, padx=input_padx)

entry_size = customtkinter.CTkEntry(master=app.frame_left, placeholder_text='Size m^2', width=input_width)
entry_size.pack(pady=input_pady, padx=input_padx)

entry_type = customtkinter.CTkOptionMenu(app.frame_left, values=['Choose Type', 'Villa', 'Ejerlejlighed','Fritidshus', 'Rækkehus', 'Villalejlighed','Landejendom','Andelsbolig','Helårsgrund'], width=input_width)
entry_type.pack(pady=input_pady, padx=input_padx)

entry_energy_class = customtkinter.CTkOptionMenu(app.frame_left, values=['Choose Energy class', 'A2020', 'A2015', 'A2010', 'B', 'C', 'D', 'E', 'F', 'G'], width=input_width)
entry_energy_class.pack(pady=input_pady, padx=input_padx)

entry_rooms = customtkinter.CTkEntry(master=app.frame_left, placeholder_text='Room count', width=input_width)
entry_rooms.pack(pady=input_pady, padx=input_padx)

entry_constructed = customtkinter.CTkEntry(master=app.frame_left, placeholder_text='Year constructed', width=input_width)
entry_constructed.pack(pady=input_padx, padx=input_padx)

entry_burglary_risk = customtkinter.CTkOptionMenu(app.frame_left, values=[
    'Risiko for indbrud', 'meget lav', 'lav', 'mellem', 'høj', 'meget høj'
], width=input_width)
entry_burglary_risk.pack(pady=input_pady, padx=input_padx)

entry_pharmacy_distance = customtkinter.CTkEntry(master=app.frame_left, placeholder_text='Pharmacy distance', width=input_width)
entry_pharmacy_distance.pack(pady=input_pady, padx=input_padx)

entry_daycare_distance = customtkinter.CTkEntry(master=app.frame_left, placeholder_text='Daycare distance', width=input_width)
entry_daycare_distance.pack(pady=input_pady, padx=input_padx)

entry_grocery_distance = customtkinter.CTkEntry(master=app.frame_left, placeholder_text='Daycare grocery', width=input_width)
entry_grocery_distance.pack(pady=input_pady, padx=input_padx)

calculate_button = customtkinter.CTkButton(master=app.frame_left, text="Calculate", fg_color="blue", width=input_width, command=lambda: calculate())
calculate_button.pack(pady=12, padx=10)


help_window_width = 500
help_window_height = 200
# Help button
def show_help():
    help_text = (
        "1. Enter the address and select the zip code.\n"
        "2. Fill in the property details.\n"
        "3. Click 'Calculate' to get the coordinates and estimate price.\n"
        "4. Use 'Save Data' to save inputs and 'Load Data' to retrieve them.\n"
        "5. Generate a detailed report by clicking 'Generate Report'."
    )
    help_modal = customtkinter.CTkToplevel(app)
    help_modal.title("Help")
    help_modal.geometry(f"{help_window_width}x{help_window_height}")

    # Center the modal on the screen
    screen_width = help_modal.winfo_screenwidth()
    screen_height = help_modal.winfo_screenheight()
    x_position = (screen_width - help_window_width) // 2
    y_position = (screen_height - help_window_height) // 2
    help_modal.geometry(f"{help_window_width}x{help_window_height}+{x_position}+{y_position}")

    help_label = customtkinter.CTkLabel(master=help_modal, text=help_text, font=('Roboto', 14), anchor="w", justify="left")
    help_label.pack(pady=20, padx=20)

help_button = customtkinter.CTkButton(master=app.frame_left, text="Help", command=show_help)
help_button.pack(pady=12, padx=10)

# RIGHT SIDE
app.frame_right = customtkinter.CTkFrame(master=app, corner_radius=0)
app.frame_right.grid(row=0, column=1, rowspan=2, pady=0, padx=0, sticky='nsew')
app.frame_right.grid_rowconfigure(2, weight=1)

label = customtkinter.CTkLabel(master=app.frame_right, text='Map', font=('Roboto', 24))
label.pack(pady=12, padx=10)

map_widget = TkinterMapView(master=app.frame_right, corner_radius=0)
map_widget.set_address("colosseo, rome, italy")
map_widget.pack(fill='both', expand=True)

# Text box and button grid
app.text_box_frame = customtkinter.CTkFrame(master=app.frame_right, corner_radius=0)
app.text_box_frame.pack(fill='x')
app.text_box_frame.grid_rowconfigure(0, weight=1)
app.text_box_frame.grid_columnconfigure(0, weight=1)
app.text_box_frame.grid_columnconfigure(1, weight=0)

app.text_box = customtkinter.CTkTextbox(master=app.text_box_frame, height=10, font=('Roboto', 14))
app.text_box.insert(tk.END, "Please fill out the form and press calculate")
app.text_box.configure(state='disabled')
app.text_box.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

generate_report_btn = customtkinter.CTkButton(master=app.text_box_frame,
                                              text="Generate Report",
                                              fg_color="blue")
generate_report_btn.grid(row=0, column=1, padx=10, pady=10, sticky='e')

def update_text_box(text, error=False):
    app.text_box.configure(state='normal')
    app.text_box.delete(1.0, tk.END)
    if error:
        app.text_box.insert(tk.END, f"Error: {text}")
        app.text_box.configure(fg_color="red")
    else:
        app.text_box.insert(tk.END, text)
        app.text_box.configure(fg_color="white")
    app.text_box.configure(state='disabled')

def get_coordinates(address, postnr, callback):
    def geocode():
        try:
            url = f'https://api.opencagedata.com/geocode/v1/json?q={address}%20{postnr}%20Danmark&key={OPENCAGE_API_KEY}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data['results']:
                location = data['results'][0]['geometry']
                callback(location['lat'], location['lng'])
            else:
                callback(None, None)
        except requests.RequestException as e:
            callback(None, None)
            update_text_box(f"Error: {e}", error=True)
    threading.Thread(target=geocode).start()

def search_event(address, zip_code, x, y):
    map_widget.set_address(f'{address}, {zip_code}')
    app.marker_list.append(map_widget.set_marker(x, y))

def process_data(x, y, address, zip_code):
    if x is None or y is None:
        update_text_box("Could not find the address. Please try again.", error=True)
    else:
        search_event(address, zip_code, x, y)
        update_text_box(f"Coordinates for the address '{address}' are ({x}, {y})")

def validate_inputs():
    address = entry_address.get()
    zip_code = entry_zip_code.get()
    size = entry_size.get()
    type = entry_type.get()
    energy_class = entry_energy_class.get()

    if not address:
        update_text_box("Please enter a valid address.", error=True)
        return False
    if zip_code == "Choose Zip":
        update_text_box("Please choose a zip code.", error=True)
        return False
    if not size.isdigit() or int(size) <= 0:
        update_text_box("Please enter a valid size in m^2.", error=True)
        return False
    if type == "Choose Type":
        update_text_box("Please choose a property type.", error=True)
        return False
    if energy_class == "Choose Energy class":
        update_text_box("Please choose an energy class.", error=True)
        return False
    return True

def calculate():
    if not validate_inputs():
        return
    address = entry_address.get()
    zip_code = entry_zip_code.get()

    get_coordinates(address, zip_code, lambda x, y: app.after(100, process_data, x, y, address, zip_code))

def change_map(new_map):
    #if new_map == "OpenStreetMap":
     #   map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
    if new_map == "Google normal":
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    elif new_map == "Google satellite":
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

app.map_option_menu = customtkinter.CTkOptionMenu(app.frame_left, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                       command=change_map)
app.map_option_menu.pack(pady=12, padx=10)

app.appearance_mode_label = customtkinter.CTkLabel(app.frame_left, text="Appearance Mode:", anchor="w")
app.appearance_mode_label.pack(pady=12, padx=10)
app.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(app.frame_left, values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode)
app.appearance_mode_optionmenu.pack(pady=12, padx=10)

map_widget.set_zoom(7)
app.appearance_mode_optionmenu.set('Dark')

app.mainloop()
