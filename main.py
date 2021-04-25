# from kivymd.uix.boxlayout import BoxLayout
from kivy.event import EventDispatcher
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.camera import Camera
from kivy.uix.label import Label
import webbrowser
import random
import requests
#Builder String
helper_string = '''
ScreenManager:
    Welcome:
    Pref1:
    Pref2:
    Pref3:
    Pref4:
    Pref5:
    Cam:
    Pred:
    
<Welcome>:
    name: 'hello'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Welcome to moddy'
            elevation:8 
        MDLabel:
            id: text_change
            text:'MOODY'
            halign: 'center'
            theme_text_color: 'Custom'
            text_color : 79/255,195/255,247/255,1
            font_style : 'H2'
        MDBottomAppBar:
            MDToolbar:
                title: 'Lets Begin'
                icon: 'arrow-right'
                type: 'bottom'
                on_action_button:
                    root.manager.current = 'chips'
                    root.manager.transition.direction = 'left'
        
<Pref1>
    name: 'chips'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Language'
            elevation:8 
        ScrollView:
            MDGridLayout:
                cols:1
                adaptive_height:True
                padding:dp(80),dp(50)
                spacing:dp(15)
            
                MDChooseChip:
                    pos_hint: {'center_x':0.55,'center_y':0.5}
                    MDLabel:
                        text: 'Language Selected'
                        text_color : 79/255,195/255,247/255,1
                    MDChip:
                        label:'Hindi'
                        text: 'Hindi'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                        icon:''
                        size : (dp(30),dp(50))
                        spacing:sp(15)
                        on_press:app.selected_lang('Hindi')
                        on_release: 
                            root.manager.current = 'HindiArt'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'English'
                        text: 'English'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        icon:''
                        on_press:app.selected_lang('English')
                        on_release: 
                            root.manager.current = 'EnglishArt'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Gujarati'
                        text: 'Gujarati'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                
                        size : (dp(30),dp(50))
                        icon:''
                        on_press:app.selected_lang('Gujarati')
                        on_release: 
                            root.manager.current = 'GujaratiArt'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Punjabi'
                        text: 'Punjabi'
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        selected_chip_color: 0,0,1,1
                        icon:''
                        on_press:app.selected_lang('Punjabi')
                        on_release: 
                            root.manager.current = 'PunjabiArt'
                            root.manager.transition.direction = 'left'
<Pref2>
    name: 'HindiArt'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Hindi Artist'
            elevation:8
        ScrollView:
            MDGridLayout:
                cols:1
                adaptive_height:True
                padding:dp(80),dp(50)
                spacing:dp(15)
                
            
                MDChooseChip:
                    pos_hint: {'center_x':0.55,'center_y':0.5}
                    MDLabel:
                        text: 'Language Selected'
                        text_color : 79/255,195/255,247/255,1
                    MDChip:
                        label:'AS'
                        text: 'Arijit Singh'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                        icon:''
                        size : (dp(30),dp(50))
                        spacing:sp(15)
                        on_press: app.selected_art('Arijit Singh')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Darshan Raval'
                        text: 'Darshan Raval'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Darshan Raval')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Ritviz'
                        text: 'Ritviz'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                
                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Ritviz')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Shreya ghoshal'
                        text: 'Shreya ghoshal'
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        selected_chip_color: 0,0,1,1
                        icon:''
                        on_press: app.selected_art('Shreya ghoshal')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
<Pref3>

    name: 'EnglishArt'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'English Artist'
            elevation:8
        ScrollView:
            MDGridLayout:
                cols:1
                adaptive_height:True
                padding:dp(80),dp(50)
                spacing:dp(15)
                
            
                MDChooseChip:
                    pos_hint: {'center_x':0.55,'center_y':0.5}
                    MDLabel:
                        text: 'Language Selected'
                        text_color : 79/255,195/255,247/255,1
                    MDChip:
                        label:'HS'
                        text: 'Harry Styles'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                        icon:''
                        size : (dp(30),dp(50))
                        on_press: app.selected_art('Harry Styles')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'ES'
                        text: 'Ed Sheeran'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Ed Sheeran')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Imagine Dragons'
                        text: 'Imagine Dragons'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                
                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Imagine Dragons')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Coldplay'
                        text: 'Coldplay'                   
                        
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        selected_chip_color: 0,0,1,1
                        icon:''
                        on_press: app.selected_art('Coldplay')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
<Pref4>
    name: 'GujaratiArt'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Gujarati Artist'
            elevation:8
    
        ScrollView:
            MDGridLayout:
                cols:1
                adaptive_height:True
                padding:dp(80),dp(50)
                spacing:dp(15)
                
            
                MDChooseChip:
                    pos_hint: {'center_x':0.55,'center_y':0.5}
                    MDLabel:
                        text: 'Language Selected'
                        text_color : 79/255,195/255,247/255,1
                    MDChip:
                        label:'Sachin-Jigar'
                        text: 'Sachin-Jigar'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                        icon:''
                        size : (dp(30),dp(50))
                        spacing:sp(15)
                        on_press: app.selected_art('Sachin-Jigar')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Falguni Pathak'
                        text: 'Falguni Pathak'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Falguni Pathak')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Kinjal Dave'
                        text: 'Kinjal Dave'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                
                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Kinjal Dave')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Jigardan Gadhvi'
                        text: 'Jigardan Gadhvi'
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        selected_chip_color: 0,0,1,1
                        icon:''
                        on_press: app.selected_art('Jigardan Gadhvi')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
<Pref5>
    name: 'PunjabiArt'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Punjabi Artist'
            elevation:8
        ScrollView:
            MDGridLayout:
                cols:1
                adaptive_height:True
                padding:dp(80),dp(50)
                spacing:dp(15)
                
            
                MDChooseChip:
                    pos_hint: {'center_x':0.55,'center_y':0.5}
                    MDLabel:
                        text: 'Language Selected'
                        text_color : 79/255,195/255,247/255,1
                    MDChip:
                        label:'karan aujla'
                        text: 'karan aujla'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                        icon:''
                        size : (dp(30),dp(50))
                        spacing:sp(15)
                        on_press: app.selected_art('karan aujla')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Sidhu Moose Wala'
                        text: 'Sidhu Moose Wala'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Sidhu Moose Wala')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Diljit Dosanjh'
                        text: 'Diljit Dosanjh'
                        selected_chip_color: 0,0,1,1
                        size_hint_x:1
                
                        size : (dp(30),dp(50))
                        icon:''
                        on_press: app.selected_art('Diljit Dosanjh')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
                    MDChip:
                        label:'Harrdy Sandhu'
                        text: 'Harrdy Sandhu'
                        size_hint_x:1

                        size : (dp(30),dp(50))
                        selected_chip_color: 0,0,1,1
                        icon:''
                        on_press: app.selected_art('Harrdy Sandhu')
                        on_release: 
                            root.manager.current = 'Camera'
                            root.manager.transition.direction = 'left'
<Cam>
    name:'Camera'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Camera'
            elevation:8 
        Camera:
            id:camera
            play: True
            resolution: (800, 800)
        
        MDChooseChip:
            MDChip:
                text: 'Retry'
                selected_chip_color: 0,0,1,1
                font_size: 20
                pos_hint: {'center_x':0.55,'center_y':0.5}
                icon:''
                on_press:camera.play = True
            MDChip:
                text: 'Capture'
                selected_chip_color: 0,0,1,1
                icon:''
                font_size: 20
                pos_hint: {'center_x':0.55,'center_y':0.5}
                on_press: 
                    camera.play = False
                    root.take_pic()
        MDBottomAppBar:
            MDToolbar:
                title: 'Lets Predict'
                icon: 'arrow-right'
                type: 'bottom'
                on_action_button:
                    root.manager.current = 'Predict'
                    root.manager.transition.direction = 'left'
<Pred>
    
    name:'Predict'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Prediction'
            elevation:8
        MDLabel:
            text: "Emotion:" + root.respon
            halign: 'center'
            theme_text_color: 'Custom'
            text_color : 79/255,195/255,247/255,1
            font_style : 'H3'
        MDFillRoundFlatButton
            icon: ''
            text: 'Click to Predict Your Emotion'
            text_size:(200,200)
            user_font_size: '100sp'
            size_hint:(None, None)
            halign:'center'
            on_press:root.send_img()
        MDBottomAppBar:
            MDToolbar:
                title: 'Lets search for music'
                icon: 'arrow-right'
                type: 'bottom'
                on_action_button:app.redirect()



'''
class Welcome(Screen):
    pass
