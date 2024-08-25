# this is a simple university project
# not complete

file=open('Info.txt','w')
file.close()
print('Welcome!')
print('(Remember your username and userpass.)')

def fullname(name,family):
  return name+'_'+family


def filee(Admin,ContactInfo):
  file=open('Info.txt','w')
  yechizimasalan=str(ContactInfo).replace('},','},\n   ')
  file.write(str(Admin))
  file.write('\n')
  file.write(yechizimasalan)
  file.close()

Admin={
  'userName':input('username: '),
  'userPass':input('userPass: '),
  'phone':input('phone: '),
  'userID':'0'
}
#Admin's info entered

ContactsInfo={
  'Admin':{Admin['userName']:Admin['phone']}
}
#informations save here
filee(Admin,ContactsInfo)


save_ac_name=[]
def make_account():
  #accountNum='user'+str(len(save_ac_name)+1)
  esm=fullname(input('Name: '),input('Family: '))
  accountNum=esm
  if esm in save_ac_name:
    print('This account already exists')
  else:
    ContactsInfo[accountNum]={}
    ContactsInfo[accountNum]['accountName']=esm
    ContactsInfo[accountNum]['secret']=input('secret: ')
    ContactsInfo[accountNum][esm]=input('phone: ')
  save_ac_name.append(esm)
  filee(Admin,ContactsInfo)


def del_contact_admin():
  fordelcontactadmin=input('What is the contact name?(full name) ')
  if fordelcontactadmin!=Admin['userName']:
    try:
      del ContactsInfo['Admin'][fordelcontactadmin]
      filee(Admin,ContactsInfo)
      print('Contact deleted succesfully')
    except:
      print('Contact name does not exist!')
  else:
    print('You cant delete yourself!')


def new_contact_admin():
  noidea=input('Enter name: ')
  nooidea=input('Enter lastname: ')
  nofidea=input('Enter phone number: ')
  kln_noidea=fullname(noidea,nooidea)
  ContactsInfo['Admin'][kln_noidea]= nofidea
  filee(Admin,ContactsInfo)
  print('contact saved succesfully.')


def admin_search():
  reshte_admin=input('Enter string: ')
  for i in ContactsInfo['Admin'].keys():
    if reshte_admin in i or reshte_admin in ContactsInfo['Admin'][i]:
      print(i,'=',ContactsInfo['Admin'][i])
  print('These are the results.')


def edit_admin():
  print('Which one do you want to edit?(username|userpass|phone|all)')
  admineditoption=input()
  if admineditoption=='username':
    temp=Admin['userName']
    Admin['userName']=input('New username: ')
    ContactsInfo['Admin'][Admin['userName']]=Admin['phone']
    del ContactsInfo['Admin'][temp]
    filee(Admin,ContactsInfo)
  elif admineditoption=='userpass':
    Admin['userPass']=input('New userpass: ')
    filee(Admin,ContactsInfo)
  elif admineditoption=='phone':
    #del ContactsInfo['Admin'][Admin['phone']]
    ContactsInfo['Admin'][Admin['userName']]=input('New Phone: ')
    Admin['phone']=ContactsInfo['Admin'][Admin['userName']]
    filee(Admin,ContactsInfo)
  elif admineditoption=='all':
    del ContactsInfo['Admin'][Admin['userName']]
    Admin['userName']=input('New username: ')
    Admin['userPass']=input('New userpass: ')
    #Admin['phone']==input('New Phone: ')
    ContactsInfo['Admin'][Admin['userName']]=input('New Phone: ')
    Admin['phone']=ContactsInfo['Admin'][Admin['userName']]
    filee(Admin,ContactsInfo)


def admin_access():
  print('Whose account do you want to access?(name_lastame)')
  whichname=input()
  if whichname in ContactsInfo.keys():
    print('You entered this account.')
    after_user_login(whichname)
    print('You are back as Admin.')
  else:
    print('User does not exist.')

#admin
def after_login():
  global Admin
  global ContactsInfo
  while True:
    print('What do you want to do? (sign up|new contact|del contact|del account|search|edit|access|exit)')
    adminjob=input()
    if adminjob=='exit':
      print('You are done.')
      break
    elif adminjob=='sign up':
      make_account()
      filee(Admin,ContactsInfo)
    elif adminjob=='new contact':
      new_contact_admin()
    elif adminjob=='del contact':
      del_contact_admin()
    elif adminjob=='del account':
      print('Which one?(mine|others)')
      wtdrn=input()
      if wtdrn=='mine':
        del Admin
        del ContactsInfo
        print('Everything is deleted.')
        break
      elif wtdrn=='others':
        askname=input('Users username(name_lastname): ')
        del ContactsInfo[askname]
        print('The account of user deleted')
    elif adminjob=='search':
      admin_search()
    elif adminjob=='edit':
      edit_admin()
    elif adminjob=='access':
      admin_access()
    else:
      print('I didnt understand.Try again.')
      

