print('Welcome to Terminal Apps Launcher!')
print('___________________________________________________')
print('Copyright HappyPr0gramming, all rights reserved')

import importlib

while True:
    print('1) Legal')
    print('2) Launch')
    print('3) Documentation')

    choice = input('>>> ')

    if choice == '1':
        print('Copyright HappyPr0gramming, all rights reserved')
    elif choice == '2':
        print('Which app would you like to launch?')
        app_select = input('>>> ')
        try:
            app = importlib.import_module(app_select)
            print('App launched correctly!')
        except:
            print('App failed to launch!')
    elif choice == '3':
        print('To be able to launch an app with this launcher, you need to first add the .py file to this folder!')