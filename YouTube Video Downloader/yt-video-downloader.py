# importing the packages
import tkinter
import pytube

# displaying the window
window = tkinter.Tk()
window.geometry('600x300')
window.resizable(0, 0)
window.title("Youtube Video Downloader")
window.config(bg="cyan")

tkinter.Label(window, text="Youtube Video Downloader", font="Helvetica 20 bold", bg='black', fg='white').pack()

# creating placeholder for the link
link_type =tkinter.StringVar()
tkinter.Label(window, text="Paste Link here: ", font="ariel 19", bg='grey').place(x=190, y=60)

videolink = tkinter.Entry(window,bd=5, width=80, textvariable=link_type).place(x=60, y=110)

path = "C:/Users/User/PycharmProjects/hobby_projects/yt video downloader"


# main function to do the download
def downloadvideo():
    videourl = pytube.YouTube(str(link_type.get()))
    ytvideo = videourl.streams.filter(res="480p").first()
    ytvideo.download(path)
    message = tkinter.Label(window, text="Video Downloaded Successfully!", font="Times 16",bg="brown",fg="white")
    message.place(x=160, y=210)

def clearfield():    #this function sets all variable to an empty string
    link_type.set("")

# creating the download button
downloadbutton = tkinter.Button(window, text="Download", font="airel 10 bold", command=downloadvideo, bg="#0052cc", padx=10, pady=10)
downloadbutton.place(x=200,y=150)

clearbutton = tkinter.Button(window, font="airel 10 bold", text="Clear", command=clearfield, bg="#0052cc", padx=10, pady=10)
clearbutton.place(x=300,y=150)

#to execute the program
window.mainloop()
