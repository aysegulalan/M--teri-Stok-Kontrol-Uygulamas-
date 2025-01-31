from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        self.title = "Müşteri ve Ürün Yönetim Sistemi"  # Uygulama başlığını değiştirin

        self.products = []  # Ürünler için liste
        self.customers = []  # Müşteriler için liste

        self.main_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Menü düğmelerini oluştur
        self.create_menu()
        return self.main_layout

    def create_menu(self):
        """Ana menüyü oluştur ve göster."""
        self.main_layout.clear_widgets()

        # 6 buton oluştur
        button1 = Button(text="Ürünleri Görüntüle", size_hint=(1, 0.15), on_press=self.show_products)
        button2 = Button(text="Müşteriler ve Borçları", size_hint=(1, 0.15), on_press=self.show_customers)
        button3 = Button(text="Stok Kontrolü", size_hint=(1, 0.15), on_press=self.show_stock)
        button4 = Button(text="Yeni Müşteri Ekle", size_hint=(1, 0.15), on_press=self.add_customer_screen)
        button5 = Button(text="Yeni Ürün Ekle", size_hint=(1, 0.15), on_press=self.add_product_screen)
        button6 = Button(text="Satış Gir", size_hint=(1, 0.15), on_press=self.add_sales_screen)
        button7 = Button(text="Müşteri Sil", size_hint=(1, 0.15), on_press=self.delete_customer_screen)  # Yeni Buton

        self.main_layout.add_widget(button1)
        self.main_layout.add_widget(button2)
        self.main_layout.add_widget(button3)
        self.main_layout.add_widget(button4)
        self.main_layout.add_widget(button5)
        self.main_layout.add_widget(button6)
        self.main_layout.add_widget(button7)  # Yeni Buton

    def clear_layout(self):
        """Düzeni temizle."""
        self.main_layout.clear_widgets()

    def show_products(self, instance):
        self.clear_layout()
        if self.products:
            label = Label(text="Ürünler:\n" + "\n".join(f"{p['name']} - {p['stock']} adet" for p in self.products), size_hint=(1, 0.8))
        else:
            label = Label(text="Henüz eklenmiş bir ürün yok.", size_hint=(1, 0.8))
        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
        self.main_layout.add_widget(label)
        self.main_layout.add_widget(back_button)

    def show_customers(self, instance):
        self.clear_layout()
        if not self.customers:
            label = Label(text="Henüz eklenmiş bir müşteri yok.", size_hint=(1, 0.8))
            back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
            self.main_layout.add_widget(label)
            self.main_layout.add_widget(back_button)
            return

        # Müşterileri ve borçlarını göster
        for customer in self.customers:
            customer_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
            customer_label = Label(text=f"{customer['name']} - {customer['debt']}₺", size_hint=(0.6, 1))
            
            # Borç artırma ve azaltma butonları
            increase_button = Button(text="Borç Ekle", size_hint=(0.2, 1),
                                      on_press=lambda x, c=customer: self.show_debt_input(c, 'increase'))
            decrease_button = Button(text="Borç Sil", size_hint=(0.2, 1),
                                      on_press=lambda x, c=customer: self.show_debt_input(c, 'decrease'))
            
            customer_layout.add_widget(customer_label)
            customer_layout.add_widget(increase_button)
            customer_layout.add_widget(decrease_button)
            self.main_layout.add_widget(customer_layout)

        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
        self.main_layout.add_widget(back_button)

    def show_debt_input(self, customer, action):
        """Borç ekleme veya silme ekranını aç."""
        self.clear_layout()

        # Borç ekleme veya silme için başlık
        action_text = "Borç Ekle" if action == 'increase' else "Borç Sil"
        action_label = Label(text=f"{action_text} için bir miktar girin:", size_hint=(1, 0.1))
        debt_input = TextInput(hint_text="Borç Miktarı", size_hint=(1, 0.2))
        save_button = Button(
            text="Kaydet",
            size_hint=(1, 0.2),
            on_press=lambda x: self.update_debt(customer, action, debt_input.text),
        )
        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.show_customers(None))

        self.main_layout.add_widget(action_label)
        self.main_layout.add_widget(debt_input)
        self.main_layout.add_widget(save_button)
        self.main_layout.add_widget(back_button)

    def update_debt(self, customer, action, debt_amount):
        """Müşterinin borcunu artır veya azalt."""
        if debt_amount.isdigit() and int(debt_amount) > 0:
            amount = int(debt_amount)
            if action == 'increase':
                customer['debt'] += amount  # Borç artır
            elif action == 'decrease' and customer['debt'] >= amount:
                customer['debt'] -= amount  # Borç azalt
            else:
                print("Borç miktarı geçerli değil.")
        self.show_customers(None)  # Müşteriler ekranını tekrar güncelle

    def show_stock(self, instance):
        self.clear_layout()
        if self.products:
            label = Label(text="Stok Kontrolü:\n" + "\n".join(f"{p['name']} - {p['stock']} adet" for p in self.products), size_hint=(1, 0.8))
        else:
            label = Label(text="Stokta ürün bulunmamaktadır.", size_hint=(1, 0.8))
        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
        self.main_layout.add_widget(label)
        self.main_layout.add_widget(back_button)

    def add_customer_screen(self, instance):
        self.clear_layout()
        name_input = TextInput(hint_text="Müşteri Adı", size_hint=(1, 0.2))
        debt_input = TextInput(hint_text="Borç Miktarı", size_hint=(1, 0.2))
        save_button = Button(text="Kaydet", size_hint=(1, 0.2), on_press=lambda x: self.add_customer(name_input.text, debt_input.text))
        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
        self.main_layout.add_widget(name_input)
        self.main_layout.add_widget(debt_input)
        self.main_layout.add_widget(save_button)
        self.main_layout.add_widget(back_button)

    def add_customer(self, name, debt):
        if name and debt.isdigit():
            self.customers.append({"name": name, "debt": int(debt)})
        self.create_menu()

    def add_product_screen(self, instance):
        self.clear_layout()
        name_input = TextInput(hint_text="Ürün Adı", size_hint=(1, 0.2))
        stock_input = TextInput(hint_text="Stok Miktarı", size_hint=(1, 0.2))
        save_button = Button(text="Kaydet", size_hint=(1, 0.2), on_press=lambda x: self.add_product(name_input.text, stock_input.text))
        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
        self.main_layout.add_widget(name_input)
        self.main_layout.add_widget(stock_input)
        self.main_layout.add_widget(save_button)
        self.main_layout.add_widget(back_button)

    def add_product(self, name, stock):
        if name and stock.isdigit():
            self.products.append({"name": name, "stock": int(stock)})
        self.create_menu()

    def add_sales_screen(self, instance):
        self.clear_layout()
        if not self.customers or not self.products:
            label = Label(text="Önce müşteri ve ürün ekleyin.", size_hint=(1, 0.8))
            back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
            self.main_layout.add_widget(label)
            self.main_layout.add_widget(back_button)
            return

        customer_spinner = Spinner(text="Müşteri Seçin", values=[c["name"] for c in self.customers], size_hint=(1, 0.2))
        product_spinner = Spinner(text="Ürün Seçin", values=[p["name"] for p in self.products], size_hint=(1, 0.2))
        amount_input = TextInput(hint_text="Miktar", size_hint=(1, 0.2))
        price_input = TextInput(hint_text="Ürün Fiyatı", size_hint=(1, 0.2))

        total_price_label = Label(text="Toplam Fiyat: 0", size_hint=(1, 0.2))

        def update_total_price(instance, value):
            try:
                amount = int(amount_input.text)
                price = int(price_input.text)
                total_price_label.text = f"Toplam Fiyat: {amount * price}"
            except ValueError:
                total_price_label.text = "Toplam Fiyat: 0"

        amount_input.bind(text=update_total_price)
        price_input.bind(text=update_total_price)

        save_button = Button(
            text="Satışı Kaydet",
            size_hint=(1, 0.2),
            on_press=lambda x: self.add_sale(customer_spinner.text, product_spinner.text, amount_input.text, price_input.text),
        )

        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())

        self.main_layout.add_widget(customer_spinner)
        self.main_layout.add_widget(product_spinner)
        self.main_layout.add_widget(amount_input)
        self.main_layout.add_widget(price_input)
        self.main_layout.add_widget(total_price_label)
        self.main_layout.add_widget(save_button)
        self.main_layout.add_widget(back_button)

    def add_sale(self, customer_name, product_name, amount, price):
        if not amount.isdigit() or int(amount) <= 0 or not price.isdigit() or int(price) <= 0:
            print("Geçerli bir miktar ve fiyat girin.")
            return

        amount = int(amount)
        price = int(price)
        total_price = price * amount
        customer = next((c for c in self.customers if c["name"] == customer_name), None)
        product = next((p for p in self.products if p["name"] == product_name), None)

        if customer and product:
            if product["stock"] >= amount:
                product["stock"] -= amount
                customer["debt"] += total_price  # Toplam fiyat borca eklenir
                print(f"Satış eklendi: {customer_name} -> {amount} x {product_name}")
                self.create_menu()
            else:
                print("Yeterli stok yok.")
        else:
            print("Geçersiz müşteri veya ürün seçimi.")
        self.create_menu()

    def delete_customer_screen(self, instance):
        self.clear_layout()
        if not self.customers:
            label = Label(text="Henüz silinecek müşteri yok.", size_hint=(1, 0.8))
            back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())
            self.main_layout.add_widget(label)
            self.main_layout.add_widget(back_button)
            return

        customer_spinner = Spinner(text="Müşteri Seçin", values=[c["name"] for c in self.customers], size_hint=(1, 0.2))
        confirm_button = Button(text="Müşteriyi Sil", size_hint=(1, 0.2), on_press=lambda x: self.confirm_delete_customer(customer_spinner.text))
        back_button = Button(text="Geri Dön", size_hint=(1, 0.2), on_press=lambda x: self.create_menu())

        self.main_layout.add_widget(customer_spinner)
        self.main_layout.add_widget(confirm_button)
        self.main_layout.add_widget(back_button)



    def confirm_delete_customer(self, customer_name):
        """Müşteri silme işlemi için onay popup'ı göster."""
        customer = next((c for c in self.customers if c['name'] == customer_name), None)

        if not customer:
            return

        # Silme onay popup'ı
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"{customer_name} adlı müşteriyi silmek istediğinizden emin misiniz?"))

        # Evet butonu
        yes_button = Button(text="Evet", size_hint=(1, 0.2))
        yes_button.bind(on_press=lambda instance: self.delete_customer(customer, popup))

        # Hayır butonu
        no_button = Button(text="Hayır", size_hint=(1, 0.2))
        no_button.bind(on_press=lambda instance: popup.dismiss())  # Hayır'a basıldığında sadece popup'ı kapat

        content.add_widget(yes_button)
        content.add_widget(no_button)

        popup = Popup(title="Müşteri Silme Onayı", content=content, size_hint=(0.8, 0.4))
        popup.open()

    def delete_customer(self, customer, popup):
        """Müşteri silme işlemi."""
        if customer in self.customers:
            self.customers.remove(customer)
        popup.dismiss()  # Popup'ı kapatalım
        self.create_menu()  # Ana menüyü yeniden oluştur


if __name__ == '__main__':
    MyApp().run()
    
  #kodumuz bu kadardır.   