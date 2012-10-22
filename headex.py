import tkinter
import tkinter.messagebox

def storeData():
	try:
		dFile = open("deliveries.txt", "a")
		dFile.write("Depot:\n%s\n" % depot.get())
		dFile.write("Description:\n%s\n" % description.get())
		dFile.write("Address:\n%s\n" % address.get("1.0", 'end'))
		dFile.close()
		description.delete(0, 'end')
		address.delete("1.0", 'end')
	except Exception as ex:
		tkinter.messagebox.showerror("Error!", "Can't write to file\n%s" % ex)
def readDepots(file):
	depFile = open(file)
	depots = []
	for depot in depFile:
		depots.append(depot.rstrip())
	return depots


window = tkinter.Tk()
window.title('Head-Ex Deliveries')


tkinter.Label(window, text = "Depot:").pack()
depot = tkinter.StringVar()
depot.set(None)
depots = readDepots("depots.txt")
tkinter.OptionMenu(window, depot, *depots).pack()

tkinter.Label(window, text = "Description:").pack()
description = tkinter.Entry(window)
description.pack()

tkinter.Label(window, text = "Address:").pack()
address = tkinter.Text(window)
address.pack()

saveB = tkinter.Button(window, text = "Save", command = storeData)
saveB.pack()
window.mainloop()