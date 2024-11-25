#importing the required module
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#main class. ellam mae starts from here
class BankingSystem():
    def __init__(self,master):
        self.master=master  #everything starts with an instance

        self.master.title("BANKING MANAGEMENT SYSTEM")    
        self.master.geometry("400x400")

        self.users={}      #used to store all the users details within that instance 
        
        #MAIN FRAME TOP PORTION
        self.main_frame=Frame(self.master, bg='#F0F0F0')
        self.main_frame.pack(pady=10)
        self.name_label=Label(self.main_frame,text="Name:",bg='#F0F0F0',font=("Arial", 14))
        self.name_label.grid(row=0,column=0,padx=10,pady=10)
        self.name_entry=Entry(self.main_frame,relief='solid', borderwidth=1,font=("Arial", 14))
        self.name_entry.grid(row=0,column=1,padx=10,pady=10)
        self.age_label=Label(self.main_frame,text="Age:",bg='#F0F0F0',font=("Arial", 14))
        self.age_label.grid(row=1,column=0,padx=10,pady=10)
        self.age_entry=Entry(self.main_frame,relief='solid', borderwidth=1,font=("Arial", 14))
        self.age_entry.grid(row=1,column=1,padx=10,pady=10)
        self.salary_label=Label(self.main_frame,text="Salary:",bg='#F0F0F0',font=("Arial", 14))
        self.salary_label.grid(row=2,column=0,padx=10,pady=10)
        self.salary_entry=Entry(self.main_frame,relief='solid', borderwidth=1,font=("Arial", 14))
        self.salary_entry.grid(row=2,column=1,padx=10,pady=10)
        self.pin_label=Label(self.main_frame,text="Pin:",bg='#F0F0F0',font=("Arial", 14))
        self.pin_label.grid(row=3,column=0,padx=10,pady=10)
        self.pin_entry=Entry(self.main_frame,show="*",relief='solid', borderwidth=1,font=("Arial", 14))
        self.pin_entry.grid(row=3,column=1,padx=10,pady=10)
        self.create_account_button=Button(self.main_frame,text="Create Account",font=("Arial", 14),bg="#4CAF50",fg="#FFFFFF",relief="raised",activebackground="#2E8B57",activeforeground="#FFFFFF",command=self.create_account) 
        self.create_account_button.grid(row=4,column=1,padx=10,pady=10)
        self.master.bind("<Return>",self.create_account)
        
        #MAIN FRAME BOTTOM PORTION
        self.login_frame=Frame(self.master,bg='#F0F0F0')
        self.login_frame.pack(pady=20)
        self.login_name_label=Label(self.login_frame,text="Name:",bg='#F0F0F0',font=("Arial", 14))
        self.login_name_label.grid(row=0,column=0,padx=10,pady=10)
        self.login_name_entry=Entry(self.login_frame,relief='solid', borderwidth=1)
        self.login_name_entry.grid(row=0,column=1,padx=10,pady=10)
        self.login_pin_label=Label(self.login_frame,text="Pin:",bg='#F0F0F0',font=("Arial", 14))
        self.login_pin_label.grid(row=1,column=0,padx=10,pady=10)
        self.login_pin_entry=Entry(self.login_frame,show="*",relief='solid', borderwidth=1,font=("Arial", 14))
        self.login_pin_entry.grid(row=1,column=1,padx=10,pady=10)
        self.login_button=Button(self.login_frame,text="Login Account",bg="orange",fg="#FFFFFF",font=("Arial", 14),relief="raised",activebackground="#2E8B57",activeforeground="#FFFFFF",command=self.login)#command=self.login
        self.login_button.grid(row=2,column=1,padx=10,pady=10)
        self.master.bind("<Return>",self.login)
         
        #LOGIN KU APPARAM VARA FRAME (USER_FRAME)
        self.user_detail_frame=Frame(self.master)
        self.user_name_label2=Label(self.user_detail_frame,text="Name:",bg='#F0F0F0',font=("Arial", 14))
        self.user_name_label2.grid(row=0,column=1,padx=10,pady=10)
        self.user_age_label2=Label(self.user_detail_frame,text="Age:",bg='#F0F0F0',font=("Arial", 14))
        self.user_age_label2.grid(row=1,column=1,padx=10,pady=10)
        self.user_salary_label2=Label(self.user_detail_frame,text="Salary:",bg='#F0F0F0',font=("Arial", 14))
        self.user_salary_label2.grid(row=2,column=1,padx=10,pady=10)
        self.user_current_balance_label2=Label(self.user_detail_frame,text="Current Balance:",bg='#F0F0F0',font=("Arial", 14))
        self.user_current_balance_label2.grid(row=3,column=1,padx=10,pady=10)

        #LOGIN KU APPARAM VARA FRAME LA IRUKURA BUTTONS (USER_FRAME)
        self.transaction_button=Button(self.user_detail_frame, text="Transaction Log",font=("Arial", 14),bg="grey",fg="#FFFFFF",relief="raised",activebackground="#2E8B57",activeforeground="#FFFFFF",command=self.transaction_log) #command=self.transaction
        self.transaction_button.grid(row=5,column=0,padx=10,pady=10)
        self.deposit_button=Button(self.user_detail_frame, text="Deposit",bg="pink",font=("Arial", 14),fg="#FFFFFF",relief="raised",activebackground="#2E8B57",activeforeground="#FFFFFF",command=self.deposit) #command=self.deposit
        self.deposit_button.grid(row=5,column=1,padx=10,pady=10)
        self.withdraw_button=Button(self.user_detail_frame, text="Withdraw",font=("Arial", 14),bg="violet",fg="#FFFFFF",relief="raised",activebackground="#2E8B57",activeforeground="#FFFFFF",command=self.withdraw) #command=self.withdraw
        self.withdraw_button.grid(row=5,column=2,padx=10,pady=10)
        self.logout_button=Button(self.user_detail_frame, text="Logout",font=("Arial", 14),bg="black",fg="#FFFFFF",relief="raised",activebackground="#2E8B57",activeforeground="#FFFFFF",command=self.logout)
        self.logout_button.grid(row=5,column=3,padx=10,pady=10)

        #asigning the null values just for understanding nothing else"
        self.name=""
        self.age=""
        self.salary=""
        self.pin=""
        self.current_balance=0
        self.transaction_log=[]
        users_data={}

    def create_account(self):
        #getting values from the entry widget(through user)
        name=self.name_entry.get()
        age=self.age_entry.get()
        pin=self.pin_entry.get()
        salary=self.salary_entry.get()
        #print(f"Name: '{name}', Age: '{age}', Pin: '{pin}', Salary: '{salary}'")
        #checking for errors
        if not name or not age or not pin or not salary:
            messagebox.showerror("Error Message", "Enter all the details!")
            return
        if not age.isdigit():
            messagebox.showerror("Error Message", "enter a valid age!")
            return
        if not pin.isdigit() or len(pin)!=4 :
            messagebox.showerror("Error Message", "enter a valid pin!")
            return
        if not salary.isdigit():
            messagebox.showerror("Error Message","Enter a Valid salary!")
            return
            
        #assigning the value to dictionary
        users_data={"name":name,"age":age,"pin":pin,"salary":salary,"balance":0}  
        self.users[pin]=users_data

        #assigning values to the intance variable for using in other functions
        self.name=name
        self.age=age
        self.pin=pin
        self.salary=salary

        #deleting the text typed by the user input
        self.name_entry.delete(0,END)
        self.age_entry.delete(0,END)
        self.salary_entry.delete(0,END)
        self.pin_entry.delete(0,END)

        #after account created, users details frame la show panna we are updating
        self.user_name_label2.config(text="Name:"+self.name)
        self.user_age_label2.config(text="Age:"+self.age)
        self.user_salary_label2.config(text="Salary:"+self.salary)
        self.user_current_balance_label2.config(text="Current Balance:"+str(self.current_balance))

         #changing the frame from main_frame to user_details frame   
        self.main_frame.pack_forget()
        self.login_frame.pack_forget()
        self.user_detail_frame.pack(padx=10,pady=10)

    def login(self):
        #login frame ku functionalities
        login_pin=self.login_pin_entry.get()
        login_name=self.login_name_entry.get()
        #print(f'login_pin:{login_pin}')
        #print(f'Name:{login_name}')

        #checking for valid users
        if login_pin in self.users:
            if self.users[login_pin]["name"]==login_name:
                self.details_transfer=self.users[login_pin]

                #setting the revlavent data to the screen 
                self.user_name_label2['text']=f'Name: {self.details_transfer["name"]}'
                self.user_age_label2['text']=f'Age: {self.details_transfer["age"]}'
                self.user_salary_label2['text']=f'Salary: {self.details_transfer["salary"]}'
                self.user_current_balance_label2['text']=f'Current_Balance: {self.details_transfer["balance"]}'
                #changing the frame
                self.user_detail_frame.pack(pady=10)
                self.main_frame.pack_forget()
                self.login_frame.pack_forget()
            else:
                messagebox.showerror("Error","User Name is Invalid")
                return
        else:
            messagebox.showerror("Error","User Pin is Invalid")
            return
        
    def deposit(self):
        #getting inputs for the users
        login_pin_for_deposit=simpledialog.askstring("Deposit","Enter the pin:")
        print(f'PIN:{login_pin_for_deposit}')
        #checking for validation
        if not login_pin_for_deposit:
            messagebox.showerror("Error","Enter a pin")
            return
        elif not login_pin_for_deposit in self.users:
            messagebox.showerror("Error","Invalid Pin")
            return
        elif not login_pin_for_deposit.isdigit():
            messagebox.showerror("Error","Please enter a valid pin")
            return
        else:
            deposit_amount=simpledialog.askstring("Deposit","Enter the amount:")
            print(f'amount:{deposit_amount}')
        
        if  not deposit_amount:
            messagebox.showerror("Error","Please enter the amount to deposit")
            return
        elif int(deposit_amount) <=0:
            messagebox.showerror("Error","Please enter a valid amount")
            return
        else: #updating the values in the user_details frame
            self.users[login_pin_for_deposit]["balance"]+=int(deposit_amount)
            self.user_current_balance_label2['text']=f'Current Balance: {str(self.users[login_pin_for_deposit]["balance"])}'
            transaction="Deposit: "+deposit_amount+" Balance: "+str(self.users[login_pin_for_deposit]["balance"]) #adding transaction log
            self.transaction_log.append(transaction)
            self.users[login_pin_for_deposit]["transactions"]=self.transaction_log
            print(self.users[login_pin_for_deposit]["transactions"])

    def withdraw(self):
        #getting inputs for the users
        login_pin_for_withdraw=simpledialog.askstring("Withdraw","Enter the pin:")
        print(f'PIN:{login_pin_for_withdraw}')
        #checking for validation
        if not login_pin_for_withdraw:
            messagebox.showerror("Error","Enter a pin")
            return
        elif not login_pin_for_withdraw in self.users:
            messagebox.showerror("Error","Invalid Pin")
            return
        elif not login_pin_for_withdraw.isdigit():
            messagebox.showerror("Error","Please enter a valid pin")
            return
        else:
            withdraw_amount=simpledialog.askstring("Withdraw","Enter the amount:")
            print(f'amount:{withdraw_amount}')
        
        if  not withdraw_amount:
            messagebox.showerror("Error","Please enter the amount to withdraw")
            return
        elif int(withdraw_amount) <=0:
            messagebox.showerror("Error","Please enter a valid amount")
            return
        else: #updating the values in the user_details frame
            self.users[login_pin_for_withdraw]["balance"]-=int(withdraw_amount)
            self.user_current_balance_label2['text']=f'Current Balance: {str(self.users[login_pin_for_withdraw]["balance"])}'
            transaction="Withdraw: "+withdraw_amount+" Balance: "+str(self.users[login_pin_for_withdraw]["balance"]) #adding transaction log
            self.transaction_log.append(transaction)
            self.users[login_pin_for_withdraw]["transactions"]=self.transaction_log
            print(self.users[login_pin_for_withdraw]["transactions"])

        
    def transaction_log(self):
        pin=self.login_pin_entry.get()
        transaction_log_window=Toplevel(self.master)
        transaction_log_window.title("Transaction Log")
        transaction_frame=Frame(transaction_log_window)
        transaction_frame.pack(padx=10,pady=10)
        transaction_frame_label=Label(transaction_frame,text="Transaction Log")
        transaction_frame_label.grid(row=0,column=0,padx=10,pady=10)

        transaction_listbox=Listbox(transaction_frame,width=50)
        transaction_listbox.grid(row=1,column=0,padx=10,pady=10)
        if pin in self.users:
            self.users[pin]["transactions"].extend(self.transaction_log)

        for transaction in self.users[pin]["transactions"]:
            transaction_listbox.insert(END, transaction)

        

    def logout(self):
        self.name=""
        self.age=""
        self.pin=""
        self.salary=""
        self.transaction_log=[]
        self.current_balance=0
        self.user_detail_frame.pack_forget()
        self.main_frame.pack(pady=10)
        self.login_frame.pack(pady=10)



def main():
    root=Tk()
    #root.mainloop()
    bank_system=BankingSystem(root)
    root.mainloop()


if __name__=='__main__':
    main()


