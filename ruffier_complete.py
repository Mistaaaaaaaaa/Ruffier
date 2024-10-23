from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import *
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction
from instructions import txt_test1
from instructions import txt_test2
from instructions import txt_test3
from instructions import txt_sits
from ruffier import test
from kivy.clock impoer clock



imie = ''
wiek = 0
wynik1, wynik2, wynik3 = 0, 0, 0

class Screen1(Screen): 
    def switch(self):
       pass
      
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        h1 = BoxLayout(size_hint = (0.6,0.5))
        h2 = BoxLayout(size_hint = (0.6,0.5))
        v1 = BoxLayout(orientation = 'vertical', height = '80sp', padding = 10, spacing = 20)
        
        self.tekst_1 = Label(text =  txt_instruction )
        tekst_2 = Label(text = "Enter you name:", halign='left')
        tekst_3 = Label(text = "Enter your age:", halign='left')
        
        self.btn = Button(text = "Start", size_hint= (0.5,0.5), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        self.okienko1 = TextInput(multiline = False, size_hint = (1,0.6))
        self.okienko2 = TextInput(multiline = False, size_hint = (1,0.6))
        
        h1.add_widget(tekst_2)
        h1.add_widget(self.okienko1)
        
        h2.add_widget(tekst_3)
        h2.add_widget(self.okienko2)
        
        v1.add_widget(self.tekst_1)
        v1.add_widget(h1)
        v1.add_widget(h2)
        v1.add_widget(self.btn)
       
        self.add_widget(v1)
    def next(self):
       global imie
       global wiek
       imie = self.okienko1.text
       wiek = self.okienko2.text
       try:
   
          imie = imie
          wiek = int(wiek)
          self.manager.current = 'e2'
       except:
          self.tekst_1.text = "The data you have added is incorect. Please check and input the correct data."
         
                             
class Screen2(Screen):
     def switch(self):
        global winik1
        winik1 = self.okienko1.text
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        h1 = BoxLayout(size_hint = (0.6,0.5))
        h2 = BoxLayout(size_hint = (0.6,0.5))
        v1 = BoxLayout(orientation = 'vertical', height = '80sp', padding = 10, spacing = 20)
        
        self.tekst_1 = Label(text = txt_test1)
       
        
        self.btn = Button(text = "Next", size_hint= (0.5,0.5), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        self.okienko1 = TextInput(multiline = False, size_hint = (1,0.6))
       
        
        
        h1.add_widget(self.okienko1)
        
        
        v1.add_widget(self.tekst_1)
        v1.add_widget(h1)
        v1.add_widget(h2)
        v1.add_widget(self.btn)
       
        self.add_widget(v1)
     def next(self):
        try:
           global wynik1
           wynik1 = self.okienko1.text 
           wynik1 = int(wynik1)
           self.manager.current = 'e3'
        except:
           self.tekst_1.text = 'Please put in the correct puls'

class Screen3(Screen):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        h1 = BoxLayout(size_hint = (0.6,0.5))
        h2 = BoxLayout(size_hint = (0.6,0.5))
        v1 = BoxLayout(orientation = 'vertical', height = '80sp', padding = 10, spacing = 20)
        
        tekst_1 = Label(text = txt_sits)
        
        
        self.btn = Button(text = "Next", size_hint= (0.5,0.5), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
       
        v1.add_widget(tekst_1)
        v1.add_widget(h1)
        v1.add_widget(h2)
        v1.add_widget(self.btn)
       
        self.add_widget(v1)
     def next(self):
        self.manager.current = 'e4'   
class Screen4(Screen):
     def switch(self):
             global tekst2
             global tekst3
             tekst2 = self.okienko1.text
             tekst3 = self.okienko2.text
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        h1 = BoxLayout(size_hint = (0.6,0.5))
        h2 = BoxLayout(size_hint = (0.6,0.5))
        v1 = BoxLayout(orientation = 'vertical', height = '80sp', padding = 10, spacing = 20)
        
        self.tekst_1 = Label(text = txt_test3 )
        
        
        self.btn = Button(text = "Next", size_hint= (0.5,0.5), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        self.okienko1 = TextInput(multiline = False, size_hint = (1,0.6))
        self.okienko2 = TextInput(multiline = False, size_hint = (1,0.6))
        
      
        h1.add_widget(self.okienko1)
        
      
        h2.add_widget(self.okienko2)
        
        v1.add_widget(self.tekst_1)
        v1.add_widget(h1)
        v1.add_widget(h2)
        v1.add_widget(self.btn)
       
        self.add_widget(v1)
     def next(self):
        try:
           global wynik2
           global wynik3
           wynik2 = self.okienko1.text
           wynik3 = self.okienko2.text
           wynik2 = int(wynik2)
           wynik3 = int(wynik3)
           self.manager.current = 'e5'
        except:
           self.tekst_1.text = 'Please put in the correct puls.' 
class Screen5(Screen):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        h1 = BoxLayout(size_hint = (0.6,0.5))
        h2 = BoxLayout(size_hint = (0.6,0.5))
        v1 = BoxLayout(orientation = 'vertical', height = '80sp', padding = 10, spacing = 20)
        
        self.tekst_1 = Label(text = 'teskt 5'  )
        
       
        v1.add_widget(self.tekst_1)
        v1.add_widget(h1)
        v1.add_widget(h2)
        self.on_enter = self.przed
       
        self.add_widget(v1)
     def przed(self):
        global imie, wiek, wynik1, wynik2, wynik3
        self.tekst_1.text = 'Hello ' + imie + ' your result is ' + str(test(wynik1,wynik2,wynik3,wiek))
  

class Myapp(App):    
    def build(self):
        manager_ekranow = ScreenManager()

        manager_ekranow.add_widget(Screen1(name = 'e1'))
        
        manager_ekranow.add_widget(Screen2(name = 'e2'))
        
        manager_ekranow.add_widget(Screen3(name = 'e3'))
       
        manager_ekranow.add_widget(Screen4(name = 'e4'))
        
        manager_ekranow.add_widget(Screen5(name = 'e5'))
       
        
        
        return manager_ekranow



app = Myapp()
app.run()