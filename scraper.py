import requests
from bs4 import BeautifulSoup
import config

# دالة لاستخراج الروابط المخفضة من موقع AliExpress
def extract_discounted_link(product_url):
    try:
        # استخدام BeautifulSoup لاستخراج معلومات الصفحة من AliExpress والبحث عن التخفيضات
        page = requests.get(product_url, headers={'App-Key': config.app_key})
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'html.parser')

        # يمكنك إضافة المزيد من الخطوات هنا لفحص الصفحة والبحث عن تخفيض السلة
        # على سبيل المثال، يمكنك البحث عن عناصر السلة والتحقق من وجود تخفيضات عليها

        # إذا وجدت تخفيضات على السلة، قم بإعادة تشكيل الرابط بتخفيض
        cart_discounted_link = "الرابط بتخفيض على السلة"
        return cart_discounted_link

        # إذا لم توجد تخفيضات على السلة، قم بإعادة رابط المنتج كما هو
        return product_url
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "حدثت مشكلة أثناء جلب البيانات من AliExpress."

# دالة لاستخراج الروابط المخفضة على السلة
def extract_cart_discounted_link(product_url):
    try:
        # استخدام BeautifulSoup لاستخراج معلومات الصفحة من AliExpress والبحث عن التخفيضات على السلة
        page = requests.get(product_url, headers={'App-Key': config.app_key})
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'html.parser')

        # يمكنك إضافة الخطوات اللازمة هنا لفحص وجود تخفيضات على السلة

        # إذا وجدت تخفيضات على السلة، قم بإعادة تشكيل الرابط بتخفيض
        cart_discounted_link = "الرابط بتخفيض على السلة"
        return cart_discounted_link

        # إذا لم توجد تخفيضات على السلة، قم بإعادة رابط المنتج كما هو
        return product_url
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "حدثت مشكلة أثناء جلب البيانات من AliExpress."
