wl = round(float(input("Enter the wavelength: ")),1)
struct = "Outside the visible range."
if (wl >= 380):
  struct = f"{wl} nm is Violet."
if (wl >= 450):
  struct = f"{wl} nm is Blue."
if (wl >= 495):
  struct = f"{wl} nm is Green."
if (wl >= 570):
  struct = f"{wl} nm is Yellow."
if (wl >= 590):
  struct = f"{wl} nm is Orange."
if (wl >= 620):
  struct = f"{wl} nm is Red"
if (wl >= 750):
  struct = "Outside the visible range."
print(struct)
