import tkinter as tk

def update_text():
    input_text = entry.get()  # Obtém o conteúdo da entrada de texto
    output_text.set('')  # Reseta o conteúdo do campo de saída
    for i in range(1, len(input_text) + 1):
        output_text.set(output_text.get() + input_text[:i] + '\n')  # Exibe o texto progressivamente

# Configurações da janela
root = tk.Tk()
root.title("Programa com Interface Gráfica")
root.geometry("400x400")  # Tamanho da janela
root.configure(bg='lightblue')  # Define cor de fundo

# Label para o título
title_label = tk.Label(root, text="Exibindo o conteúdo do texto:", font=('Helvetica', 12, 'bold'), bg='lightblue')
title_label.pack(pady=10)

# Entrada de texto
entry = tk.Entry(root, font=('Helvetica', 12))
entry.pack(pady=5, fill=tk.BOTH, expand=True)

# Botão para atualizar
update_button = tk.Button(root, text="Exibir", command=update_text, font=('Helvetica', 12))
update_button.pack(pady=10)

# Campo para exibir a saída
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, font=('Helvetica', 14), bg='lightblue', fg='darkblue', justify='left')
output_label.pack(pady=10, fill=tk.BOTH, expand=True)

# Botão de entrada para terminar o programa
exit_button = tk.Button(root, text="Sair", command=root.destroy, font=('Helvetica', 12))
exit_button.pack(pady=10)

root.mainloop()
