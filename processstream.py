import tkinter as tk
from flask import Flask, render_template, Response
import datetime
import time
import os
import threading
import subprocess
#pip install flask
#sudo apt-get install lm-sensors
#sudo service kmod start
global mensagem
# Inicializar a mensagem

mensagem = ""
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    global mensagem
    while True:
        mensagem = subprocess.check_output("ps -ef", shell=True).decode().strip().replace("\n","<br>").replace("\r","<br>")
    
        message_label.config(text=mensagem)
        yield  f"data: {mensagem}\n\n"
        time.sleep(1)
        



@app.route('/time')
def time_stream():
    return Response(generate(), mimetype='text/event-stream')

def targets():
    app.run(host='0.0.0.0', port=5000, threaded=True)



    
# Criar a janela principal
root = tk.Tk()
root.title("Change Message")
root.geometry("630x400")
root.configure(bg='white')

# Adicionar um rótulo para exibir a mensagem
message_label = tk.Label(root, text=mensagem, bg='white', font=('Arial', 14))
message_label.pack(pady=20)





# Iniciar o loop principal da aplicação

  
t1 = threading.Thread(target=targets)
t1.start()
root.mainloop()
t1.join()
