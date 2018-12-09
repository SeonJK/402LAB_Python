import gugudan
import ctypes

print(gugudan.__doc__)
value = gugudan.gugudan(10)

ctypes.windll.user32.MessageBoxW(None, str(value), "gugudan MessageBox", 0)