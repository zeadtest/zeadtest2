def get_data_from_source():
    # هنا يمكنك إضافة منطق الحصول على البيانات
    return {"message": "مرحبًا بكم في CybeTerms! موقع يهتم بتثقيف المستخدمين حول الأمن السيبراني."}

#####################################
# main.py
import tkinter as tk
from tkinter import Button
from util import Carousel, print_settings_and_breakpoints

class CarouselApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Carousel Example")
        self.root.geometry("600x400")  # إعداد حجم نافذة التطبيق

        # إنشاء سلايدر
        self.carousel = Carousel(speed=4, fade_in=True, fade_delay=250)
        self.carousel.reel_width = 500  # عرض السلايدر
        self.carousel.update()

        # طباعة الإعدادات والنقاط
        print_settings_and_breakpoints()

        # إنشاء الأزرار للتفاعل مع السلايدر
        self.create_buttons()

    def create_buttons(self):
        # زر التحريك للأمام
        forward_button = Button(self.root, text="Move Forward", command=self.move_forward)
        forward_button.pack(pady=10)

        # زر التحريك للخلف
        backward_button = Button(self.root, text="Move Backward", command=self.move_backward)
        backward_button.pack(pady=10)

        # زر الـ Fade In
        fade_in_button = Button(self.root, text="Fade In", command=self.fade_in)
        fade_in_button.pack(pady=10)

    def move_forward(self):
        """تحريك السلايدر للأمام"""
        self.carousel.forward()

    def move_backward(self):
        """تحريك السلايدر للخلف"""
        self.carousel.backward()

    def fade_in(self):
        """محاكاة تأثير fade-in"""
        self.carousel.fade_in_items()

def main():
    # إنشاء واجهة التطبيق
    root = tk.Tk()
    app = CarouselApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
