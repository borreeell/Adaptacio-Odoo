def reinicia_sequencia(env, sequence_code, new_value=1):
    #Busca la sequencia per codi
    sequence = env['ir.sequence'].search([('code', '=', sequence_code)], limit = 1)

    if sequence:
        sequence.write({'number_next': new_value})
        print(f'Sequencia {sequence_code} reiniciada a {new_value}')
    else: 
        print(f"Sequencia {sequence_code} no trobada")

