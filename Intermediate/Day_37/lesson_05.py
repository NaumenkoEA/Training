from functools import wraps

is_logged_in =True

def login_required(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if is_logged_in :
                print("Доступ разрешен")
                result = func(*args,**kwargs)
                return result
            else:
                print("Сначала войдите в аккаунт!")
        return wrapper
     
@login_required
def show_profile(username):
    print(f"Профиль пользователя: {username}")

show_profile("Alex")
        