class Pref1(Screen):
    pass
class Pref2(Screen):
    pass
class Pref3(Screen):
    pass
class Pref4(Screen):
    pass
class Pref5(Screen):
    pass
class Cam(Screen):
    def take_pic(self):
        self.cam_obj = self.ids['camera']

        self.cam_obj.export_as_image().save("Images/pic.jpg")

class Pred(Screen):
    respon = StringProperty()
    def send_img(self, *args):
        url = "https://emotion-detection-api2.herokuapp.com/predict"

        payload = {}
        files = [
            ("image", ("Neutral2.jpg", open("Images/pic.jpg", "rb"), "image/jpeg"))
        ]
        headers = {}

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files
        )
        

        obj = response.json()
        self.respon= obj['emotion_detected']
        return self.respon
    

sm = ScreenManager()

sm.add_widget(Welcome(name = 'hello'))
sm.add_widget(Pref1(name='chips'))
sm.add_widget(Pref2(name='HindiArt'))
sm.add_widget(Pref3(name='EnglishArt'))
sm.add_widget(Pref4(name='GujaratiArt'))
sm.add_widget(Pref5(name='PunjabiArt'))
sm.add_widget(Cam(name='Camera'))
sm.add_widget(Pred(name='Predict'))


class Moody(MDApp):
    def build(self):
        self.language = ''
        self.artist = ''
        response = Pred()
        self.resp = response.send_img()
        self.song = ''
        self.theme_cls.theme_style = 'Dark'
        
        
        # self.theme_cls.primary_hue = 500
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)
        return screen
    
    

    def selected_lang(self,instance):
        self.language = instance
        print(self.language)

    def selected_art(self,instance):

        self.artist = instance
        print(self.artist)

    def choose_song(self):
        song = ''
        if self.resp == 'Happy':
            genre = ['upbeat','happy','party','energetic','joyful','celebration','cheerful','Exciting','pop','ambience','rock','rap']
            song = random.choice(genre)
        elif self.resp == 'Neutral':
            genre = ['cheerful','calm','neutral','soothing','relaxing','emotional','hopeful','soft','jazz','opera','orchestra']
            song = random.choice(genre)
        elif self.resp == 'Sad':
            genre = ['soft','calm','soothing','soul','jazz','ballad','heartache','heart touching','emotional']
            song = random.choice(genre)
        elif self.resp == 'Surprised':
            genre = ['surprise','rap','hiphop','disco','rock','electronic music','Trance']
            song = random.choice(genre)
        elif self.resp == 'Fearful':
            genre = ['deep','instrumental','jazz','jazz fussion','classical']
            song = random.choice(genre)
        elif self.resp == 'Disgusted':
            genre = ['metal','rock','reggae']
            song = random.choice(genre)
        elif self.resp == 'Angry':
            genre = ['rock','metal','heavy metal','electronic music','Trance','pop','hiphop']
            song = random.choice(genre)

        return song
        
    def redirect(self):
        self.song=self.choose_song()
        link = f"https://www.youtube.com/results?search_query={self.artist}+{self.song}+{self.language}+song"
        webbrowser.open(link)


Moody().run()