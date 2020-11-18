def msgs_errors_campo_num(valor_campo, nome_campo, lista_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_erros [nome_campo] = 'Não inclua número neste campo' 