def log_in_admin():
  usrnme=input('Your Username: ')
  psswrd=input('Your Password: ')
  if usrnme==Admin['userName'] and psswrd==Admin['userPass']:
    print('You entered your account.')
    after_login()
  else:
    print('Wrong Username or Password.')


def new_user_contact(usrnme):
  noidea2=input('Enter name: ')
  nooidea2=input('Enter lastname: ')
  kln_noidea2=fullname(noidea2,nooidea2)
  nofidea2=input('Enter phone number: ')
  ContactsInfo[usrnme][kln_noidea2]= nofidea2
  print('contact saved succesfully.')
  filee(Admin,ContactsInfo)


def user_search(usrnme):
  reshte_user=input('Enter string: ')
  templist=[]
  for x in ContactsInfo[usrnme].keys():
    templist.append(x)
  templist=templist[2:]
  for i in templist:
    if reshte_user in i or reshte_user in ContactsInfo[usrnme][i]:
      print(i,'=',ContactsInfo[usrnme][i])
  print('These are the results.')


def edit_user(usrnme):
  print('Which one do you want to edit?(name|secret|phone|all)')
  usereditoption=input()
  if usereditoption=='name':
    te=input('New account name: ')
    te2=input('New account lastname: ')
    tempo=fullname(te,te2)
    ContactsInfo[tempo]={}
    ContactsInfo[tempo]=ContactsInfo[usrnme]
    ContactsInfo[tempo]['accountName']=tempo
    ContactsInfo[tempo][tempo]=ContactsInfo[tempo][usrnme]
    del ContactsInfo[tempo][usrnme]
    del ContactsInfo[usrnme]
    usrnme=tempo
    filee(Admin,ContactsInfo)
  elif usereditoption=='secret':
    newsecret=input('New secret: ')
    ContactsInfo[usrnme]['secret']=newsecret
    filee(Admin,ContactsInfo)
  elif usereditoption=='phone':
    newphone=input('New phone: ')
    ContactsInfo[usrnme][usrnme]=newphone
    filee(Admin,ContactsInfo)
  elif usereditoption=='all':
    te2=input('New account name: ')
    te22=input('New account lastname: ')
    tempo2=fullname(te2,te22)
    newsecret2=input('New secret: ')
    newphone2=input('New phone: ')
    ContactsInfo[tempo2]={}
    ContactsInfo[tempo2]=ContactsInfo[usrnme]
    ContactsInfo[tempo2]['accountName']=tempo2
    ContactsInfo[tempo2]['secret']=newsecret2
    ContactsInfo[tempo2][tempo2]=newphone2
    del ContactsInfo[tempo2][usrnme]
    del ContactsInfo[usrnme]
    usrnme=tempo2
    filee(Admin,ContactsInfo)


#search eshtebah khahad shod
#user
def after_user_login(usrnme):
  while True:
    print('What do you want to do? (new contact|del contact|del account|search|edit|exit)')
    userjob=input()
    if userjob=='exit':
      break
    elif userjob=='new contact':
      new_user_contact(usrnme)
    elif userjob=='del contact':
      del_contact(usrnme)
    elif userjob=='del account':
      del ContactsInfo[usrnme]
      print('Everything is deleted.')
      filee(Admin,ContactsInfo)
      break
    elif userjob=='search':
      user_search(usrnme)
    elif userjob=='edit':
      edit_user(usrnme)
      break



def del_contact(usrnme):
  fordelcontact=input('What is the contact name?(full name) ')
  if fordelcontact!=ContactsInfo[usrnme]['accountName']:
    try:
      del ContactsInfo[usrnme][fordelcontact]
      print('Contact deleted succesfully')
      filee(Admin,ContactsInfo)
    except:
      print('Contact name does not exist!')
  else:
    print('You cant delete yourself!')


def login():
  usrnme=input('Your Username(hint: name_lastname): ')
  psswrd=input('Your Password: ')
  if usrnme in ContactsInfo.keys():
    if ContactsInfo[usrnme]['secret']==psswrd:
      print('You entered your account.')
      after_user_login(usrnme)
    else:
      print('Wrong Password.')
  else:
    print('Username does not exist.')


#main menu
while True:
  print('Who are you? (admin|user|exit)')
  job=input()
  try:
    if job=='exit':
      print('You are done.')
      break
    elif job=='admin':
      log_in_admin()
      filee(Admin,ContactsInfo)
    elif job=='user':
      login()
  except:
    break

