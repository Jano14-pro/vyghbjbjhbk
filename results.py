import customtkinter as a

win = a.CTk()
win.title("Agape Academy International(AAI)")
win.geometry("1290x760")
win.resizable(0,0)

dash_frame = a.CTkFrame(win, height = 55, width=1290, fg_color= "#820025", corner_radius=0)
dash_frame.place(relx = 0, rely = 0)

mark_frame= a.CTkFrame(win, width = 400, height= 65, fg_color="#f5f5f5" )
mark_frame.place(relx = 0.43, rely = 0.18)

mark_lbl = a.CTkLabel(mark_frame, text = "Total Mark", text_color="black", font = ("Monserrat", 30, "bold"))
mark_lbl.place(relx = 0.1, rely = 0.3)

mark_entry = a.CTkEntry(mark_frame, width = 150, height = 40)
mark_entry.place(relx = 0.55, rely = 0.23)

record_frame = a.CTkFrame(win,  width= 750,  height=80, fg_color= "#f5f5f5")
record_frame.place(relx = 0.28, rely = 0.3)

record_lbl1 = a.CTkLabel(record_frame, text="Student ID", font=("Monserrat", 25, "bold"), text_color="black")
record_lbl1.place(relx = 0.1, rely = 0.3)

record_lbl1_entry = a.CTkEntry(record_frame, width = 100, height=40)
record_lbl1_entry.place(relx = 0.28, rely = 0.25)

record_lbl2 = a.CTkLabel(record_frame, text="Mark", font=("Monserrat", 25, "bold"), text_color="black" )
record_lbl2.place(relx = 0.5, rely = 0.3)

record_lbl2_entry = a.CTkEntry(record_frame, width = 100, height=40)
record_lbl2_entry.place(relx = 0.6, rely = 0.25)

record_btn = a.CTkButton(record_frame, text = "Record", font= ("Monserrat", 20, "bold"), width = 100, height = 35 )
record_btn.place(relx = 0.8, rely = 0.3)

chart_frame = a.CTkFrame(win, width= 750, height=300, fg_color="#f5f5f5")
chart_frame.place(relx = 0.28, rely = 0.43)

dash_pic = a.CTkFrame(dash_frame, width=40, height= 40, fg_color="white", corner_radius= 600)
dash_pic.place(relx = 0.96, rely = 0.15)

btm_frame = a.CTkFrame(win, height = 55, width=1290, fg_color= "#820025",corner_radius=0)
btm_frame.place(relx = 0, rely = 0.836)

dash_title = a.CTkLabel(win, text = "Agape Management System", text_color = "white", font = ("Monserrat", 20), fg_color= "#820025", corner_radius=0)
dash_title.place(relx = .05, rely = 0.020)

dash_title2 = a.CTkLabel(win, text = "December 25, 2025", text_color = "white", font = ("Monserrat", 15), fg_color= "#820025", corner_radius=0)
dash_title2.place(relx = .5, rely = 0.020)

side_frame = a.CTkFrame(win, height = 581, width = 200, fg_color= "#0e716b", corner_radius = 0)
side_frame.place(relx = 0, rely = 0.0716)

ms_frame1 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame1.place(relx = 0.136, rely = 0.1)

msf1_label = a.CTkLabel(ms_frame1, text = "DASHBOARD", font = ("Monserrat", 12, "bold"))
msf1_label.place(relx= 0.21, rely = 0.01)

ms_frame2 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame2.place(relx = 0.136, rely = 0.2)

msf2_label = a.CTkLabel(ms_frame2, text = "REGISTRATION", font = ("Monserrat", 12, "bold"))
msf2_label.place(relx= 0.16, rely = 0.01)

ms_frame3 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame3.place(relx = 0.136, rely = 0.3)

msf3_label = a.CTkLabel(ms_frame3, text = "DATA HOUSE", font = ("Monserrat", 12, "bold"))
msf3_label.place(relx= 0.2, rely = 0.01)

ms_frame4 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame4.place(relx = 0.136, rely = 0.4)

msf4_label = a.CTkLabel(ms_frame4, text = "ACADEMICS", font = ("Monserrat", 12, "bold"))
msf4_label.place(relx= 0.23, rely = 0.01)

ms_frame5 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame5.place(relx = 0.136, rely = 0.5)

msf5_label = a.CTkLabel(ms_frame5, text = "PROPERTIES", font = ("Monserrat", 12, "bold"))
msf5_label.place(relx= 0.22, rely = 0.01)

ms_frame6 = a.CTkFrame(side_frame, width= 140, height = 20, corner_radius = 4)
ms_frame6.place(relx = 0.136, rely = 0.6)

msf6_label = a.CTkLabel(ms_frame6, text = "SETTING", font = ("Monserrat", 12, "bold"))
msf6_label.place(relx= 0.28, rely = 0.01)

dash_frame2 = a.CTkFrame(win, width =1090, height= 55, corner_radius = 0, fg_color = "#014342")
dash_frame2.place(relx = 0.155, rely = 0.072)



win.mainloop()