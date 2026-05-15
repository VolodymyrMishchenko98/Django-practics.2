from django.http import HttpResponse


def get_layout(title, content):
    menu = """
    
    <nav>
        <a href="/">Головна</a>
        <a href="/about/">Про нас</a>
        <a href="/products/">Товари</a>
        <a href="/students/">Студенти</a>
        <a href="/profile/">Профіль</a>
        <a href="/contacts/">Контакти</a>
        <a href="/uni/">Університет (ДЗ)</a>
    </nav>
    <hr>
    <h1>""" + title + """</h1>
    <div>""" + content + """</div>
    """
    return HttpResponse(menu)


def index(request):
    return get_layout("Головна сторінка", "Ласкаво просимо до нашого першого проєкту!")

def about(request):
    return get_layout("Про нас", "Інформація про нашу команду розробників.")

def contacts(request):
    return get_layout("Контакти", "Зв'яжіться з нами: +380 00 000 00 00")

# --- Практична №2 ---
def products(request):
    items = """
    <ul>
        <li>Ноутбук - 25000 грн</li>
        <li>Мишка - 700 грн</li>
        <li>Клавіатура - 1200 грн</li>
    </ul>
    """
    return get_layout("Наші товари", items)

def students(request):
    table = """
    <table border="1">
        <tr><th>Ім’я</th><th>Вік</th><th>Курс</th></tr>
        <tr><td>Іван</td><td>18</td><td>Python</td></tr>
        <tr><td>Марія</td><td>20</td><td>Django</td></tr>
    </table>
    """
    return get_layout("Список студентів", table)

# --- Практична №4 ---
def profile(request):
    name, age, city = "Іван", 18, "Київ"
    content = f"<p>Ім'я: {name}</p><p>Вік: {age}</p><p>Місто: {city}</p>"
    return get_layout("Профіль користувача", content)


def university(request):
    content = """
    <p>Це головна сторінка університету. Виберіть розділ:</p>
    <ul>
        <li><a href="/uni/courses/">Наші курси</a></li>
        <li><a href="/uni/teachers/">Викладачі</a></li>
    </ul>
    """
    return get_layout("Мінісайт Університету", content)