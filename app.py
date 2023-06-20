from flask import Flask, render_template, request
import csv
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/criar_ordem', methods=['POST'])
def criar_ordem():
    numero_ordem = request.form['numero_ordem']
    data_ordem = datetime.datetime.now().strftime("%d/%m/%Y")
    nome_cliente = request.form['nome_cliente']
    endereco_cliente = request.form['endereco_cliente']
    telefone_cliente = request.form['telefone_cliente']
    email_cliente = request.form['email_cliente']
    descricao_servico = request.form['descricao_servico']
    materiais_necessarios = request.form['materiais_necessarios']

    ordem = [numero_ordem, data_ordem, nome_cliente, endereco_cliente, telefone_cliente, email_cliente, descricao_servico, materiais_necessarios]

    with open('ordens_de_servico.csv', 'a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(ordem)

    return "Ordem de serviço criada com sucesso!"

@app.route('/pesquisar_ordem', methods=['POST'])
def pesquisar_ordem():
    numero_ordem = request.form['numero_ordem']

    with open('ordens_de_servico.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        encontrada = False
        for linha in leitor_csv:
            if linha[0] == numero_ordem:
                encontrada = True
                return f"""
                Número da Ordem: {linha[0]} <br>
                Data da Ordem: {linha[1]} <br>
                Nome do Cliente: {linha[2]} <br>
                Endereço do Cliente: {linha[3]} <br>
                Telefone do Cliente: {linha[4]} <br>
                E-mail do Cliente: {linha[5]} <br>
                Descrição do Serviço: {linha[6]} <br>
                Materiais Necessários: {linha[7]}
                """
        if not encontrada:
            return "Ordem de serviço não encontrada."

if __name__ == '__main__':
    app.run(debug=True)
